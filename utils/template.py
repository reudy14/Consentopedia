import re

ARRAY_REGEX = re.compile(r'\{(\w+)\}\[(.*?)\]', re.DOTALL)
class Template():
    """
allows to make consise templates for strings
example:
    
history = [{"role": "SYSTEM", "content": "You are a helpful assistant that responds to user questions"},
           {"role": "USER", "content": "What is the capital of France?"} ]

docs = [{"doc":"https://www.google.com/search?q=capital+of+france"},
        {"doc":"https://en.wikipedia.org/wiki/Paris"},
        {"doc":"https://en.wikipedia.org/wiki/France"}]

template = Template(\"""
{messages}[{role}: {content}\n]
THESE {type} CAN HELP YOU:
{docs}[{doc}\n]
\""")

template.fill(messages=history, docs=docs, type="LINKS")

SYSTEM: You are a helpful assistant that responds to user questions
USER: What is the capital of France?

THESE LINKS CAN HELP YOU:
https://www.google.com/search?q=capital+of+france
https://en.wikipedia.org/wiki/Paris
https://en.wikipedia.org/wiki/France
    """
    def __init__(self, template):
        self.template = template
        
    def fill(self, **kwargs):
        prompt = self.template
        for match in ARRAY_REGEX.findall(prompt):
            array_key, array_template = match
            array_prompt = ""
            if array_key not in kwargs:
                continue
            for array_value in kwargs[array_key]:
                copy = array_template
                for key in array_value:
                    copy = copy.replace(f'{{{key}}}', array_value[key])
                array_prompt += copy
            prompt = prompt.replace(f'{{{array_key}}}[{array_template}]', array_prompt)
        for key in kwargs:
            if not isinstance(kwargs[key], list):
                prompt = prompt.replace(f'{{{key}}}', kwargs[key])
        return prompt