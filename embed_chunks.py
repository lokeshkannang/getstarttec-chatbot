from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import GoogleGenerativeAIEmbeddings
import chromadb
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# Load site content
with open("site_content.txt", "r", encoding="utf-8") as f:
    text = f.read()

splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
chunks = splitter.split_text(text)

embedding = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)

chroma_client = chromadb.Client()
collection = chroma_client.create_collection(name="site_content")

for i, chunk in enumerate(chunks):
    collection.add(documents=[chunk], ids=[f"chunk_{i}"], embeddings=[embedding.embed_query(chunk)])
