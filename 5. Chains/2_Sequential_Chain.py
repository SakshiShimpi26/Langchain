# Chain Flow
# Topic -> LLM -> Detailed Report -> LLM -> 5 Line Summary

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

prompt1 = PromptTemplate(
    template="Generate 5 interesting facts about {topic}",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template="Provide me with 5 important points from the {text}",
    input_variables=["text"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")  

# Output parser
parser = StrOutputParser()

# Chain setup
chain = prompt1 | model | parser | prompt2 | model | parser

# Run chain
result = chain.invoke({"topic": "Black Hole"})
print(result)

chain.get_graph().print_ascii()