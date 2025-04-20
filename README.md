# College AI Chatbot

Welcome to the **College AI Chatbot** project! This chatbot is designed to provide instant answers to questions about a college, such as its courses, fee structure, facilities, and more. It leverages advanced AI technologies to process and retrieve information from college-related documents.

---

## Features

- **Interactive Chat Interface**: A user-friendly web-based interface for seamless interaction.
- **AI-Powered Responses**: Uses state-of-the-art language models to generate accurate and concise answers.
- **Document Integration**: Processes and retrieves information from college-related documents (e.g., PDFs).
- **Customizable**: Easily adaptable to other institutions or datasets.
- **Local and Secure**: Runs locally, ensuring data privacy and security.

---

## Project Structure

```
College-AI-Chatbot/
├── app.py               # Main Flask application
├── test.py              # Test cases for the project
├── requirements.txt     # Python dependencies
├── setup.py             # Project setup file
├── Data/                # Folder containing college-related documents
│   └── College-Data.pdf
├── src/                 # Source code for helper functions and prompts
│   ├── helper.py
│   ├── prompt.py
├── templates/           # HTML templates for the chatbot UI
│   └── chat.html
├── static/              # Static files (CSS, images, etc.)
│   └── style.css
├── research/            # Jupyter notebooks for experimentation
│   └── trials.ipynb
└── README.md            # Project documentation
```

---

## Technologies Used

- **Frontend**: HTML, CSS (Bootstrap for styling)
- **Backend**: Python (Flask framework)
- **AI Models**: Hugging Face Transformers, Ollama (local LLMs)
- **Vector Database**: Pinecone for efficient document retrieval
- **PDF Processing**: PyPDFLoader for extracting text from PDFs

---

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-repo/College-AI-Chatbot.git
   cd College-AI-Chatbot
   ```

2. **Set Up a Virtual Environment**:
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables**:
   - Create a `.env` file in the root directory.
   - Add your Pinecone API key:
     ```env
     PINECONE_API_KEY=your_pinecone_api_key
     ```

5. **Run the Application**:
   ```bash
   python app.py
   ```
   Access the chatbot at `http://localhost:8080/`.

---

## Usage

1. Open the chatbot in your browser.
2. Ask questions about the college, such as:
   - "What is the fee structure?"
   - "What courses are offered?"
   - "Who is the chairman?"
3. View instant responses powered by AI.

---

## Contributing

Contributions are welcome! If you'd like to improve this project, please follow these steps:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add a new feature"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## Acknowledgments

- **Hugging Face**: For providing pre-trained models.
- **Pinecone**: For vector database services.
- **Flask**: For the lightweight web framework.
- **Bootstrap**: For modern and responsive UI design.

---

## Contact

For any questions or feedback, please contact:
- **Name**: Muthuvelan Thangaiah
- **Email**: tmuthuvelan0201@gmail.com