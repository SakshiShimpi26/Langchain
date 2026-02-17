# RunnableParallel

# RunnableParallel is a runnable primitive that allows multiple runnables to execute in parallel.

# Each runnable receives the same input and processes it independently, producing a dictionary of outputs.

# Chain Flow
#         Tweet
#       /      \
#   Topic        -> Combine this both and show to user
#       \      /
#       LinkedIN Post

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel,RunnableSequence

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")  

prompt1 = PromptTemplate(
    template="Generate a tweet on provided text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate a 5-6 lines LinkedIN post on the provided text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

paraller_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1 | model | parser),
    'LinkedIN': RunnableSequence(prompt2 | model | parser)
})

result = paraller_chain.invoke({'text': "Generative AI"})

print(result['tweet'])
print("===============")
print(result['LinkedIN'])