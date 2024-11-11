from config import MICROSERVICE_URLS
from fastapi import APIRouter, Header, HTTPException
from utils.forward import forward_request

router = APIRouter()
AUTH_SERVICE_URL = MICROSERVICE_URLS["auth_service"]

def get_token(authorization: str = Header(...)):
    if not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Invalid token format")
    return authorization.split(" ")[1] 

@router.post("/login")
def login(data: dict):
    token = forward_request("auth_service", "/login", method="POST", json=data)
    return {"access_token": token, "token_type": "bearer"}

@router.post("/register/user")
def register(data: dict):
    return forward_request("auth_service", "/register/user", method="POST", json=data)

@router.post("/register/warehouse-assistant")
def register(data: dict):
    return forward_request("auth_service", "/register/warehouse-assistant", method="POST", json=data)