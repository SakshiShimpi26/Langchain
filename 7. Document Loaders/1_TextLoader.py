from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

loader = TextLoader('black_hole.txt', encoding="utf-8")

docs = loader.load()

print(docs)

# The type of docs is always a list 
# Hence we can access individual documents using docs[0], docs[1]
print("Type of docs:",type(docs))

# Every docs consists of two main parameters 
# 1. page_content -> consists of actual data that is present in the Text File
# 2. metadata -> consists of file information like File name, last modified, source , etc 

print("Page_content",docs[0].page_content)
print("Metadata:",docs[0].metadata)

load_dotenv()

prompt = PromptTemplate(
    template="Generate 5 line poem on {topic}",
    input_variables=["topic"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro") 

parser = StrOutputParser()

chain = prompt | model | parser

print("=========== POEM =============")
print(chain.invoke({'topic':docs[0].page_content}))