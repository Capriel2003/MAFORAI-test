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
   git clone [https://github.com/YOUR_USERNAME/astro-copilot.git](https://github.com/YOUR_USERNAME/astro-copilot.git)
   cd astro-copilot
