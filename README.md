# 🚢 Titanic Survival Prediction API

A production-ready Machine Learning REST API that predicts whether a passenger would survive the Titanic disaster using a trained Scikit-learn Decision Tree model. The project follows industry best practices including data preprocessing, feature engineering, ML pipelines, Docker containerization, and FastAPI deployment.

---

# 📌 Project Overview

The Titanic Survival Prediction project demonstrates how to build, package, and deploy a Machine Learning model as a production-ready REST API.

This project includes:

- Exploratory Data Analysis (EDA)
- Data Cleaning & Preprocessing
- Feature Engineering
- Scikit-learn Pipeline
- ColumnTransformer
- Decision Tree Classification
- Model Serialization using Joblib
- FastAPI REST API
- Docker Containerization
- Docker Compose
- Production-ready Project Structure

---

# 🧠 Problem Statement

Predict whether a passenger survived the Titanic disaster based on passenger information such as:

- Passenger Class
- Gender
- Age
- Fare
- Number of Siblings/Spouses
- Number of Parents/Children
- Embarked Port

Target Variable:

```
Survived
0 = No
1 = Yes
```

---

# 📂 Project Structure

```
Titanic_Survival_Prediction
│
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── predictor.py
│   └── schemas.py
│
├── datasets
│   └── Titanic-Dataset.csv
│
├── model
│   └── pipeline.joblib
│
├── notebooks
│   └── Titanic_Survival_Prediction.ipynb
│
├── Dockerfile
├── docker-compose.yml
├── .dockerignore
├── requirements.txt
├── README.md
└── LICENSE
```

---

# ⚙️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- FastAPI
- Pydantic
- Uvicorn
- Joblib
- Docker
- Docker Compose
- Git
- GitHub

---

# 🔬 Machine Learning Workflow

```
Dataset

↓

EDA

↓

Data Cleaning

↓

Feature Engineering

↓

Train-Test Split

↓

ColumnTransformer

↓

Pipeline

↓

Decision Tree Classifier

↓

Hyperparameter Tuning

↓

pipeline.joblib

↓

FastAPI

↓

Docker

↓

Docker Compose
```

---

# 🚀 API Endpoints

## Home

```
GET /
```

Returns API status.

---

## Prediction

```
POST /predict
```

Example Request

```json
{
  "Pclass": 3,
  "Sex": "male",
  "Age": 22,
  "SibSp": 1,
  "Parch": 0,
  "Fare": 7.25,
  "Embarked": "S"
}
```

Example Response

```json
{
  "prediction": 0
}
```

---

# 📦 Run Locally

Create Virtual Environment

```bash
python -m venv .venv
```

Activate

Windows

```bash
.venv\Scripts\activate
```

Install Requirements

```bash
pip install -r requirements.txt
```

Run API

```bash
uvicorn app.main:app --reload
```

Open Swagger UI

```
http://localhost:8000/docs
```

---

# 🐳 Docker

Build

```bash
docker compose build
```

Run

```bash
docker compose up
```

Stop

```bash
docker compose down
```

Swagger

```
http://localhost:8000/docs
```

---

# 📈 Model Used

Decision Tree Classifier

Reasons:

- Easy to interpret
- Good baseline classifier
- Handles mixed feature types
- Works well with preprocessing pipeline

---

# 📊 Dataset

Source:

Titanic Dataset

Features include:

- Pclass
- Sex
- Age
- SibSp
- Parch
- Fare
- Embarked

Target:

```
Survived
```

---

# 🎯 Key Learning Outcomes

- Exploratory Data Analysis
- Data Cleaning
- Missing Value Handling
- Feature Engineering
- Pipeline Creation
- ColumnTransformer
- Model Serialization
- FastAPI Development
- Docker Containerization
- REST API Deployment
- Git & GitHub Workflow

---

# 📌 Future Improvements

- Random Forest Classifier
- XGBoost Classifier
- LightGBM
- CatBoost
- Azure Container Apps Deployment
- GitHub Actions CI/CD
- Model Monitoring
- MLflow Integration

---

# 👨‍💻 Author

**Sumanth Ashwath**

Senior Infrastructure Engineer | Azure | DevOps | Machine Learning | FastAPI | Docker

GitHub

https://github.com/Sumanth181991

---

# ⭐ If you found this project useful, consider giving it a star!