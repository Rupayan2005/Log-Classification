🔍 Log Classification with Hybrid Framework

This project implements a hybrid log classification system that combines multiple machine learning and rule-based strategies to accurately classify log messages of varying complexity. It supports both automated backend classification and a Streamlit frontend interface for user interaction.

🚀 Key Features

Hybrid Classification Pipeline:

📜 Regex-based Classification:Fast and efficient for logs with predictable patterns using predefined rules.

🤖 Sentence Transformer + Logistic Regression:Embeds log messages using Sentence Transformers and classifies them with a Logistic Regression model—ideal when labeled data is available.

🧠 LLM-powered Classification (Gemini API):Uses Google’s Gemini model for complex or novel log patterns where rule-based or ML approaches are insufficient.

📊 Streamlit Frontend:

Simple drag-and-drop interface to upload log files.

Displays classified logs with export capability.

📁 Folder Structure

log-classifier/
│
├── training/                 # Code for training ML models and regex classification
├── models/                   # Saved models and embeddings
├── resources/                # CSVs, sample outputs, utility files
├── server.py                 # FastAPI backend server
├── frontend.py               # Streamlit frontend app
└── requirements.txt          # Project dependencies

⚙️ Setup Instructions

1. Clone the Repository

git clone https://github.com/Rupayan2005/Log-Classification.git

cd log-classifier

2. Install Dependencies

Make sure Python 3.8+ is installed, then run:

pip install -r requirements.txt

3. Add Environment Variables

Create a .env file in the root directory and include your Google Gemini API Key:

GEMINI_API_KEY=your_gemini_api_key_here

💾 Running the Applications

Backend: FastAPI Server

uvicorn server:app --reload

API Docs: http://127.0.0.1:8000/docs

Redoc: http://127.0.0.1:8000/redoc

Frontend: Streamlit App

streamlit run frontend.py

Access the frontend at: http://localhost:8501

📅 Usage

Open the Streamlit interface.

Upload a CSV file containing logs with the following columns:

source

log_message

The system classifies each entry and returns a downloadable file with an added column:

target_label

🧠 Tech Stack

FastAPI – for serving the API

Streamlit – for frontend interface

Google Gemini API – LLM-based fallback classification

scikit-learn, sentence-transformers – for ML-based classification

pandas, regex – for data handling and rule-based classification


✨ Acknowledgments

Google AI – for the Gemini API

HuggingFace – for Sentence Transformers

FastAPI and Streamlit – for powering the app