from llms.llmBase import LLMBase
from openai import OpenAI as Client

class LLMOpenAI(LLMBase):
    def __init__(self):
        LLMBase.__init__(self)
        self.client = Client()
        
    def complete(self, prompt, model="chatgpt-4o-latest"):
        response = self.client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content