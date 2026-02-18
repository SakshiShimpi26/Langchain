from langchain_experimental.text_splitters import SemanticChunker
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv
import os

# Load .env file (must contain GOOGLE_API_KEY)
load_dotenv()

# Initialize Gemini embeddings
embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")

# Initialize Semantic Chunker
text_splitter = SemanticChunker(
    embeddings,
    breakpoint_threshold_type="standard_deviation",
    breakpoint_threshold_amount=1
)

# Sample text
sample = """
Farmers were working hard in the fields, preparing the soil and planting seeds for the next season.
The sun was bright, and the air smelled of earth and fresh grass.
The Indian Premier League (IPL) is the biggest cricket league in the world.
People all over the world watch the matches and cheer for their favorite teams.

Terriorism is a big danger to peace and safety. It causes harm to peopleand creates fear in cities and villages.
When such attacks happens they leave behind pain and sadness.
To fight terriorism we need to have strong laws, alert security forces and support from peoples who cares about peace and safetly.
"""

# Split text semantically using Gemini
chunks = text_splitter.split_text(sample)

# Print the semantic chunks
for i, chunk in enumerate(chunks, start=1):
    print(f"\n--- Chunk {i} ---\n{chunk}")
