import streamlit as st
import PyPDF2
import io
import requests
import json

# Page config
st.set_page_config(page_title="College Notes Summarizer", page_icon="📚", layout="wide")

# Title and description
st.title("📚 College Notes Summarizer")
st.markdown("Upload your lecture PDFs and get AI-generated summaries instantly!")

# Sidebar for API key
with st.sidebar:
    st.header("⚙️ Configuration")
    groq_api_key = st.text_input("Enter Groq API Key", type="password", help="Get your API key from https://console.groq.com")
    st.markdown("---")
    st.markdown("### How to use:")
    st.markdown("1. Enter your Groq API key")
    st.markdown("2. Upload a PDF lecture file")
    st.markdown("3. Click 'Generate Summary'")
    st.markdown("4. Get your summarized notes!")

def split_text(text, chunk_size=3000):
    """Split text into chunks"""
    words = text.split()
    chunks = []
    current_chunk = []
    current_size = 0
    
    for word in words:
        current_chunk.append(word)
        current_size += len(word) + 1
        
        if current_size >= chunk_size:
            chunks.append(' '.join(current_chunk))
            current_chunk = []
            current_size = 0
    
    if current_chunk:
        chunks.append(' '.join(current_chunk))
    
    return chunks

def call_groq_api(api_key, prompt, model="llama-3.3-70b-versatile"):
    """Call Groq API directly"""
    url = "https://api.groq.com/openai/v1/chat/completions"
    
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 2000
    }
    
    response = requests.post(url, headers=headers, json=data)
    
    if response.status_code == 200:
        return response.json()['choices'][0]['message']['content']
    else:
        raise Exception(f"API Error: {response.status_code} - {response.text}")

def summarize_document(text, api_key, summary_type="Concise", model="llama-3.3-70b-versatile"):
    """Summarize document using Groq API"""
    chunks = split_text(text, chunk_size=3000)
    
    if len(chunks) == 1:
        # Single chunk - direct summarization
        if summary_type == "Concise":
            prompt = f"""Write a concise summary of the following lecture notes. Focus on key concepts, main ideas, and important takeaways:

{text}

CONCISE SUMMARY:"""
        else:
            prompt = f"""Write a detailed summary of the following lecture notes. Include:
- Main topics and concepts
- Key definitions and explanations
- Important examples or case studies
- Critical takeaways

{text}

DETAILED SUMMARY:"""
        
        return call_groq_api(api_key, prompt, model)
    
    else:
        # Multiple chunks - summarize each then combine
        summaries = []
        progress_bar = st.progress(0)
        status_text = st.empty()
        
        for i, chunk in enumerate(chunks):
            status_text.text(f"Processing chunk {i+1}/{len(chunks)}...")
            progress_bar.progress((i + 1) / (len(chunks) + 1))
            
            chunk_prompt = f"Summarize the key points from this section of lecture notes:\n\n{chunk}\n\nSUMMARY:"
            summary = call_groq_api(api_key, chunk_prompt, model)
            summaries.append(summary)
        
        # Combine all summaries
        status_text.text("Combining summaries...")
        combined_text = "\n\n".join(summaries)
        
        if summary_type == "Concise":
            final_prompt = f"""Based on these section summaries from lecture notes, create a final concise summary that captures all key concepts:

{combined_text}

FINAL CONCISE SUMMARY:"""
        else:
            final_prompt = f"""Based on these section summaries from lecture notes, create a comprehensive final summary that includes:
- All main topics and concepts
- Key definitions and explanations
- Important examples
- Critical takeaways

{combined_text}

FINAL DETAILED SUMMARY:"""
        
        final_summary = call_groq_api(api_key, final_prompt, model)
        progress_bar.progress(1.0)
        status_text.empty()
        progress_bar.empty()
        
        return final_summary

# Main content area
uploaded_file = st.file_uploader("Upload Lecture PDF", type=['pdf'])

col1, col2 = st.columns([1, 1])

with col1:
    summary_type = st.selectbox(
        "Summary Type",
        ["Concise", "Detailed"],
        help="Concise: Quick overview | Detailed: Comprehensive summary"
    )

with col2:
    model_choice = st.selectbox(
        "Model",
        ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"],
        help="70b: Best quality | 8b: Fastest | Mixtral: Balanced"
    )

if st.button("🎯 Generate Summary", type="primary", use_container_width=True):
    if not groq_api_key:
        st.error("⚠️ Please enter your Groq API key in the sidebar")
    elif not uploaded_file:
        st.error("⚠️ Please upload a PDF file")
    else:
        try:
            with st.spinner("📖 Reading PDF..."):
                # Read PDF
                pdf_reader = PyPDF2.PdfReader(io.BytesIO(uploaded_file.read()))
                text = ""
                for page in pdf_reader.pages:
                    text += page.extract_text()
                
                if not text.strip():
                    st.error("❌ Could not extract text from PDF. The file might be image-based.")
                    st.stop()
                
                st.success(f"✅ Extracted {len(text)} characters from {len(pdf_reader.pages)} pages")
            
            with st.spinner("🤖 Generating summary with AI..."):
                summary = summarize_document(text, groq_api_key, summary_type, model_choice)
            
            # Display results
            st.success("✨ Summary Generated Successfully!")
            
            st.markdown("---")
            st.subheader("📝 Summary")
            st.markdown(summary)
            
            # Download option
            st.download_button(
                label="📥 Download Summary",
                data=summary,
                file_name=f"{uploaded_file.name.replace('.pdf', '')}_summary.txt",
                mime="text/plain"
            )
            
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("💡 Tip: Make sure your Groq API key is valid and you have available credits")

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: gray;'>
        Built with Streamlit & Groq | Made for students 🎓
    </div>
    """,
    unsafe_allow_html=True
)