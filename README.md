# 🧠 Smart Price Predictor
[![Python](https://img.shields.io/badge/Python-3.11-blue)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-Backend-brightgreen)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Containerized-blue)](https://www.docker.com/)
[![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestrated-326ce5)](https://kubernetes.io/)
[![Machine Learning](https://img.shields.io/badge/ML-RandomForest-orange)](https://scikit-learn.org/stable/)

A complete **Machine Learning + FastAPI + Docker + Kubernetes** project that predicts product prices using a **Random Forest Regressor** and deploys the model as a scalable API.

---

## 🚀 Tech Stack

### Machine Learning
- Scikit-Learn  
- Random Forest Regressor  
- Label Encoding  
- Pandas, NumPy  
- Joblib (for saving/loading models)

### Backend
- FastAPI  
- Uvicorn  

### DevOps / MLOps
- Docker  
- Kubernetes (Kind Cluster)  
- NodePort Service  
- Deployment with multiple replicas  

---

## 📁 Project Structure

```
smart-price-predictor/
│
├── data/
│   ├── train_products.csv
│   └── test_products.csv
│
├── models/
│   ├── price_model.pkl
│   ├── brand_encoder.pkl
│   └── category_encoder.pkl
│
├── app/
│   ├── main.py
│   ├── model_loader.py
│   ├── schemas.py
│   └── requirements.txt
│
├── train_model.py
├── Dockerfile
├── k8s/
│   ├── deployment.yaml
│   └── service.yaml
└── README.md
```

---

## 📊 Dataset Schema

| Column     | Type    | Description |
|------------|---------|-------------|
| brand      | string  | Product brand |
| category   | string  | Product category |
| rating     | float   | Product rating |
| reviews    | int     | Number of reviews |
| quantity   | int     | Stock/units |
| price      | float   | **Target variable** |

---

## 🔄 ML Pipeline

```
CSV → Cleaning → Label Encoding → Train/Test Split → RandomForest → Evaluation → Save Model
```

### Run Training
```
python train_model.py
```

Outputs:
- MSE  
- RMSE  
- Saves model + encoders in /models

---

## 🌐 FastAPI Backend

### Run locally:
```
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

Swagger Docs:
```
http://localhost:8000/docs
```

### /predict Endpoint

POST /predict

Body:
```json
{
  "brand": "Samsung",
  "category": "Smartphone",
  "rating": 4.5,
  "reviews": 1200,
  "quantity": 1
}
```

Response:
```json
{
  "predicted_price": 24999.5
}
```

---

## 🐳 Docker Setup

### Build the image:
```
docker build -t smart-price-predictor .
```

### Run the container:
```
docker run -d -p 8000:8000 smart-price-predictor
```

Visit:
```
http://localhost:8000/docs
```

---

## ☸️ Kubernetes Deployment (Kind Cluster)

### Create Kind Cluster
```
kind create cluster --name my-cluster
```

### Deploy the App
```
kubectl apply -f k8s/deployment.yaml
kubectl apply -f k8s/service.yaml
```

### Check Status
```
kubectl get pods -o wide
kubectl get svc
```

Example output:
```
smart-price-predictor-service  NodePort  8000:30080/TCP
```

### Access the API
```
http://localhost:30080/docs
```

Alternative:
```
kubectl port-forward service/smart-price-predictor-service 8000:8000
```

---

## 🧱 System Architecture Diagram

```
                ┌─────────────────────────────┐
                │     Train Model (Python)     │
                │  RandomForest + Encoders     │
                └───────────────┬─────────────┘
                                │
                        Save to /models
                                │
                ┌───────────────▼──────────────┐
                │        FastAPI Backend        │
                │  Loads Model + Encoders       │
                └───────────────┬──────────────┘
                                │
                     Docker Container Build
                                │
                ┌───────────────▼──────────────┐
                │         Kubernetes            │
                │  Deployment (2 Replicas)      │
                │        NodePort Service       │
                └───────────────┬──────────────┘
                                │
                     External Client / Browser
                                │
                ┌───────────────▼──────────────┐
                │   http://localhost:30080      │
                │         /predict              │
                └───────────────────────────────┘
```

---

## 🔮 Future Enhancements

- CI/CD with GitHub Actions  
- Ingress instead of NodePort  
- Auto Docker builds & push to Docker Hub  
- MLflow for model tracking  
- Monitoring using Prometheus & Grafana  
- Frontend UI 

---

## 🏆 Why This Project?

This project demonstrates:

✔ ML Model Lifecycle  
✔ Production API (FastAPI)  
✔ Dockerization  
✔ Kubernetes Orchestration  
✔ Scaling with Deployments  

