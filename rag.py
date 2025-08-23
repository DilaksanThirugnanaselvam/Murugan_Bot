import os

from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings


def create_rag_chain(groq_api_key):
    try:
        documents = []
        file_path = "data/murugan_knowledge.txt"
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Knowledge file not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()
            if not text.strip():
                raise ValueError(f"Knowledge file is empty: {file_path}")
            documents.append(Document(page_content=text))

        if not documents:
            raise ValueError("No documents loaded")

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        splits = text_splitter.split_documents(documents)
        if not splits:
            raise ValueError("No document splits created")

        embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )
        vectorstore = FAISS.from_documents(splits, embeddings)

        llm = ChatGroq(
            groq_api_key=groq_api_key, model="llama3-70b-8192", temperature=0
        )
        retriever = vectorstore.as_retriever()

        return retriever
    except Exception as e:
        raise Exception(f"Error creating RAG chain: {str(e)}")


def rag_tool(query, retriever):
    try:
        docs = retriever.get_relevant_documents(query)
        if not docs:
            return "No relevant documents found"
        return "\n".join([doc.page_content for doc in docs])
    except Exception as e:
        return f"Error in RAG tool: {str(e)}"
