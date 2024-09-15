from openai import OpenAI as Client

class EmbedOpenAI:
    def __init__(self, model):
        self.model = model
        self.client = Client()
        
    def embed(self, text):
        return self.client.embeddings.create(input=[text], model=self.model).data[0].embedding