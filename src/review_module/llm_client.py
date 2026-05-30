import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()



class LLMClient:

    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY")

        if not self.api_key:
            raise ValueError("OPENAI_API_KEY is not set. Add to .env file")

        self.client = OpenAI()
        self.model = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")


    def query_model(self, system_prompt: str, user_prompt: str) -> str:
        """Generate JSON response from system + user prompt"""
        response = self.client.chat.completions.create(
            model = self.model,
            messages = [{"role": "system","content": system_prompt}, {"role": "user","content": user_prompt}],
            temperature = 0)

        return response.choices[0].message.content







