from routerBase import RouterBase
from openai import OpenAI as Client
from secrets import OPENAI_API_KEY

class RouterOpenAI(RouterBase):
    def __init__(self):
        RouterBase.__init__(self, OPENAI_API_KEY)
        self.api = Client(api_key=self.apikey)
        
    def complete(self, model, prompt):
        response = self.api.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}]
        )
        return response.choices[0].message.content
    
    def chat():
        raise NotImplementedError("Method not implemented")