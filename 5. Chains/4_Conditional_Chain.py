# Chain Flow
#             Review
#               |
#              LLM
#     ----------------------
#     |                    |
# Positive              Negative
#     |                    |
#   Model                Model
#     |                    |
# Generate a           Generate a 
# Positive Message    Negative Message

# Here, either a Positive Chain will get executed or Negative Chain will get executed

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.output_parsers import PydanticOutputParser
from langchain.schema.runnable import RunnableBranch, RunnableLambda
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro") 

class Review(BaseModel):
    sentiment: Literal['Positive', 'Negative'] = Field(description="Give me sentiment of the review")

parser = StrOutputParser()
parser2 = PydanticOutputParser(pydantic_object=Review)

prompt1 = PromptTemplate(
    template="Classify the Sentiment of Following review into Positive or Negative \n {review} \n {format_instruction}",
    input_variables=['review'],
    partial_variables={'format_instruction': parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

# classifier_result = classifier_chain.invoke({'review':"This is a wonderful smartphone"}).sentiment

# print("Classifier Result", classifier_result)

prompt2 = PromptTemplate(
    template="Write an appropriate 2 line message for the Positive review \n {review}",
    input_variables=['review']
)

prompt3 = PromptTemplate(
    template="Write an appropriate 2 line message for the Negative review \n {review}",
    input_variables=['review']
)

branch_chain = RunnableBranch(
    (lambda x: x.sentiment == "Positive", prompt2 | model | parser),
    (lambda x: x.sentiment == "Negative", prompt3 | model | parser),
    RunnableLambda(lambda x: "Could not Find any Sentiment")
)

chain = classifier_chain | branch_chain

print(chain.invoke({'review':"This is a terrible Laptop"}))