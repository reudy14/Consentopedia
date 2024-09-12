class Template():
    def __init__(self, template):
        self.template = template
        
    def fill(self, **kwargs):
        prompt = self.template
        for key in kwargs:
            prompt = prompt.replace(f'{{{key}}}', kwargs[key])
        return prompt