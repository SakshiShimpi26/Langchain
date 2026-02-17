# RunnableSequence

# RunnableSequence is a sequential chain of runnables in LangChain that executes each step one 
# after another, passing the output of one step as the input to the next.

# It is useful when you need to compose multiple runnables together in a structured workflow.

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")  

prompt = PromptTemplate(
    template="Write a joke for me on the following topic \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the joke in 3-4 sentences \n {joke}",
    input_variables=['joke']
)

parser = StrOutputParser()

chain = RunnableSequence(prompt,model,parser,prompt2,model,parser)

print(chain.invoke({'topic':"AI"}))