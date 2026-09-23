import pandas as pd
from classroom_discourse_intelligence.core import classify_move,discourse_summary,annotate

def test_classifier():
    assert classify_move('teacher','Why do you think this happened?')=='open_question'
    assert classify_move('student','I think this because evidence changes')=='elaboration'

def test_summary():
    d=pd.DataFrame([{'role':'teacher','text':'Why do you think?'},{'role':'student','text':'I think because x'}]); m=discourse_summary(d); assert 0<=m['teacher_talk_share']<=1
