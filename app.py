from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_pinecone import PineconeVectorStore
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os
import subprocess
import json

app = Flask(__name__)

load_dotenv()

PINECONE_API_KEY = os.environ.get("PINECONE_API_KEY")

os.environ["PINECONE_API_KEY"] = PINECONE_API_KEY

from langchain_pinecone import PineconeVectorStore
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

# Load the embeddings
embeddings = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')

# Load the Pinecone vector store
index_name = "chatbot"
docsearch = PineconeVectorStore.from_existing_index(
    index_name=index_name,
    embedding=embeddings
)

# Create the retriever
retriever = docsearch.as_retriever(search_type="similarity", search_kwargs={"k": 3})

from src.prompt import system_prompt

# Define the retrieval chain
def create_ollama_retrieval_chain(retriever, context_template):
    def retrieval_chain(input_query):
        # Retrieve relevant documents
        retrieved_docs = retriever.invoke(input_query)
        context = "\n".join([doc.page_content for doc in retrieved_docs])

        # Query Ollama with the context and input query
        response = query_ollama(input_query, context=context_template.format(context=context))
        return response

    return retrieval_chain

# Initialize the rag_chain
rag_chain = create_ollama_retrieval_chain(retriever, context_template=system_prompt)

import subprocess
import json

def query_ollama(prompt, context="", model="gemma3:12b"):
    """Query the Ollama CLI with a prompt and context."""
    command = ["ollama", "run", model]
    input_data = {"messages": [
        {"role": "system", "content": context},
        {"role": "user", "content": prompt}
    ]}
    process = subprocess.run(command, input=json.dumps(input_data), text=True, capture_output=True)
    if process.returncode != 0:
        raise RuntimeError(f"Ollama CLI error: {process.stderr}")
    response = process.stdout
    return response

@app.route("/")
def index():
    return render_template('chat.html')


@app.route("/get", methods=["GET", "POST"])
def chat():
    msg = request.form["msg"]
    input = msg
    print(input)
    response = rag_chain(input)
    print(response)
    return str(response)  # Return plain text response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port= 8080, debug= True)