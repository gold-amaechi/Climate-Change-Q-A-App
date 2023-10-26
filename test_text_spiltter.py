import unittest
from main import RecursiveCharacterTextSplitter, PyPDFDirectoryLoader

class TestTextSplitter(unittest.TestCase):
    def test_text_splitting(self):
        # Test text splitting functionality
        
        # Initialize the PDF loader
        loader = PyPDFDirectoryLoader("pdfs")

        # Load all PDF documents from the "pdfs" directory
        docs = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=10,  # Set appropriate values for testing
            chunk_overlap=5,
            length_function=len,
            is_separator_regex=False,
            separators=["\n\n", "\n", " ", ""]
        )
        result = text_splitter.split_documents(docs)
        self.assertIsNotNone(result)  # Assert that the result is not None

if __name__ == '__main__':
    unittest.main()