import pandas as pd
from classroom_discourse_intelligence.core import annotate,discourse_summary

print("Synthetic software fixture only; not an empirical TalkMoves result.")
df=pd.DataFrame({
    "role":["teacher","student","teacher","student"],
    "text":["Why do you think that?","Because the parts are equal.","Good, explain more.","I think both fractions match."]
})
print(annotate(df))
print(discourse_summary(df))
