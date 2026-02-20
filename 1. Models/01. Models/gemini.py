from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-2.5-pro')

query = input("Enter the prompt:\n")

result = model.invoke(query)

print(result)

print(result.content)
