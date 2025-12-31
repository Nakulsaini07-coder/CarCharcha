from fastapi import APIRouter, Depends
from pydantic import BaseModel
import numpy as np
from app.core.dependencies import get_current_user, get_api_key
from app.services.model_service import predict_car_price

router = APIRouter()

class CarFeatures(BaseModel):
    company: str
    year: int
    owner: str
    fuel: str
    seller_type: str
    transmission: str
    km_driven: float
    mileage_mpg: float
    engine_cc: float
    max_power_bhp: float
    torque_nm: float
    seats: float


@router.post('/predict')
def predict_price(car: CarFeatures, user=Depends(get_current_user), _=Depends(get_api_key)):
    log_prediction = predict_car_price(car.model_dump())    
    actual_prediction = float(np.expm1(log_prediction))
    return {'predicted_price': f'{actual_prediction:,.2f}'} 