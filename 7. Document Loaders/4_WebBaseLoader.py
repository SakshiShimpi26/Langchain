# WebBaseLoader:

# It is used to extract Text content from the Web pages (URL)
# It used BeautifulSoup under the hood to parse the HTML and extract visible Text.
# Also if we load only single URL then in docs only 1 document will get created, if we add multiple URLs 
# the multiple documents will get created. 

# When to Use::
#   -> For blogs, news articles, or public websites where the content is primarily text-based and static.

# Limitations::
#   -> Does not handle Javascript- heavy pages well(use SeleniumURLLoader for that)
#   -> Loads only static content (what's in the HTML, not what loads after the page render)

from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

# Load URL data using WebBaseLoader
url = "https://docs.coderabbit.ai/getting-started/quickstart"
loader = WebBaseLoader(url)
docs = loader.load()
# print(docs)

prompt = PromptTemplate(
    template="Answer the following question {question} from the following text \n {text}",
    input_variables=["question","text"]
)

model = ChatGoogleGenerativeAI(model="gemini-2.5-pro") 

parser = StrOutputParser()

chain = prompt | model | parser

print(chain.invoke({"question":"How to add CodeRabbit to your repository ?. Provide me with the steps","text":docs[0].page_content}))
