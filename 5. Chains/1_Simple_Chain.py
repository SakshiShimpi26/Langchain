# Chain Flow 
# Prompt -> LLM -> Output

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")  

# Output parser
parser = StrOutputParser()

# Chain setup
chain = prompt | model | parser

# Run chain
result = chain.invoke({"topic": "cricket"})
print(result)

chain.get_graph().print_ascii()