# RunnablePassthrough

# RunnablePassthrough is a special Runnable primitive that simply returns the input as output without 
# modifying it.

#                                             RunnablePassthrough (print joke as it is)
#                                           /
# prompt to generate joke -> LLM -> Parser -
#                                           \
#                                             Prompt2 -> LLM -> Output (explain joke)

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")  

prompt1 = PromptTemplate(
    template="Write a joke for me on the following topic \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Explain the joke in 3-4 sentences \n {joke}",
    input_variables=['joke']
)

parser = StrOutputParser()

joke_generation_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'explanation':RunnableSequence(prompt2, model, parser)
})

chain = RunnableSequence(joke_generation_chain,parallel_chain)

print(chain.invoke({'topic':'AI'}))