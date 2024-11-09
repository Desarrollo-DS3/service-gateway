from fastapi import APIRouter, Depends
from routes.auth_routes import get_token
from utils.forward import forward_request

router = APIRouter()

@router.post("/buy")
def add_item(token: str = Depends(get_token)):
    return forward_request("transaction_service", "/transaction/buy", method="POST", token=token)

@router.post("/supply")
def add_item(token: str = Depends(get_token)):
    return forward_request("transaction_service", "/transaction/supply", method="POST", token=token)