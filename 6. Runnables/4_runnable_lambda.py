# RunnableLambda

# RunnableLambda is a runnable primitive that allows you to apply custom Python functions within an AI pipeline.
# It acts as a middleware between different AI components, enabling preprocessing, transformation, API calls, 
# filtering, and post-processing in a LangChain workflow.

#                         RunnablePassthrough (print joke as it is) -> Print Output
#                        /
# Prompt -> LLM -> Joke -
#                        \
#                         RunnableLambda (count number of words in Joke) -> Print Output

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")  

prompt1 = PromptTemplate(
    template="Write a joke for me on the following topic \n {topic}",
    input_variables=['topic']
)

parser = StrOutputParser()

def word_count(text):
    x = text.split()
    return len(x)

joke_generation_chain = RunnableSequence(prompt1, model, parser)

parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(word_count)
})

chain = RunnableSequence(joke_generation_chain,parallel_chain)

print(chain.invoke({'topic':'AI'}))