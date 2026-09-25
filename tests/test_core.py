import pandas as pd

from classroom_discourse_intelligence.core import annotate,discourse_summary
from classroom_discourse_intelligence.talkmoves import parse_teacher_tag,transcript_split,assert_group_disjoint

def test_descriptive_core_still_operates():
    df=pd.DataFrame({"role":["teacher","student"],"text":["Why do you think that?","Because it is equal"]})
    assert "move" in annotate(df).columns
    assert "open_question_rate" in discourse_summary(df)

def test_official_teacher_tag_mapping():
    assert parse_teacher_tag("1") == 0
    assert parse_teacher_tag("9 - something") == 6
    assert parse_teacher_tag("7") is None
    assert parse_teacher_tag(None) is None

def test_transcript_split_has_no_group_overlap():
    rows=[]
    for g in range(20):
        for i in range(4):
            rows.append({"text":f"text {g} {i}","label":i%2,"transcript":f"t{g}.xlsx"})
    frame=pd.DataFrame(rows)
    train,val,test=transcript_split(frame,seed=42)
    assert assert_group_disjoint(train,val,test)
    assert len(train)+len(val)+len(test)==len(frame)
