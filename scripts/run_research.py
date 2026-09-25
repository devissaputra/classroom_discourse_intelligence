import json
import sys
from collections import Counter
from pathlib import Path

import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, f1_score
from sklearn.pipeline import Pipeline

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"src"))
from classroom_discourse_intelligence.talkmoves import (
    assert_group_disjoint,download_and_extract,load_teacher_utterances,transcript_split
)

SEED=42

def metrics(y_true,y_pred):
    return {
        "accuracy":float(accuracy_score(y_true,y_pred)),
        "macro_f1":float(f1_score(y_true,y_pred,average="macro",zero_division=0)),
        "weighted_f1":float(f1_score(y_true,y_pred,average="weighted",zero_division=0)),
        "classification_report":classification_report(y_true,y_pred,output_dict=True,zero_division=0),
        "confusion_matrix":confusion_matrix(y_true,y_pred).tolist(),
    }

def main():
    extracted=download_and_extract(ROOT/".cache"/"talkmoves")
    frame,skipped=load_teacher_utterances(extracted)
    train,validation,test=transcript_split(frame,SEED)
    assert_group_disjoint(train,validation,test)

    majority=Counter(train["label"]).most_common(1)[0][0]
    majority_pred=np.full(len(test),majority,dtype=int)

    model=Pipeline([
        ("tfidf",TfidfVectorizer(ngram_range=(1,2),min_df=2,max_features=50000,sublinear_tf=True)),
        ("logit",LogisticRegression(max_iter=4000,class_weight="balanced",random_state=SEED)),
    ])
    model.fit(train["text"],train["label"])
    prediction=model.predict(test["text"])

    result={
        "research_bundle":True,
        "dataset":"TalkMoves",
        "source":"Suresh et al., LREC 2022",
        "license":"CC BY-NC-SA 4.0",
        "seed":SEED,
        "parsed_utterances":int(len(frame)),
        "parsed_transcripts":int(frame["transcript"].nunique()),
        "skipped_files":skipped,
        "label_distribution":{str(k):int(v) for k,v in sorted(Counter(frame["label"]).items())},
        "splits":{
            "train":{"utterances":int(len(train)),"transcripts":int(train["transcript"].nunique())},
            "validation":{"utterances":int(len(validation)),"transcripts":int(validation["transcript"].nunique())},
            "test":{"utterances":int(len(test)),"transcripts":int(test["transcript"].nunique())},
        },
        "no_transcript_overlap":True,
        "majority_baseline":{"majority_label":int(majority),**metrics(test["label"],majority_pred)},
        "tfidf_logistic":metrics(test["label"],prediction),
        "primary_metric":"macro_f1",
    }
    out=ROOT/"results"; out.mkdir(exist_ok=True)
    (out/"research_metrics.json").write_text(json.dumps(result,indent=2),encoding="utf-8")
    print(json.dumps(result,indent=2))

if __name__=="__main__":
    main()
