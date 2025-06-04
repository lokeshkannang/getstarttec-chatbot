# # pip install google-genai

# import os
# from google import genai
# from google.genai import types

# # Initialize the Gemini Client
# client = genai.Client(api_key="AIzaSyDJzMMz-ji77C0E8H6dJEMo6kOWwnxYuls")

# model_name = "gemini-1.5-flash"
# chat_history = []

# # System instruction: Set chatbot behavior
# system_instruction = types.Content(
#     role="user",
#     parts=[
#         types.Part.from_text(text="You are a Kubernetes expert. Only answer Kubernetes-related questions. If asked something else, politely redirect the user.")
#     ],
# )
# chat_history.append(system_instruction)

# # Generate Content Function
# def ask_gemini(question):
#     chat_history.append(
#         types.Content(role="user", parts=[types.Part.from_text(text=question)])
#     )

#     config = types.GenerateContentConfig(response_mime_type="text/plain")

#     response_text = ""
#     for chunk in client.models.generate_content_stream(
#         model=model_name,
#         contents=chat_history,
#         config=config,
#     ):
#         if hasattr(chunk, "text") and chunk.text:
#             print(chunk.text, end="", flush=True)
#             response_text += chunk.text

#     print()  # new line after response
#     chat_history.append(
                        
#         types.Content(role="model", parts=[types.Part.from_text(text=response_text)])
#     )

# # Chat Loop
# def start_chat():
#     print("🤖 Gemini Kubernetes Chatbot (type 'exit' to quit)\n")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ["exit", "quit"]:
#             print("👋 Goodbye!")
#             break
#         ask_gemini(user_input)

# if __name__ == "__main__":
#     start_chat()

# pip install google-genai fastapi uvicorn

import os
from google import genai
from google.genai import types


# Initialize the Gemini Client
client = genai.Client(api_key="AIzaSyDJzMMz-ji77C0E8H6dJEMo6kOWwnxYuls")

model_name = "gemini-1.5-flash"
chat_history = []

# System instruction: Set chatbot behavior
system_instruction = types.Content(
    role="user",
    parts=[
        types.Part.from_text(
            text="You are a Kubernetes expert. Only answer Kubernetes-related questions. If asked something else, politely redirect the user. max 20 words"
        )
    ],
)
chat_history.append(system_instruction)

# Generate Content Function
def ask_gemini(question):
    chat_history.append(
        types.Content(role="user", parts=[types.Part.from_text(text=question)])
    )

    config = types.GenerateContentConfig(response_mime_type="text/plain")

    response_text = ""
    for chunk in client.models.generate_content_stream(
        model=model_name,
        contents=chat_history,
        config=config,
    ):
        if hasattr(chunk, "text") and chunk.text:
            print(chunk.text, end="", flush=True)
            response_text += chunk.text

    print()  # new line after response
    chat_history.append(
        types.Content(role="model", parts=[types.Part.from_text(text=response_text)])
    )

    return response_text  # ✅ For FastAPI response


# Chat Loop
def start_chat():
    print("🤖 Gemini Kubernetes Chatbot (type 'exit' to quit)\n")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("👋 Goodbye!")
            break
        ask_gemini(user_input)


# 🧩 FastAPI Setup (Only runs if 'fastapi' arg is passed)
from fastapi import FastAPI
from pydantic import BaseModel
import uvicorn

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str

@app.post("/ask")
async def ask_question(data: QuestionRequest):
    response = ask_gemini(data.question)
    return {"response": response}


# 🚀 Run either CLI chat or FastAPI based on command line
if __name__ == "__main__":
    import sys
    if "fastapi" in sys.argv:
        uvicorn.run("app:app", host="127.0.0.1", port=8000, reload=True)
    else:
        start_chat()
