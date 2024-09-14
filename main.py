from llms.llmOpenAI import LLMOpenAI
openai = LLMOpenAI()
from utils.template import Template

history = []

while True:
    user = input("USER: ")
    history.append({"role": "USER", "content": user})
    response = openai.chat(history)
    print("AI: " + response)
    history.append({"role": "AI", "content": response})

# docs = [{"doc":"https://www.google.com/search?q=capital+of+france"},
#         {"doc":"https://en.wikipedia.org/wiki/Paris"},
#         {"doc":"https://en.wikipedia.org/wiki/France"}]

template = Template("""
{messages}[{role}: {content}\n]
THESE {type} CAN HELP YOU:
{docs}[{doc}\n]
""")

template.fill(messages=history, docs=docs, type="LINKS")

