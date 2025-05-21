import streamlit as st
import requests

st.set_page_config(page_title="RAG LocalWisdom", page_icon="🤖")

# Set the title of the Streamlit app
st.title("Local Knowledge Query Analyzer")

# Input field for the user query
query = st.text_input("Enter your query:")

# Button to submit the query
if st.button("Analyze"):
    if query:
        with st.spinner("Processing..."):
            try:
                response = requests.post(
                    "http://backend:5050/query", json={"query": query}
                )
                response_data = response.json()
                
                if response.status_code == 500:
                    st.error(f"{response_data.get('error', 'An error occurred.')}")
                else:
                    st.subheader("Decomposition")
                    decomposition = response_data.get("decomposition", {})
                    st.write(f"**Bencana:** {decomposition.get('bencana', 'N/A')}")
                    st.write(f"**Objek:** {decomposition.get('objek', 'N/A')}")
                    st.write(f"**Peristiwa:** {decomposition.get('peristiwa', 'N/A')}")

                    # Display the similarity note
                    st.subheader("Similarity")
                    similarity = response_data.get("similarity", "N/A")
                    st.write(similarity)

                    # Display additional notes
                    st.subheader("Notes")
                    notes = response_data.get("notes", "N/A")
                    st.write(notes)

                    # Display references
                    st.subheader("References")
                    references = response_data.get("ref", [])
                    for ref in references:
                        with st.expander(ref.get('title', 'No Title')):
                            st.write(f"Halaman: {ref.get('page', 'N/A')}")
                            st.write(f"Referensi: {ref.get('reference', 'N/A')}")
            except Exception as e:
                st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a query.")