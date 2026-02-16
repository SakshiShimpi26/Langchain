# StructuredOutputParser

# StructuredOutputParser is an output parser in LangChain that helps extract structured JSON data from LLM responses based on predefined field schemas.

# It works by defining a list of fields (ResponseSchema) that the model should return, ensuring the output follows a structured format.

from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

load_dotenv()

model = ChatGroq(model="llama-3.1-8b-instant")

schema = [
    ResponseSchema(name='Point 1', description='Fact 1 about the topic'),
    ResponseSchema(name='Point 2', description='Fact 2 about the topic'),
    ResponseSchema(name='Point 3', description='Fact 3 about the topic'),
]

parser = StructuredOutputParser.from_response_schemas(schema)

template = PromptTemplate(
    template='Give 3 fact points about {topic} \n {format_instruction}',
    input_variables=['topic'],
    partial_variables={'format_instruction':parser.get_format_instructions()}
)

chain = template | model | parser

result = chain.invoke({'topic':'black hole'})

print(result)