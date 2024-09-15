from abc import ABC, abstractmethod
from utils.template import Template

class LLMBase(ABC):
    """for communicating with llms and all of their functions"""
    def __init__(self, url=""):
        self.url = url
        
    @abstractmethod
    def complete(self, messages, model):
        pass
    
    def chat(self, history):
        prompt = [f"{message['role']}: {message['content']}" for message in history]
        prompt = "\n".join(prompt)
        prompt += "\nAI: "
        response = self.complete(prompt)
        return response
    
    def chat_with_docs(self, history, docs):
        template = Template("""{messages}[{role}: {content}\n]""")
        template = template.fill(role="AI", content=docs)
        return 