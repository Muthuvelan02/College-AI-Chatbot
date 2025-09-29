# College AI Chatbot

A sophisticated AI-powered chatbot system designed to provide intelligent responses to college-related queries. The system leverages Retrieval-Augmented Generation (RAG) architecture with local language models to deliver accurate, context-aware answers about college information including admissions, courses, fees, facilities, and policies.

## Overview

This project implements a complete RAG-based chatbot solution that combines document processing, vector embeddings, and local AI models to create an intelligent assistant for college-related inquiries. The system processes PDF documents containing college information and provides real-time responses through an intuitive web interface.

## Architecture

- **Document Processing**: PDF documents are processed and split into semantic chunks
- **Vector Storage**: Document embeddings are stored in Pinecone vector database for efficient retrieval
- **AI Model**: Ollama with Gemma3:12b model for local inference
- **Retrieval System**: Similarity-based document retrieval with configurable parameters
- **Web Interface**: Flask-based web application with modern responsive UI

## Technologies Stack

### Backend
- **Python 3.x** - Core programming language
- **Flask** - Web framework for API and UI serving
- **LangChain** - Framework for LLM applications and RAG implementation
- **Ollama** - Local LLM inference engine with Gemma3:12b model
- **Pinecone** - Vector database for document embeddings

### Machine Learning & NLP
- **HuggingFace Transformers** - Sentence transformers for embeddings
- **sentence-transformers/all-MiniLM-L6-v2** - Embedding model
- **LangChain Community** - Document loaders and text splitters
- **PyPDF** - PDF document processing

### Frontend
- **HTML5/CSS3** - Modern web standards
- **Bootstrap 5.1.3** - Responsive UI framework
- **Font Awesome** - Icon library
- **Google Fonts (Inter)** - Typography

## Project Structure

```
College-AI-Chatbot/
├── app.py                          # Main Flask application with RAG chain
├── store_index.py                  # Vector database initialization script
├── requirements.txt                # Python dependencies
├── setup.py                        # Package configuration
├── template.py                     # Project template/boilerplate
├── test.py                         # Test suite (development)
├── .env                           # Environment variables (not tracked)
├── Data/
│   └── College-Data.pdf           # Source documents for knowledge base
├── src/
│   ├── __init__.py
│   ├── helper.py                  # Document processing utilities
│   └── prompt.py                  # System prompts and templates
├── templates/
│   └── chat.html                  # Web interface template
├── static/
│   └── style.css                  # Custom styles and animations
├── research/
│   └── trials.ipynb               # Development and experimentation
└── Generative_AI_Project.egg-info/ # Package metadata
```

## Prerequisites

- **Python 3.8+** installed on your system
- **Ollama** installed locally with Gemma3:12b model
- **Pinecone account** with API access
- **Git** for version control

## Installation & Setup

### 1. Environment Setup

```powershell
# Clone the repository
git clone https://github.com/Muthuvelan02/College-AI-Chatbot.git
cd College-AI-Chatbot

# Create and activate virtual environment
python -m venv venv
venv\Scripts\activate  # Windows PowerShell

# Install dependencies
pip install -r requirements.txt
```

### 2. Ollama Configuration

```powershell
# Install Ollama (if not already installed)
# Download from: https://ollama.ai/

# Pull the required model
ollama pull gemma3:12b
```

### 3. Environment Variables

Create a `.env` file in the project root:

```env
PINECONE_API_KEY=your_pinecone_api_key_here
```

### 4. Vector Database Setup

Initialize the Pinecone vector database with your documents:

```powershell
python store_index.py
```

This script will:
- Process PDF documents from the `Data/` directory
- Create embeddings using HuggingFace sentence transformers
- Store vectors in Pinecone with index name "chatbot"

### 5. Run the Application

```powershell
python app.py
```

The application will be available at `http://localhost:8080`

## Configuration

### Model Configuration
- **Embedding Model**: sentence-transformers/all-MiniLM-L6-v2 (384 dimensions)
- **LLM Model**: Gemma3:12b via Ollama
- **Chunk Size**: 500 characters with 20 character overlap
- **Retrieval**: Top 3 similar documents with cosine similarity

### Pinecone Settings
- **Index Name**: chatbot
- **Dimensions**: 384
- **Metric**: cosine
- **Cloud**: AWS (us-east-1)

## Usage Examples

### Web Interface
Navigate to `http://localhost:8080` and interact with the chatbot through the modern web interface.

### Sample Queries
- "What programs does the college offer?"
- "What is the admission process?"
- "Tell me about the fee structure"
- "What facilities are available on campus?"
- "Who are the faculty members in Computer Science?"

## API Endpoints

### GET `/`
Serves the main chat interface

### POST `/get`
Processes chat messages and returns AI responses
- **Parameter**: `msg` (form data)
- **Returns**: Plain text response from the RAG system

## Development

### Adding New Documents
1. Place PDF files in the `Data/` directory
2. Run `python store_index.py` to reprocess and update the vector database

### Customizing Prompts
Edit `src/prompt.py` to modify the system prompt and response behavior

### Frontend Modifications
- HTML templates: `templates/chat.html`
- Styles: `static/style.css`

## Troubleshooting

### Common Issues

**Ollama Connection Errors**
- Ensure Ollama is running: `ollama serve`
- Verify model is available: `ollama list`

**Pinecone API Errors**
- Check API key validity
- Verify index exists and is accessible
- Ensure sufficient quota/credits

**Empty Responses**
- Verify documents are properly indexed
- Check if query matches document content
- Review embedding model configuration

## Performance Optimization

- **Chunking Strategy**: Adjust chunk size in `src/helper.py` for better context
- **Retrieval Count**: Modify `search_kwargs={"k": 3}` in `app.py`
- **Model Selection**: Switch between different Ollama models as needed

## Security Considerations

- Store API keys securely in environment variables
- Use HTTPS in production deployments
- Implement rate limiting for API endpoints
- Sanitize user inputs to prevent injection attacks

## Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature-name`
3. Make your changes and test thoroughly
4. Commit with descriptive messages: `git commit -m "Add feature description"`
5. Push to your fork: `git push origin feature-name`
6. Create a Pull Request with detailed description

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for complete terms.

## Author

**Muthuvelan Thangaiah**
- Email: tmuthuvelan0201@gmail.com
- GitHub: [@Muthuvelan02](https://github.com/Muthuvelan02)

## Acknowledgments

- **LangChain Community** - For providing comprehensive tools for building LLM applications
- **HuggingFace** - For open-source transformer models and embeddings
- **Pinecone** - For scalable vector database infrastructure
- **Ollama** - For local LLM inference capabilities
- **Flask & Bootstrap** - For web framework and responsive UI components

## Future Enhancements

- Multi-document support with source attribution
- Conversation history and context maintenance
- Admin panel for document management
- Advanced analytics and query insights
- Mobile application development
- Multi-language support
- Integration with college management systems

## Support

For technical support, feature requests, or questions:

- **Create an Issue**: [GitHub Issues](https://github.com/Muthuvelan02/College-AI-Chatbot/issues)
- **Email**: tmuthuvelan0201@gmail.com
- **Documentation**: Refer to inline code comments and docstrings

---

**Built with precision for educational excellence** | **Powered by AI, Driven by Innovation**