# 🚗 CarCharcha - Car Price Prediction API

<div align="center">

**A powerful machine learning API for predicting car prices with enterprise-grade features**

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)](https://www.python.org/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.110-green?logo=fastapi)](https://fastapi.tiangolo.com/)
[![Docker](https://img.shields.io/badge/Docker-Ready-blue?logo=docker)](https://www.docker.com/)

</div>

---

## 📋 Overview

CarCharcha is a production-ready **REST API** that predicts car prices using advanced machine learning models. Built with FastAPI, it provides:

- ✅ **Intelligent Price Prediction** - LightGBM & Scikit-learn based ML models
- ✅ **Secure Authentication** - JWT-based API key authentication
- ✅ **High Performance** - Redis caching for optimized responses
- ✅ **Production Monitoring** - Prometheus metrics integration
- ✅ **Containerized Deployment** - Docker & Docker Compose ready
- ✅ **Comprehensive Logging** - Request tracking and error handling

---

## 📊 About the Dataset

### 📈 Dataset Overview

**CarCharcha** is trained on a comprehensive Indian used car market dataset containing real-world pricing data.

#### Dataset Characteristics

- **Source**: Indian used car market (`car-details.csv`)
- **Records**: 4,000+ car listings
- **Time Period**: 2003-2020
- **Target Variable**: Selling price (₹ INR)
- **Price Range**: ₹ 1 Lakh to ₹ 1 Crore+
- **Data Quality**: Cleaned and preprocessed with minimal missing values

#### Data Distribution

- **Cars by Company**: 30+ manufacturers including Maruti, Hyundai, Honda, Tata, Mahindra, etc.
- **Manufacturing Years**: 2003-2020 (17 years of data)
- **Fuel Types**: Petrol (55%), Diesel (40%), CNG (5%)
- **Transmission Types**: Manual (70%), Automatic (30%)
- **Ownership**: First (60%), Second (30%), Third+ (10%)
- **Seller Types**: Individual (80%), Dealer (20%)

### Features Used

1. `company` - Car manufacturer (30+ brands)
2. `year` - Manufacturing year (2003-2020)
3. `owner` - Previous owner count (1st, 2nd, 3rd+)
4. `fuel` - Fuel type (Petrol/Diesel/CNG)
5. `seller_type` - Dealer or Individual seller
6. `transmission` - Manual/Automatic transmission
7. `km_driven` - Kilometers driven (0-5,000,000 km)
8. `mileage_mpg` - Fuel efficiency (10-40 MPG)
9. `engine_cc` - Engine displacement (700-5000 cc)
10. `max_power_bhp` - Power output (30-500 bhp)
11. `torque_nm` - Torque specification (50-500 nm)
12. `seats` - Number of seats (2-8)

---

## 🎯 Features

### 🤖 Machine Learning

- Pre-trained model (`model.joblib`) trained on comprehensive car dataset
- Predicts prices based on 13 car attributes
- Uses log transformation for better prediction accuracy
- Built with LightGBM for superior performance

### 🔐 Security & Authentication

- JWT token-based authentication
- API key validation
- Secure dependency injection pattern
- User-based access control

### ⚡ Performance & Caching

- Redis cache integration for frequently requested predictions
- Fast response times with optimized model inference
- Batch prediction support ready

### 📊 Monitoring & Observability

- Prometheus metrics exposure at `/metrics`
- Structured logging middleware
- Request/response tracking
- Performance monitoring

---

## 🛠️ Tech Stack

| Component            | Technology             |
| -------------------- | ---------------------- |
| **Framework**        | FastAPI 0.110          |
| **Web Server**       | Uvicorn                |
| **ML Models**        | LightGBM, Scikit-learn |
| **Caching**          | Redis                  |
| **Monitoring**       | Prometheus             |
| **Authentication**   | JWT (PyJWT)            |
| **Containerization** | Docker, Docker Compose |

---

## 📦 Installation

### Prerequisites

- Python 3.8+
- Docker & Docker Compose (optional)
- Redis (optional, for caching)

### Local Setup

1. **Clone the repository**

```bash
git clone <repository-url>
cd CarCharcha
```

2. **Create virtual environment**

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**

```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

```bash
cp .env.example .env
# Edit .env with your configuration
```

---

## 🐳 Docker Deployment

### Quick Start with Docker Compose

```bash
docker-compose up -d
```

This starts:

- FastAPI application on `http://localhost:8000`
- Prometheus monitoring on `http://localhost:9090`
- Redis cache (if configured)

### Manual Docker Build

```bash
docker build -t carchercha:latest .
docker run -p 8000:8000 carchercha:latest
```

---

## 🚀 Usage

### Start the API

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`

### Interactive API Documentation

- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Authentication

Obtain a JWT token via the `/auth` endpoint, then include it in requests:

```bash
Authorization: Bearer <your_jwt_token>
```

### Prediction Endpoint

**POST** `/predict`

**Request Body:**

```json
{
  "company": "Toyota",
  "year": 2020,
  "owner": "First",
  "fuel": "Petrol",
  "seller_type": "Individual",
  "transmission": "Manual",
  "km_driven": 50000,
  "mileage_mpg": 18.5,
  "engine_cc": 1500,
  "max_power_bhp": 110,
  "torque_nm": 140,
  "seats": 5
}
```

**Response:**

```json
{
  "predicted_price": "8,50,000.00"
}
```

---

## 📁 Project Structure

```
CarCharcha/
├── app/
│   ├── main.py                 # FastAPI application entry point
│   ├── __init__.py
│   ├── api/
│   │   ├── routes_auth.py      # Authentication endpoints
│   │   └── routes_predict.py   # Prediction endpoints
│   ├── core/
│   │   ├── config.py           # Configuration management
│   │   ├── dependencies.py     # Dependency injection
│   │   ├── exceptions.py       # Custom exceptions
│   │   └── security.py         # Security utilities
│   ├── middleware/
│   │   └── logging_middleware.py
│   ├── models/
│   │   └── model.joblib        # Trained ML model
│   ├── cache/
│   │   └── redis_cache.py      # Caching logic
│   └── services/
│       └── model_service.py    # Model inference service
├── training/
│   ├── train_model.py          # Model training script
│   ├── train_utils.py          # Training utilities
│   └── __init__.py
├── data/
│   └── car-details.csv         # Training dataset
├── notebooks/
│   └── sample1.ipynb           # EDA & analysis notebook
├── docker-compose.yml          # Multi-container configuration
├── Dockerfile                  # Container image definition
├── prometheus.yml              # Prometheus configuration
├── requirements.txt            # Python dependencies
└── README.md
```

---

## 🔧 Configuration

### Environment Variables

Create a `.env` file:

```env
# API Configuration
API_TITLE=Car Price Prediction API
DEBUG=False

# Security
SECRET_KEY=your-secret-key-here
ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=30

# Redis Cache
REDIS_URL=redis://localhost:6379/0
CACHE_ENABLED=True

# Database
DATABASE_URL=your-database-url

# Logging
LOG_LEVEL=INFO
```

---

## 📈 Monitoring

### Prometheus Metrics

Access metrics at: http://localhost:9090

**Key Metrics:**

- Request count & latency
- Error rates
- Model inference time
- Cache hit/miss ratio

### Health Check

```bash
curl http://localhost:8000/health
```

---

## 🧪 Testing

Run tests with pytest:

```bash
pytest tests/ -v
```

---

## 🤝 Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 API Examples

### Example: Predict car price

```python
import requests
import json

url = "http://localhost:8000/predict"
headers = {
    "Authorization": "Bearer <your_token>",
    "Content-Type": "application/json"
}

data = {
    "company": "Maruti",
    "year": 2019,
    "owner": "First",
    "fuel": "Petrol",
    "seller_type": "Individual",
    "transmission": "Manual",
    "km_driven": 80000,
    "mileage_mpg": 23.4,
    "engine_cc": 1200,
    "max_power_bhp": 82,
    "torque_nm": 113,
    "seats": 5
}

response = requests.post(url, json=data, headers=headers)
print(response.json())
```

---

## 🐛 Troubleshooting

### Common Issues

**Issue**: `Redis connection failed`

- **Solution**: Ensure Redis is running or disable caching in `.env`

**Issue**: `Model file not found`

- **Solution**: Retrain the model using `python training/train_model.py`

**Issue**: `Authentication failed`

- **Solution**: Verify JWT token validity and SECRET_KEY configuration

---

## 🚀 Future Scope

### Planned Enhancements

| Category          | Features                                                                                |
| ----------------- | --------------------------------------------------------------------------------------- |
| **ML Models**     | Ensemble methods (XGBoost), Model versioning & A/B testing, Model explainability (SHAP) |
| **API & Backend** | Batch prediction, Kubernetes deployment, Model drift detection                          |
| **Frontend**      | Web dashboard, Mobile app (iOS/Android), Price comparison tool                          |
| **Data**          | Multi-region support, Real-time data ingestion, Historical price tracking               |
| **Business**      | Insurance estimation, Depreciation forecasting, Market reports                          |

---

<div align="center">

**Made with ❤️ for the automotive industry**

</div>
