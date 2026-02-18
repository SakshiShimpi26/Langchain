# DirectoryLoader

# DirectoryLoader is a document loader that lets you load multiple documents from a directory (folder) of files.

# Glob Pattern	What It Loads
#  **/*.txt	      --> All .txt files in all subfolders
#  *.pdf	      --> All .pdf files in the root directory
#  data/*.csv     --> All .csv files in the data/ folder
#  **/*	          --> All files (any type, all folders)
#  **             --> recursive search through subfolders

# ============================================================================================
# Disadvantages of DirectoryLoader

# Performance Issues:
# If the directory contains a very large number of files, loading them all at once can be slow 
# and memory intensive.

# Lack of Fine-Grained Control:
# DirectoryLoader works on glob patterns but does not give advanced filtering options 
# (e.g., load only specific metadata conditions or file sizes).

# Mixed File Types Handling:
# If the directory has many different file formats, you need to ensure proper loaders for each 
# type. Otherwise, some files may not be processed correctly.

# Recursive Search Overhead:
# Using **/* for recursive searches may unintentionally load irrelevant or temporary files 
# (like system files, cache, or backup files), which can clutter the document set.

# No Automatic Deduplication:
# If duplicate or similar files exist in the directory, they’ll all be loaded as separate 
# documents, leading to redundancy in the dataset.

from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path="Files",
    glob="*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(docs)

print(len(docs[3].page_content))
print(len(docs[3].metadata))

# ✅ load()
# Eager Loading (loads everything at once).
# Returns: A list of Document objects.
# Loads all documents immediately into memory.
# Best when:
#    --> The number of documents is small.
#    --> You want everything loaded upfront.

# 🔄 lazy_load()
# Lazy Loading (loads on demand).
# Returns: A generator of Document objects.
# Documents are not all loaded at once; they’re fetched one at a time as needed.
# Best when:
#    --> You’re dealing with large documents or lots of files.
#    --> You want to stream processing (e.g., chunking, embedding) without using lots of memory.

docs = loader.lazy_load()

for document in docs:
    print(document.metadata)