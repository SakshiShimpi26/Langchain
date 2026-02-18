# PyPDFLoader

# PyPDFLoader is a document loader in LangChain used to load content from PDF files and convert 
# each page into a Document object.

# This loader creates a separate Document for each page in the PDF.

# [
#     Document(page_content="Text from page 1", metadata={"page": 0, "source": "file.pdf"}),
#     Document(page_content="Text from page 2", metadata={"page": 1, "source": "file.pdf"}),
#     ...
# ]


# Limitations:
# It uses the PyPDF library under the hood — not great with scanned PDFs or complex layouts.

from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("n8n.pdf")

docs = loader.load()

print("No of documents available:",len(docs))

print(docs[2].page_content)
print(docs[2].metadata)