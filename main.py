from routerOpenAI import RouterOpenAI
openai = RouterOpenAI()

from template import Template
template = Template(
    """Are there any terms I should be aware of before signing there these terms of service? 
    
    TERMS OF SERVICE
    {tos}""")

with open("youtube.txt", "r", encoding="utf-8") as file:
    youtube = file.read()

prompt = template.fill(tos=youtube)
print(openai.complete("chatgpt-4o-latest", prompt))