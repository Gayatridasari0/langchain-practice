from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant", temperature=1.5)

result = model.invoke("Write a 5 line poem on cricket")

print(result.content)