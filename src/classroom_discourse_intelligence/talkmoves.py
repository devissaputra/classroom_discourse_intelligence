from __future__ import annotations

import re
import hashlib
import json
import zipfile
from pathlib import Path
from urllib.request import urlopen

import pandas as pd
from sklearn.model_selection import GroupShuffleSplit

DOWNLOAD_URL="https://platform.k12-ai-infrastructure.org/datasets/9/talkmoves/version/9/download/start/?source=cli"
TEACHER_TAG_MAP={1:0,2:1,3:2,4:3,5:4,8:5,9:6}

def parse_teacher_tag(value):
    if pd.isna(value):
        return None
    match=re.match(r"\s*(\d+)",str(value))
    if not match:
        return None
    return TEACHER_TAG_MAP.get(int(match.group(1)))

def download_and_extract(cache_dir: str | Path):
    cache=Path(cache_dir)
    cache.mkdir(parents=True,exist_ok=True)
    archive=cache/"talkmoves.zip"
    extracted=cache/"extracted"
    if not archive.exists():
        with urlopen(DOWNLOAD_URL,timeout=120) as response:
            archive.write_bytes(response.read())
    if not extracted.exists():
        extracted.mkdir(parents=True)
        with zipfile.ZipFile(archive) as zf:
            zf.extractall(extracted)
    return extracted

def load_teacher_utterances(root: str | Path):
    rows=[]; skipped=[]; seen_records=set()
    for path in sorted(Path(root).rglob("*.xlsx")):
        if path.name.startswith("~"):
            continue
        try:
            frame=pd.read_excel(path,engine="openpyxl")
        except Exception as exc:
            skipped.append({"file":str(path),"reason":f"read_error:{type(exc).__name__}"})
            continue
        required={"Sentence","Teacher Tag"}
        if not required.issubset(frame.columns):
            skipped.append({"file":str(path),"reason":"missing_required_columns"})
            continue
        transcript_rows=[]
        for _,row in frame.iterrows():
            label=parse_teacher_tag(row.get("Teacher Tag"))
            text=row.get("Sentence")
            if label is None or pd.isna(text):
                continue
            text=str(text).strip()
            if not text:
                continue
            transcript_rows.append({"text":text,"label":int(label)})
        if not transcript_rows:
            continue
        # Deduplicate archive copies by content, not filename. Two copies with
        # different filenames must never become independent train/test groups.
        record_key=hashlib.sha256(json.dumps(transcript_rows,sort_keys=True,ensure_ascii=False).encode()).hexdigest()
        if record_key in seen_records:
            skipped.append({"file":str(path.relative_to(root)),"reason":"duplicate_transcript_content"})
            continue
        seen_records.add(record_key)
        # Copies with the same text but revised annotations still share a group.
        text_key=hashlib.sha256(json.dumps([r["text"] for r in transcript_rows],ensure_ascii=False).encode()).hexdigest()
        rows.extend({**row,"transcript":text_key,"source_file":str(path.relative_to(root))} for row in transcript_rows)
    if not rows:
        raise ValueError("no labeled teacher utterances were parsed")
    return pd.DataFrame(rows),skipped

def transcript_split(frame: pd.DataFrame, seed: int=42):
    groups=frame["transcript"].to_numpy()
    outer=GroupShuffleSplit(n_splits=1,test_size=.20,random_state=seed)
    dev_idx,test_idx=next(outer.split(frame,frame["label"],groups))
    dev=frame.iloc[dev_idx].reset_index(drop=True)
    test=frame.iloc[test_idx].reset_index(drop=True)
    inner=GroupShuffleSplit(n_splits=1,test_size=.20,random_state=seed)
    train_idx,val_idx=next(inner.split(dev,dev["label"],dev["transcript"]))
    train=dev.iloc[train_idx].reset_index(drop=True)
    validation=dev.iloc[val_idx].reset_index(drop=True)
    return train,validation,test

def assert_group_disjoint(train,validation,test):
    sets=[set(x["transcript"]) for x in (train,validation,test)]
    if sets[0]&sets[1] or sets[0]&sets[2] or sets[1]&sets[2]:
        raise ValueError("transcript leakage detected")
    return True
