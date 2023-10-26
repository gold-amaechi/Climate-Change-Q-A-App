# Climate-Change-Q-A-App

Welcome to the Climate Change Q&A App! This repository contains an application for exploring climate change topics using language models and vector similarity search.

## Overview

The Climate Change App uses various technologies, including PyPDFDirectoryLoader, RecursiveCharacterTextSplitter, OpenAIEmbeddings, Pinecone, ChatOpenAI, and ConversationalRetrievalChain to provide users with information on climate change.

- **PyPDFDirectoryLoader**: This component is responsible for searching and loading PDF documents relevant to a specified subject.

- **RecursiveCharacterTextSplitter**: It splits large documents into smaller chunks for easier processing.

- **OpenAIEmbeddings**: This component handles embeddings, leveraging the OpenAI platform for natural language understanding.

- **Pinecone**: Pinecone is a vector store that stores documents and their embeddings.

- **ChatOpenAI**: It sets up a language model for chat interactions.

- **ConversationalRetrievalChain**: This component integrates the language model with the Pinecone vector store for conversational retrieval.

## Usage

The Climate Change App can be used to:

- Ingest PDF documents related to climate change subjects into the Pinecone vector store.
- Run the Language Model (LLM) to answer questions and provide information on climate change.

## Getting Started

1. Install the required packages and dependencies mentioned in the project's setup files.

2. Configure your environment variables:
   - `PINECONE_SECRET_KEY`: Your Pinecone API key.
   - `OPENAI_API_KEY`: Your OpenAI API key.

3. Ingest Documents:
   - Run the `ingest_docs` function to load documents related to a specific subject.
   - Use the `subject` parameter to specify the subject for document loading.

4. Run Language Model:
   - Execute the `run_llm` function to start the language model and interact with it.

## Contributing

Contributions to this project are welcome. If you have suggestions or improvements, feel free to open an issue or submit a pull request.

## Acknowledgments

- [OpenAI](https://openai.com) for providing the language model.
- [Pinecone](https://pinecone.io) for the vector store service.
- [Langchain](https://python.langchain.com/docs/get_started/introduction) for empowering the project with capabilities such as generating semantic text embeddings.

## Contact

For questions or support, please contact me, github:gold-amaechi.

**Thank you for using the Climate Change Q&A App!**

