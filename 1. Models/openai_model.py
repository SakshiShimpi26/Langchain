from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Initialize OpenAI Chat Model
model = ChatOpenAI(model="gpt-5") 

# Send a simple query
result = model.invoke("What is the capital of India?")

# Print results
print(result)
print(result.content)
