import streamlit as st
from main import ingest_docs, run_llm, init_pinecone

def main():
    # Set the page configuration
    st.set_page_config(
        page_title="Climate change app", page_icon="\U0001F604"
    )

    # Add a header
    st.header("Climate change Q & A")


    # Initialize Pinecone environment
    pinecone_env = init_pinecone()

    # Load documents section
    if st.button:
        subject = st.text_input("Enter a subject to search for:")
        if subject:
            try:
                st.write("Loading documents...")
                ingest_docs(subject, pinecone_env)
                st.write(f"Documents related to '{subject}' have been loaded.")
            except Exception as e:
                st.error(f"An error occurred while loading documents: {str(e)}")
                
    # Run language model section
    if st.button:
        action = st.button("Run Language Model")
        if action:
            try:
                run_llm(pinecone_env)
            except Exception as e:
                st.error(f"An error occurred while running the language model: {str(e)}")

if __name__ == "__main__":
    main()
