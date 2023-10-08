from langchain.vectorstores.chroma import Chroma
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.document_loaders.text import TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
from langchain.llms.openai import OpenAI
from langchain.schema.vectorstore import VectorStoreRetriever


persisted_dir = "db"


def qa_bot_with_chroma():
    loader = TextLoader("assets/state_of_the_union.txt")
    documents = loader.load()  # Initial text documents

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=10)
    texts = text_splitter.split_documents(
        documents,
    )  # Final version of the processed documents.

    embedding = OpenAIEmbeddings()
    vectordb = Chroma.from_documents(
        documents=texts,
        embedding=embedding,
        persist_directory=persisted_dir,
    )  # Create the db.

    vectordb = Chroma(
        persist_directory=persisted_dir, embedding_function=embedding
    )  # Load the db
    llm = OpenAI()
    retriever = VectorStoreRetriever(vectorstore=vectordb)
    chain = RetrievalQA.from_llm(llm=llm, retriever=retriever, verbose=True)
    return chain
