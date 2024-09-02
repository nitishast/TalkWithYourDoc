import streamlit as st
import os

def main():
    st.set_page_config(layout="wide")

    # Main content
    st.title("PDF Search App")

    # Sidebar
    with st.sidebar:
        st.header("Upload Documents")
        uploaded_files = st.file_uploader("Upload the Documents in PDF format here:", 
                                          type=["pdf"], 
                                          accept_multiple_files=True)
        
        if uploaded_files:
            st.subheader("Uploaded PDFs:")
            for file in uploaded_files:
                st.write(f"- {file.name}")

    # Main content area
    col1, col2 = st.columns([1, 1])

    with col1:
        st.write("Upload the Documents in PDF format here:")
        st.info("Use the sidebar to upload PDF files.")

    with col2:
        st.text_input("User: Write your question here:")
        st.text_area("Response:", height=200)

if __name__ == "__main__":
    main()