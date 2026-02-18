# CSVLoader

# CSVLoader is a document loader in LangChain that helps you read data from a CSV file 
# (Comma-Separated Values) and convert each row into a Document object.
# Each row of your CSV becomes one document.

# The content of the document is usually the values in the row.

# The metadata (extra info) can include things like column names, file path, row number, etc.

# This is super useful when you want to take data from spreadsheets or tabular formats and make it searchable or usable in an LLM-powered app (like Q&A on CSV data).

from langchain_community.document_loaders import CSVLoader

loader = CSVLoader(file_path="employees_20.csv")

docs = loader.load()

print(len(docs))

print(docs)

print("Data for Document 3") # follows 0 indexing hence 4th row in actual sheet
print(docs[3].page_content)
print(docs[3].metadata)
