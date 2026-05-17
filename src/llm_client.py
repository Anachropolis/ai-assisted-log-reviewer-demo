import os
from openai import OpenAI
from dotenv import load_dotenv


load_dotenv()



class LLMClient:

    def __init__(self) -> None:
        self.api_key = os.getenv("OPENAI_API_KEY")
        self.client = OpenAI(api_key = self.api_key)
        self.model = os.getenv("OPENAI_MODEL")


    def query_model(self, system_prompt: str, user_prompt: str) -> str:
        """generate json response from system + user prompt"""
        response = self.client.chat.completions.create(
            model = self.model,
            messages = [{"role": "system",
                      "content": system_prompt},
                     {"role": "user",
                      "content": user_prompt}])
        return response.choices[0].message.content







