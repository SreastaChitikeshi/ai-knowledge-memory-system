import streamlit as st
from core import KnowledgeBase

st.set_page_config(page_title="Personal AI Knowledge Memory", layout="centered", page_icon="🧠")

# Initialize backend
@st.cache_resource
def load_kb():
    return KnowledgeBase()

kb = load_kb()

st.title("🧠 AI Knowledge Memory System")
st.markdown("A Second Brain AI to act as a personal knowledge assistant. Store user notes, process using NLP, and intelligently retrieve information.")

tab1, tab2 = st.tabs(["Add Knowledge 📝", "Search Knowledge 🔍"])

with tab1:
    st.header("Store New Knowledge")
    with st.form("add_knowledge_form"):
        topic = st.text_input("Topic", placeholder="e.g. Neural Networks")
        date = st.date_input("Date")
        content = st.text_area("Content", placeholder="e.g. Backpropagation is used to update weights in neural networks...", height=200)
        
        submitted = st.form_submit_button("Add to Memory")
        
        if submitted:
            if topic and content:
                # Add to knowledge base
                date_str = date.strftime("%B %d, %Y")
                try:
                    kb.add_knowledge(topic, date_str, content)
                    st.success("Successfully added to knowledge memory!")
                except Exception as e:
                    st.error(f"Error adding to memory: {e}")
            else:
                st.warning("Please fill in both Topic and Content.")

with tab2:
    st.header("Ask Your Knowledge Memory")
    query = st.text_input("Your question", placeholder="e.g. What did I learn about neural networks?")
    
    if st.button("Search Knowledge") or query:
        if query:
            with st.spinner("Searching semantic memory..."):
                try:
                    results = kb.query_knowledge(query, top_k=3)
                    
                    if results:
                        st.subheader("🤖 Here is what you know:")
                        for idx, res in enumerate(results):
                            st.markdown(f"**Knowledge Entry #{idx+1}**")
                            st.markdown(f"> **Topic:** {res['topic']}")
                            st.markdown(f"> **Date:** {res['date']}")
                            st.markdown(f"> **Content:** {res['content']}")
                            st.divider()
                    else:
                        st.info("No matching knowledge found in memory yet.")
                except Exception as e:
                    st.error(f"Error searching memory: {e}")
        else:
            st.warning("Please enter a question to search.")

# Information footer
st.markdown("---")
st.caption("AI Knowledge Memory System • Built with Streamlit, SentenceTransformers, and FAISS")
