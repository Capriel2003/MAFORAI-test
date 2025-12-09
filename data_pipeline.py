import json
import pandas as pd

def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    processed = []
    for obj in data:
        # Get latest photostats safely
        stats = obj.get('photstats', [{}])[-1] if obj.get('photstats') else {}
        
        # Get best classification
        classes = obj.get('classifications', [])
        best_cls = sorted(classes, key=lambda x: x.get('probability', 0), reverse=True)[0] if classes else {}
        
        # Extract comments
        comments = " | ".join([c.get('text', '') for c in obj.get('comments', []) if c.get('text')])

        processed.append({
            'obj_id': obj.get('obj_id') or obj.get('id'),
            'ra': obj.get('ra'),
            'dec': obj.get('dec'),
            'redshift': obj.get('redshift'),
            'rise_rate': stats.get('rise_rate', 0),
            'comments': comments,
            'classification': best_cls.get('classification', 'Unknown'),
            'probability': best_cls.get('probability', 0)
        })

    return pd.DataFrame(processed)