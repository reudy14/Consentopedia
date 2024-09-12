from abc import ABC, abstractmethod

class RouterBase(ABC):
    def __init__(self, apikey, url=""):
        self.apikey = apikey
        self.url = url
        
    @abstractmethod
    def complete(self, model, messages):
        pass
    
    @abstractmethod
    def chat(self, messages):
        pass