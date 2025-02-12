import streamlit as st

# About Page with Keyword and Query Extractor workflow
def run():
    # Set the title for the about page
    st.title("📄 About the Keyword-Based Extractor and Query-Based Extractor")

    # Introduction
    st.markdown("""
    Welcome to the **Keyword-Based Extractor** and **Query-Based Extractor** page! This tool allows you to extract specific information from PDF documents based on keywords or user-defined queries.
    """)

    # Slide for Keyword-Based Extractor definition and workflow
    with st.expander("🔑 Keyword-Based Extractor"):
        st.markdown("""
        **Definition**:
        The **Keyword-Based Extractor** helps identify and extract data related to specific keywords in PDF documents. It uses predefined keywords to search through the text in the document and extract the relevant surrounding content (sentences or paragraphs). The results are displayed alongside the page images for easy visualization of where each keyword appears.
        
        **Workflow**:
        1. **Upload PDF**: Users upload the PDF file they want to extract information from.
        2. **Select Keywords**: The user selects predefined or custom keywords that are relevant to the document.
        3. **Extract Information**: The extractor searches for these keywords in the document, highlights their occurrences, and extracts the surrounding context.
        4. **Results**: The relevant keywords and surrounding sentences are displayed in an easy-to-read format. Page images with highlighted keywords are also shown for better visualization.

        **Key Features**:
        - Extracts keywords from text-based PDFs.
        - Displays the extracted sentences with context.
        - Highlights keywords directly on the PDF pages.
        """)

    # Slide for Query-Based Extractor definition and workflow
    with st.expander("❓ Query-Based Extractor"):
        st.markdown("""
        **Definition**:
        The **Query-Based Extractor** allows users to define specific queries or search patterns (such as regular expressions) that they want to search within a PDF document. This is especially useful when the user needs to find information based on complex queries or patterns rather than specific keywords.
        
        **Workflow**:
        1. **Upload PDF**: Similar to the Keyword-Based Extractor, users upload the PDF.
        2. **Define Query**: Users provide specific search queries (e.g., sentences or exact phrases).
        3. **Extract Results**: The extractor searches for the query matches within the document based on sentence similiarity.
        4. **Display Results**: The results of the query are displayed with the matching text and highlighted locations in the document, similar to how keyword extraction works.
        
        **Key Features**:
        - Enables complex pattern-based extractions using user-defined queries.
        - Allows the use of regular expressions for more advanced queries.
        - Supports extraction of both text-based and image-based PDF content.
        """)

    # General Information Section
    st.markdown("""
    **Both extractors** serve to streamline the process of finding and extracting important information from lengthy PDF documents, saving time and effort. Depending on the document's structure and the user's needs, you can choose between these two extraction methods to get the most accurate results.
    """)

    # Contact Us Section (highlighted)
    st.markdown("""
    <h3 style='color: #FF5733;'>📩 **Contact Us**:</h3>
    <p>If you have any questions or need further assistance, feel free to reach out to us at:</p>
    <p style='font-size: 18px; color: #1E90FF;'><b>dineshkumar.n@msci.com</b></p>
    <p>We are happy to assist you!</p>
    """, unsafe_allow_html=True)
if __name__ == "__main__":
    run()
