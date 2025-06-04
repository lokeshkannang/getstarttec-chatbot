import google.generativeai as genai
from langchain.embeddings import GoogleGenerativeAIEmbeddings
import chromadb
import os
from dotenv import load_dotenv

# ✅ Step 1: Load API Key from .env
load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")

# ✅ Step 2: Configure Gemini model
genai.configure(api_key=api_key)
model = genai.GenerativeModel("gemini-1.5-flash")

# ✅ Step 3: Setup Embeddings
embedding = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=api_key  # 🔒 Use env key here, not hardcoded
)

# ✅ Step 4: Load Chroma Vector DB
chroma_client = chromadb.Client()
collection = chroma_client.get_collection("site_content")

# ✅ Step 5: Create Chat Function
def chat_with_website(question):
    # Get embedding of user question
    q_embedding = embedding.embed_query(question)
    
    # Query Chroma DB
    result = collection.query(query_embeddings=[q_embedding], n_results=3)
    context_chunks = result['documents'][0]
    context = "\n".join(context_chunks)
    
    # Ask Gemini with context
    response = model.generate_content(f"""
    You are a chatbot for a website. Answer the user's question based only on the context below.

    --- Website Content ---
    {context}

    --- Question ---
    {question}
    """)
    
    return response.text
