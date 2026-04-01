#  End-to-End Student Performance Predictor

## 📌 Project Overview
This project is a comprehensive, production-ready Machine Learning solution designed with **Modular Programming** and **MLOps** best practices. It automates the entire lifecycle of a machine learning model, from data ingestion to cloud deployment using a robust CI/CD pipeline.

## 🛠️ Key Features
- **Modular Architecture:** Separate components for Data Ingestion, Transformation, and Model Training.
- **Custom Logging & Exceptions:** Robust error tracking and system-wide logging for production monitoring.
- **Automated Pipeline:** Integrated training and prediction pipelines.
- **Containerization:** Fully Dockerized application for consistent environment execution.
- **CI/CD Integration:** Automated deployment workflow using GitHub Actions.

## 💻 Tech Stack
- **Language:** Python
- **ML Frameworks:** Scikit-Learn, Pandas, NumPy
- **Web Interface:** Flask
- **DevOps:** Docker, GitHub Actions
- **Cloud:** AWS (ECR, S3, EC2/App Runner)

## 📂 Project Structure
```text
├── src/
│   ├── components/         # Data Ingestion, Transformation, Model Trainer
│   ├── pipeline/           # Training and Prediction Pipelines
│   ├── logger.py           # Custom system logging
│   ├── exception.py        # Custom exception handling
│   └── utils.py            # Common utility functions
├── artifacts/              # Saved models and preprocessor objects
├── notebooks/              # Jupyter Notebooks for EDA and experiments
├── app.py                  # Flask web application entry point
├── Dockerfile              # Docker image configuration
└── requirements.txt        # Project dependencies
