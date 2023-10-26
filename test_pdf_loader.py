import unittest
from main import PyPDFDirectoryLoader

class TestPDFLoader(unittest.TestCase):
    def test_pdf_loading(self):
        # Test PDF loading functionality
        loader = PyPDFDirectoryLoader("pdfs")

        # Load all PDF documents
        all_documents = loader.load()

        # Define the subject or keyword to search for
        subject = "net zero strategy"

        # Filter documents related to the subject
        relevant_documents = [doc for doc in all_documents if subject in doc]

        # Now, relevant_documents contains the documents related to "net zero strategy"
        for doc in relevant_documents:
            print(doc)  # Print the titles of relevant documents

if __name__ == '__main__':
    unittest.main()
