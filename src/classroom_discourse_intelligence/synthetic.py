import numpy as np,pandas as pd

def make_transcript(n=240,seed=43):
    rng=np.random.default_rng(seed); teacher=['Why do you think that happened?','Good, now consider the evidence in the graph.','What is the definition?','How would you explain the pattern?','Try another example because your first one changes two variables.']; student=['I think it happens because the input changes.','The answer is three.','For example, the second case has a lower value.','Building on your idea, the graph also changes after time four.','I am not sure yet.']
    rows=[]
    for i in range(n):
        role='teacher' if rng.random()<.47 else 'student'; rows.append({'turn':i,'role':role,'speaker':'T' if role=='teacher' else f'S{rng.integers(1,7)}','text':rng.choice(teacher if role=='teacher' else student)})
    return pd.DataFrame(rows)
