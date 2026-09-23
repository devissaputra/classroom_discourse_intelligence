from pathlib import Path
import json
from classroom_discourse_intelligence.synthetic import make_transcript
from classroom_discourse_intelligence.core import annotate,discourse_summary
root=Path(__file__).resolve().parents[1]; (root/'results').mkdir(exist_ok=True)
d=make_transcript(); a=annotate(d); a.to_csv(root/'results'/'synthetic_transcript_annotated.csv',index=False); m={k:round(v,3) for k,v in discourse_summary(d).items()}; (root/'results'/'demo_metrics.json').write_text(json.dumps(m,indent=2)); print(json.dumps(m,indent=2))
