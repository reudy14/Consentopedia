from llms.llmBase import LLMBase
from openai import OpenAI as Client
from secrets import OPENAI_API_KEY

class LLMOpenAI(LLMBase):
    def __init__(self):
        LLMBase.__init__(self, OPENAI_API_KEY)
        self.api = Client(api_key=self.apikey)
        
    def complete(self, prompt, model="chatgpt-4o-latest"):
        response = self.api.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content