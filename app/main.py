import streamlit as st

# Set the page configuration (optional)
st.set_page_config(page_title="Extractor", page_icon=":material/edit:")

# Sidebar for navigation
page = st.sidebar.selectbox("Select a page", ["About","Keyword Based Extractor", "Query Based Extractor"])

# Conditional logic for different pages
if page == "About":
    import about
    about.run()
elif page == "Keyword Based Extractor":
    st.title("Keyword Based Extractor")
    # Import and run the PDF extraction page
    import keyword_extractor
    keyword_extractor.run()

elif page == "Query Based Extractor":
    st.title("Query Based Extractor")
    # Import and run the web extraction page
    import query_extractor
    query_extractor.run()
