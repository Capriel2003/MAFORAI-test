from openai import OpenAI

class AstronomerCopilot:
    def __init__(self, base_url="http://localhost:1234/v1"):
        # Connects to Local LLM (LM Studio)
        self.client = OpenAI(base_url=base_url, api_key="lm-studio")

    def analyze(self, row):
        """Sends data to LLM. Returns None if connection fails."""
        prompt = f"""
        Analyze this astronomical transient:
        ID: {row['obj_id']} | Redshift: {row['redshift']}
        Class: {row['classification']} (Prob: {row['probability']})
        Rise Rate: {row['rise_rate']}
        Comments: {row['comments']}

        Task: Summarize physics, explain classification reasoning, and suggest observations.
        """
        
        try:
            response = self.client.chat.completions.create(
                model="local-model",
                messages=[{"role": "user", "content": prompt}],
                temperature=0.7
            )
            return response.choices[0].message.content
        except Exception as e:
            return f"Error: LLM unreachable. Check if LM Studio server is running. ({e})"