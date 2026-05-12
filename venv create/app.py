print("Hello")
from longchain.llm import Ollama

Ollama = Ollama (base_url='https://localhost:11434', model='Gemma 2')
print(ollama('why is the sky blue'))
