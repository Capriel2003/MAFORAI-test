# Astronomical Transient Classification Copilot

## 🌌 Overview
This project implements an intelligent data processing pipeline and an AI-powered "Copilot" designed to assist astronomers in analyzing transient events (Supernovae, Variable Stars, etc.) from the Skyportal platform.

The system processes raw JSON data, extracts critical photometric and spectral features, and utilizes a **Large Language Model (LLM)** to generate scientific summaries, classification reasoning, and observational recommendations.

## 🚀 Key Features
* **ETL Pipeline**: Parses complex, nested JSON data into structured, machine-learning-ready datasets.
* **Feature Engineering**: Extracts key metrics such as `rise_rate`, `redshift`, and aggregates astronomer comments.
* **Local Inference Architecture**: configured to run with **Open-Source LLMs (e.g., Llama-3)** via **LM Studio**, ensuring data privacy and zero API costs.
* **Resilience**: Includes error handling for API connection failures.

## 🛠️ Architecture
The project consists of three main modules:
1.  **`data_pipeline.py`**: Handles data ingestion, cleaning, and flattening.
2.  **`intelligent_agent.py`**: The "Brain" of the system. It connects to the LLM (via OpenAI-compatible local endpoint) to perform reasoning tasks.
3.  **`main.py`**: The orchestrator that executes the workflow and generates reports.

## 📦 Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Capriel2003/MAFORAI-test.git
   cd MAFORAI-test
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. Setup Local LLM (Recommended):
- Download and install LM Studio.
- Load a model (e.g., Llama-3.2-3B-Instruct).
- Start the Local Server on port 1234.

## ▶️ Usage
Run the main script:
   ```bash
   python main.py
   ```
The script will:
- Load sources_sample.json.
- Connect to the Local LLM at http://localhost:1234/v1.
- Analyze the most relevant objects.
- Output the results to copilot_results.csv.
