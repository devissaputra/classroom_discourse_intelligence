from __future__ import annotations
import re,pandas as pd

def classify_move(role:str,text:str)->str:
    t=(text or '').lower()
    if '?' in t and any(x in t for x in ['why','how','what do you think','explain']): return 'open_question'
    if '?' in t: return 'closed_question'
    if role=='teacher' and any(x in t for x in ['good','notice','try','consider','because you']): return 'feedback'
    if role=='student' and any(x in t for x in ['because','for example','therefore','i think']): return 'elaboration'
    if any(x in t for x in ['as you said','your idea','building on']): return 'uptake'
    return 'other'
def discourse_summary(df:pd.DataFrame)->dict:
    d=df.copy(); d['move']=[classify_move(r.role,r.text) for r in d.itertuples()]; teacher=d.role.eq('teacher')
    q=d.move.isin(['open_question','closed_question'])
    return {'teacher_talk_share':float(teacher.mean()),'open_question_rate':float((d.move=='open_question').sum()/max(1,q.sum())),'feedback_rate':float((d.move=='feedback').mean()),'learner_elaboration_rate':float(((d.move=='elaboration') & d.role.eq('student')).sum()/max(1,d.role.eq('student').sum())),'uptake_rate':float((d.move=='uptake').mean())}
def annotate(df:pd.DataFrame)->pd.DataFrame:
    out=df.copy(); out['move']=[classify_move(r.role,r.text) for r in out.itertuples()]; return out
