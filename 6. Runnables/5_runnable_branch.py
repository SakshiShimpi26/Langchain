# RunnableBranch

# RunnableBranch is a control flow component in LangChain that allows you to conditionally route input data 
# to different chains or runnables based on custom logic.

# It functions like an if/elif/else block for chains — where you define a set of condition functions, each 
# associated with a runnable (e.g., LLM call, prompt chain, or tool). The first matching condition is executed. 
# If no condition matches, a default runnable is used (if provided).

#                                                          If >300 Words -> LLM -> Summarize It -> Print
#                                                         /
# Take Topic from User -> Prompt -> LLM - Analyze Response
#                                                         \ 
#                                                          If <300 Words -> Simply Print

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableSequence, RunnableParallel, RunnablePassthrough, RunnableLambda, RunnableBranch

load_dotenv()

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro")  

prompt1 = PromptTemplate(
    template="Write a report on the mentioned topic \n {topic}",
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template="Summarize the following text \n {text}",
    input_variables=['text']
)

parser = StrOutputParser()

generate_topic_details = RunnableSequence(prompt1,model,parser)

branch_chain = RunnableBranch(
    (lambda x: len(x.split()) >= 500, RunnableSequence(prompt2 | model | parser)),
    (lambda x: len(x.split()) <=500, RunnablePassthrough()), 
    RunnableLambda(lambda x: "Thank You!")
)

final_chain = RunnableSequence(generate_topic_details,branch_chain)

print(final_chain.invoke({'AI'}))