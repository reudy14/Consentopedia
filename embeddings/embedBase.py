from abc import abstractmethod

class EmbedBase():
    """for creating embeddings of files"""
    def __init__(self, model):
        self.model = model
        
    @abstractmethod
    def embed(self, text):
        pass