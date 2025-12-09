import pandas as pd
from data_pipeline import load_data
from intelligent_agent import AstronomerCopilot

def main():
    # 1. Load Data
    print("Loading data...")
    df = load_data('sources_sample.json')
    
    # 2. Init Agent
    agent = AstronomerCopilot()

    # 3. Analyze Sample (Top 3 interesting objects)
    results = []
    sample = df[df['comments'] != ""].head(3) # Prefer objects with comments

    print(f"Analyzing {len(sample)} objects with Local LLM...")
    
    for _, row in sample.iterrows():
        print(f" -> Processing {row['obj_id']}...")
        analysis = agent.analyze(row)
        
        results.append({
            'obj_id': row['obj_id'],
            'analysis': analysis
        })

    # 4. Save
    pd.DataFrame(results).to_csv('copilot_results.csv', index=False)
    print("Done. Saved to 'copilot_results.csv'.")

if __name__ == "__main__":
    main()