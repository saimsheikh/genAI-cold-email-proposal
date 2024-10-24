from langchain_groq import ChatGroq
import os

llm = ChatGroq(
    model="llama-3.1-70b-versatile",
    temperature=0,
    groq_api_key= os.getenv('groq_api_key')
)


response = llm.invoke("the first person to land on moon was ...")

print(response)