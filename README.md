<p align="center">
  <img src="https://readme-typing-svg.herokuapp.com?size=28&duration=3000&color=F75C7E&center=true&vCenter=true&width=900&lines=Production-Grade+LangChain+System+Architecture;LLM+Pipelines+%7C+RAG+%7C+Vector+Search+%7C+Tool+Execution;Modular+Design+of+Composable+LLM+Infrastructure" />
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/LangChain-Core-orange?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-OpenAI_+_Gemini-black?style=for-the-badge" />
  <img src="https://img.shields.io/badge/VectorDB-Chroma_+_Pinecone-purple?style=for-the-badge" />
  <img src="https://img.shields.io/badge/RAG-Implemented-success?style=for-the-badge" />
</p>

---

# 🧠 Overview

This repository demonstrates a **production-grade modular implementation of LangChain architecture**, covering:

- Multi-provider LLM integration  
- Prompt engineering & structured parsing  
- LCEL runnable pipelines  
- Retrieval-Augmented Generation (RAG)  
- Vector storage & semantic search  
- Tool-augmented LLM workflows  

Each component is implemented independently to deeply understand system behavior before integrating into full-scale LLM pipelines.

---

# 🎯 Why This Project

Modern LLM applications require more than just model calls.  
They require:

- Retrieval-grounded reasoning  
- Deterministic schema validation  
- Composable execution graphs  
- Tool-driven decision-making  
- Multi-model abstraction  

This project demonstrates **system-level understanding of scalable LLM infrastructure design.**

---

# ⚙️ System Architecture

## 🟢 Standard LLM Pipeline

```
User Input
    ↓
Prompt Template
    ↓
Chat Model (OpenAI / Gemini)
    ↓
Output Parser
    ↓
Structured Response
```

---

## 🔵 Retrieval-Augmented Generation (RAG)

```
User Query
     ↓
Text Splitter
     ↓
Embeddings
     ↓
Vector Store (Chroma / Pinecone)
     ↓
Retriever
     ↓
LLM + Retrieved Context
     ↓
Grounded Output
```

---

# 🧩 Core Implementation Components

## 🔹 1. Models

- OpenAI Chat Model integration  
- Gemini model integration  
- Provider-based configuration  
- Temperature & invocation control  
- Multi-provider abstraction layer  

---

## 🔹 2. Prompts

- PromptTemplate  
- ChatPromptTemplate  
- Message objects  
- MessagePlaceholder  
- JSON-based templates  
- Chat history handling  
- Dynamic prompt utilities  

---

## 🔹 3. Structured Output

- TypedDict schema parsing  
- Pydantic validation  
- JSON schema enforcement  
- Deterministic output guarantees  

---

## 🔹 4. Output Parsers

- StrOutputParser  
- JSONOutputParser  
- StructuredOutputParser  
- PydanticOutputParser  

---

## 🔹 5. Chains

- Simple Chain  
- Sequential Chain  
- Parallel Chain  
- Conditional Chain  

---

## 🔹 6. Runnables (LCEL)

- RunnableSequence  
- RunnableParallel  
- RunnablePassthrough  
- RunnableLambda  
- RunnableBranch  

### Composable Pattern

```python
chain = prompt | model | parser
response = chain.invoke({"input": "example"})
```

LCEL enables clean functional composition and scalable pipeline construction.

---

## 🔹 7. Document Loaders

- TextLoader  
- PyPDFLoader  
- DirectoryLoader  
- WebBaseLoader  
- CSVLoader  

Supports ingestion of structured and unstructured external data sources.

---

## 🔹 8. Text Splitters

- Character-based splitter  
- RecursiveCharacterTextSplitter  
- Token-aware chunking  

Optimized for embedding efficiency and retrieval quality.

---

## 🔹 9. Vector Stores

- ChromaDB integration  
- Pinecone integration  
- Embedding persistence  
- Similarity search  

---

## 🔹 10. Retrievers

- VectorStore → Retriever conversion  
- Similarity-based context fetching  
- RAG experimentation notebook  

---

## 🔹 11. Tools

- Built-in tool usage  
- Custom tool creation  
- Tool calling integration  
- Tool-driven reasoning workflows  

---

# 🧪 Example Use Cases

- 📄 Document-based RAG chatbot  
- 🔎 Semantic search over PDFs  
- 🧾 Structured information extraction  
- 🤖 Tool-enabled research assistant  
- 🧠 Multi-step reasoning pipelines  

---

# 🔬 Technical Highlights

- Multi-provider LLM abstraction  
- Schema-constrained generation  
- Deterministic output validation  
- Retrieval-grounded reasoning  
- LCEL functional composition  
- Modular system isolation  
- Tool-enabled execution patterns  

---

# 📂 Repository Structure

```
Langchain/
│
├── models/
├── prompts/
├── output_parsers/
├── structured_output/
├── chains/
├── runnables/
├── document_loaders/
├── text_splitters/
├── vector_stores/
├── retrievers/
├── tools/
└── notebooks/
```

---

# 🚀 Installation

```bash
git clone https://github.com/your-username/Langchain.git
cd Langchain
pip install -r requirements.txt
```

### Environment Variables

```
OPENAI_API_KEY=
GOOGLE_API_KEY=
PINECONE_API_KEY=
```

---

# 📊 Architectural Emphasis

✔ Modular component isolation  
✔ Explicit separation of prompt, model, parser  
✔ Composable runnable pipelines  
✔ Retrieval-grounded generation  
✔ Schema-constrained outputs  
✔ Tool-driven execution patterns  

---

# 📌 Future Enhancements

- LangGraph integration  
- Streaming responses  
- Agent memory systems  
- Evaluation & benchmarking layer  
- Production deployment setup  

---

# 👩‍💻 Author

Built to demonstrate deep understanding of modern LLM application architecture and scalable AI system design.

---
