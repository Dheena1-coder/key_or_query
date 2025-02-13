import streamlit as st

# Set the page configuration (optional)
st.set_page_config(page_title="Extractor", page_icon=":material/edit:")

# Sidebar for navigation (without "About" in the dropdown)
page = st.sidebar.selectbox("Select a page", 
                            ["Keyword Based Extractor", "Query Based Extractor"])

# Add a "Contact" or "About" section at the bottom of the sidebar using a divider
st.sidebar.markdown("---")  # This adds a horizontal line to separate sections
st.sidebar.markdown("### About")
about_link = st.sidebar.button("Go to About Page")  # Button to trigger the About page

# Conditional logic for different pages
if page == "Keyword Based Extractor":
    st.title("Keyword Based Extractor")
    # Import and run the PDF extraction page
    import keyword_extractor
    keyword_extractor.run()

elif page == "Query Based Extractor":
    st.title("Query Based Extractor")
    # Import and run the web extraction page
    import query_extractor
    query_extractor.run()

# If the "About" button is clicked, run the about page
elif about_link:
    import about
    about.run()
