# Chain Flow
#         Notes
#       /      \
#   Data         Combine this both and show to user
#       \      /
#         Quiz

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.schema.runnable import RunnableParallel

load_dotenv()

model1 = ChatGoogleGenerativeAI(model="gemini-2.5-pro")  

model2 = ChatGoogleGenerativeAI(model="gemini-1.5-flash") 

prompt1 = PromptTemplate(
    template="Generate short and simple notes on provided text \n {text}",
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template="Generate a 5 question quiz with question and answer on the provided text \n {text}",
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template="Merge the provided notes and quiz into a single document \n notes -> {notes} \n quiz -> {quiz}",
    input_variables=['notes','quiz']
)

parser = StrOutputParser()

paraller_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser,
    'quiz': prompt2 | model2 | parser
})

merge_chain = prompt3 | model1 | parser

final_chain = paraller_chain | merge_chain

info = """Generative AI (Gen AI) is a branch of artificial intelligence that focuses on creating new content—such as text, images, audio, video, or even code—rather than just analyzing or classifying existing data. It uses advanced machine learning models, especially large language models (LLMs) and diffusion models, that are trained on massive datasets to recognize patterns, structures, and relationships in data. Once trained, these models can generate outputs that look remarkably similar to human-created work. For example, Gen AI can write articles, summarize documents, create art, compose music, or even generate software code based on natural language instructions.

What makes Gen AI powerful is its ability to adapt and respond to user prompts in a contextual and creative way. Instead of following rigid rules, it leverages probability and deep learning to predict what comes next in a sequence (like the next word in a sentence or the next pixel in an image). This flexibility allows it to assist in tasks ranging from business automation and content creation to personalized education and research support. Essentially, Gen AI doesn’t just process information—it actively produces new information, making it a transformative technology across industries."""

result = final_chain.invoke({'topic': info})

print(result)

final_chain.get_graph().print_ascii()