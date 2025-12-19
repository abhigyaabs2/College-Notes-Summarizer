# 📚 College Notes Summarizer

An AI-powered application that transforms lengthy lecture PDFs into concise, easy-to-digest summaries using Groq's advanced language models.

## 🌟 Features

- **📄 PDF Upload**: Easy drag-and-drop interface for lecture notes
- **🤖 AI-Powered Summarization**: Leverages Groq's Llama 3.3 models for intelligent text processing
- **⚡ Multiple Model Options**: Choose between speed and quality
  - Llama 3.3 70B - Best quality summaries
  - Llama 3.1 8B - Lightning-fast processing
  - Mixtral 8x7B - Balanced performance
- **📝 Flexible Summary Types**:
  - **Concise**: Quick overviews for rapid review
  - **Detailed**: Comprehensive summaries with key concepts
- **📥 Download Option**: Save summaries as text files for offline access
- **🎯 Smart Chunking**: Automatically handles large documents by processing in chunks
- **📊 Progress Tracking**: Real-time feedback during processing

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Groq API key ([Get it here](https://console.groq.com))

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/College-Notes-Summarize.git
cd College-Notes-Summarize
```

2. **Install dependencies**
```bash
pip install streamlit pypdf2 requests
```

3. **Run the application**
```bash
streamlit run college.py
```

4. **Open your browser**
   - The app will automatically open at `http://localhost:8501`

## 🎯 How to Use

1. **Enter API Key**: Add your Groq API key in the sidebar
2. **Upload PDF**: Select your lecture notes PDF file
3. **Choose Settings**:
   - Select summary type (Concise or Detailed)
   - Pick your preferred model
4. **Generate**: Click the "Generate Summary" button
5. **Download**: Save your summary for future reference

## 🛠️ Technologies Used

- **[Streamlit](https://streamlit.io/)** - Web application framework
- **[PyPDF2](https://pypdf2.readthedocs.io/)** - PDF text extraction
- **[Groq API](https://groq.com/)** - LLM inference and summarization
- **Python Requests** - API communication

## 📁 Project Structure

```
college-notes-summarizer/
│
├── app.py              # Main application file
├── README.md           # Project documentation
└── .gitignore         # Git ignore file
```

## 💡 Use Cases

- **Exam Preparation**: Quickly review key concepts before tests
- **Lecture Review**: Reinforce learning after classes
- **Study Groups**: Share concise notes with classmates
- **Time Management**: Save hours of manual note-taking
- **Accessibility**: Help students who struggle with long-form reading

## 🔒 Privacy & Security

- All processing happens through secure Groq API calls
- No data is stored on servers
- PDF content is processed in memory only
- Your API key remains private and local

## 🤝 Contributing

Contributions are welcome! Here are some ways you can help:

1. Report bugs
2. Suggest new features
3. Improve documentation
4. Submit pull requests

## 📝 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 🙏 Acknowledgments

- Groq for providing fast and efficient LLM inference
- Streamlit for the amazing web framework
- The open-source community for inspiration

## 🔮 Future Enhancements

- [ ] Add support for multiple file formats (DOCX, TXT)
- [ ] Implement bullet-point formatting option
- [ ] Add keyword extraction feature
- [ ] Create quiz generation from summaries
- [ ] Support for multiple language translations
- [ ] Batch processing for multiple PDFs
- [ ] Custom summary length control

---

⭐ If you find this project helpful, please give it a star!

Made with ❤️ for students everywhere
