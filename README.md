# Log Classification with Hybrid Classification Framework

A comprehensive log classification system that combines multiple machine learning approaches to handle varying levels of complexity in log patterns. This project provides both API and web interface for efficient log analysis and classification.

## 🚀 Features

- **Hybrid Classification Architecture**: Combines three complementary approaches for robust log classification
- **Multiple Classification Methods**: Regex, Sentence Transformer + Logistic Regression, and LLM-based classification
- **Dual Interface**: FastAPI backend with Streamlit frontend for seamless user experience
- **Flexible Data Handling**: Processes varying complexity levels in log patterns
- **Professional Web Interface**: User-friendly file upload and download functionality

## 📋 Table of Contents

- [Classification Approaches](#classification-approaches)
- [Architecture](#architecture)
- [Installation](#installation)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Web Interface](#web-interface)
- [File Structure](#file-structure)
- [Contributing](#contributing)

## 🧠 Classification Approaches

### 1. Regular Expression (Regex)
- **Purpose**: Handles simplified and predictable log patterns
- **Best For**: Well-structured logs with consistent formats
- **Advantage**: Fast processing and deterministic results

### 2. Sentence Transformer + Logistic Regression
- **Purpose**: Manages complex patterns with sufficient training data
- **Technology**: Utilizes pre-trained Sentence Transformers for embeddings
- **Best For**: Complex logs with available labeled training data
- **Advantage**: High accuracy with proper training data

### 3. Large Language Model (Gemini API)
- **Purpose**: Handles complex patterns with limited training data
- **Technology**: Google's Gemini API for advanced language understanding
- **Best For**: Unpredictable or novel log patterns
- **Advantage**: Excellent generalization capabilities

## 🏗️ Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Streamlit     │    │    FastAPI       │    │   Classification│
│   Frontend      │───▶│    Backend       │───▶│   Framework     │
│                 │    │                  │    │                 │
└─────────────────┘    └──────────────────┘    └─────────────────┘
                                                         │
                                ┌────────────────────────┼────────────────────────┐
                                │                        │                        │
                        ┌───────▼────────┐    ┌─────────▼────────┐    ┌─────────▼────────┐
                        │     Regex      │    │ Sentence Trans.  │    │   Gemini API     │
                        │ Classification │    │ + Logistic Reg.  │    │ Classification   │
                        └────────────────┘    └──────────────────┘    └──────────────────┘
```

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- Google Gemini API key
- Internet connection for API calls

### Step 1: Clone the Repository
```bash
git clone https://github.com/Rupayan2005/Log-Classification.git

cd log-classification-framework
```

### Step 2: Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Environment Configuration
Create a `.env` file in the root directory:
```env
GEMINI_API_KEY=your_gemini_api_key_here
```

## 🚀 Usage

### Running the Complete System

#### 1. Start FastAPI Backend
```bash
uvicorn server:app --reload --port 8000
```

#### 2. Launch Streamlit Frontend
```bash
streamlit run frontend.py --server.port 8501
```

### Access Points
- **Web Interface**: http://localhost:8501
- **API Endpoint**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **Alternative Docs**: http://localhost:8000/redoc

## 📊 Data Format

### Input CSV Requirements
Your CSV file must contain the following columns:
- `source`: Source system or application generating the log
- `log_message`: The actual log message content

### Example Input
```csv
source,log_message
ModernCRM, "IP 192.168.133.114 blocked due to potential attack"
BillingSystem, "User 12345 logged in."
AnalyticsEngine, "File data_6957.csv uploaded successfully by user User265."
AnalyticsEngine, "Backup completed successfully."
```

### Output Format
The system returns a CSV with an additional column:
- `target_label`: Classified label for each log entry

### Example Output
```csv
source,log_message,target_label
ModernCRM," ""IP 192.168.133.114 blocked due to potential attack""",Security Alert
BillingSystem," ""User 12345 logged in.""",Security Alert
AnalyticsEngine," ""File data_6957.csv uploaded successfully by user User265.""",System Notification
AnalyticsEngine," ""Backup completed successfully.""",System Notification
```

## 🔧 API Documentation

### POST /classify
Classify logs from uploaded CSV file.

**Request:**
- Method: POST
- Content-Type: multipart/form-data
- File: CSV file with required columns

**Response:**
- Content-Type: application/octet-stream
- Body: Classified CSV file

**Example using curl:**
```bash
curl -X POST "http://localhost:8000/classify" \
     -H "accept: application/json" \
     -H "Content-Type: multipart/form-data" \
     -F "file=@logs.csv"
```

## 💻 Web Interface

The Streamlit frontend provides an intuitive interface for log classification:

1. **File Upload**: Drag and drop or browse to select your CSV file
2. **Validation**: Automatic validation of file format and required columns
3. **Processing**: Real-time progress indicators during classification
4. **Download**: Instant download of classified results
5. **Preview**: Table preview of classification results

## 📁 File Structure

```
log-classification-framework/
├── README.md
├── requirements.txt
├── .env
├── .gitignore
├── server.py                 # FastAPI backend server
├── frontend.py              # Streamlit web interface
├── classify.py               # All model page
├── processor_bert.py          # Bert model
├── processor_llm.py          # LLM Model
├── processor_regex.py          # Regex model
├── training/
│   ├── training.ipynb       # Jupyter Notebook Code
│   ├── dataset/ 
│       ├── synthetic_logs.csv      # Training Dataset
├── models/
│   ├── log_classifier.joblib # Saved Sentence Transformer models
├── resources/
│   ├── test.csv            # Sample CSV files
│   ├── output.csv          # Classification results
```

## ⚙️ Configuration

### Environment Variables
```env
# Required
GEMINI_API_KEY=your_gemini_api_key_here

# Optional
MODEL_PATH=./models
TEMP_DIR=./temp
MAX_FILE_SIZE=200MB
SUPPORTED_FORMATS=csv
```



## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Development Setup
```bash
pip install -r requirements.txt
pre-commit install
```


## 🙏 Acknowledgments

- Google Gemini API for advanced language understanding
- Sentence Transformers library for embedding generation
- FastAPI framework for robust API development
- Streamlit for intuitive web interface

---

**Made with ❤️ by [Rupayan]**
