from langchain.document_loaders import PyPDFDirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from dataclasses import dataclass
from decouple import config 
import pinecone

def ingest_docs(subject: str, pinecone_env):
    """Load documents based on a specified subject into the Pinecone vector store"""
    openai_api_key = config('OPENAI_API_KEY') # load OpenAI API key from environment variable
    try:
        pinecone.init(api_key=pinecone_env.api_key, environment=pinecone_env.environment_region)
        # Search for documents in directory
        loader = PyPDFDirectoryLoader("pdfs")
        docs = loader.load() 

        """Configure the RecursiveCharacterTextSplitter to split documents into smaller chunks for processing"""
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=50,
            length_function = len,
            is_separator_regex = False, 
            separators=["\n\n", "\n", " ", ""]   
        )

        # split documents and initialise embedding
        document = text_splitter.split_documents(docs)
        embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)
   
        # Store documents in vector store
        Pinecone.from_documents(documents=document, embedding=embedding, index_name=pinecone_env.index_name)

        print(f"Successfully loaded {subject} into the vectorstore.")

    except Exception as e:
        print(f"An error occurred while ingesting documents: {e}")

def run_llm(pinecone_env):
    """Initializes the Pinecone environment, sets up the language model (LLM), and handles user interactions with the LLM"""
    openai_api_key = config('OPENAI_API_KEY') 
    try:
        pinecone.init(api_key=pinecone_env.api_key, environment=pinecone_env.environment_region)

        embedding = OpenAIEmbeddings(openai_api_key=openai_api_key)

        # Load Pinecone index
        doc_search = Pinecone.from_existing_index(
            index_name=pinecone_env.index_name,
            embedding=embedding
        )
  
        # Set up ChatOpenAI model with specific parameters
        chat_model = ChatOpenAI(
            openai_api_key=openai_api_key,
            model_name="gpt-3.5-turbo",
            temperature=1,
            verbose=True
        )
 
        """configure a ConversationalRetrievalChain using the ChatOpenAI model and the Pinecone index as a retriever"""
        qa = ConversationalRetrievalChain.from_llm(
            llm=chat_model,
            retriever=doc_search.as_retriever()
        )

        # Store chat history
        chat_history = []

        # Welcome message
        print("Welcome, ask me about climate change.")
        print("To exit the application, type the word 'quit'.")

        # Starts loop for user interaction
        while True:
            query = input("You: ")
            if query.strip() == "":  # Check if the query is empty
                print("Invalid query. Please enter a valid question.")
                continue  # Skip to the next iteration

            if query.lower() == "quit": # Exit loop and application
                print("Exiting the application.")
                break
            response = qa({"question": query, "chat_history": chat_history})
            answer = response.get("answer")
            print(f"Response: {response.get('answer')}")
            chat_history.append((query, answer))  

    except Exception as e:
        print(f"An error occurred while running the language model: {e}")

@dataclass
# Structure for storing Pinecone credentials
class PineconeCredentials:
    api_key: str
    index_name: str
    environment_region: str
 

def init_pinecone():
    """Initializes the Pinecone environment with the necessary API keys and environment variables."""
    api_key = config('PINECONE_SECRET_KEY') # load Pinecone API key from environment variable
    index_name = "medium-text-db"
    environment = "gcp-starter" 

    if api_key is None: # Check if Pinecone API key is set
        msg = "PINECONE_API_KEY environment variable is not set."
        raise ValueError(msg)    

    if index_name is None: # Check if Pinecone index name is set
        msg = "PINECONE_INDEX_NAME environment variable is not set."
        raise ValueError(msg)

    if environment is None: # Check if Pinecone environment region key is set
        msg = "PINECONE_ENVIRONMENT_REGION environment variable is not set."
        raise ValueError(msg)
    
    # If all variables are set, return PineconeCredentials object
    return PineconeCredentials(
        api_key = config('PINECONE_SECRET_KEY'),
        index_name=index_name,
        environment_region=environment
    )

# Execution block
if __name__ == "__main__":
    try:
        pinecone_env = init_pinecone()
        run_llm(pinecone_env)
    except Exception as e:
        print(f"An error occurred: {e}")