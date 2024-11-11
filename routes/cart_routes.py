from fastapi import APIRouter, Depends
from routes.auth_routes import get_token
from utils.forward import forward_request

router = APIRouter()

@router.post("/add")
def add_item(data: dict, token: str = Depends(get_token)):
    return forward_request("cart_service", "/cart/add", method="POST", token=token, json=data)

@router.post("/remove")
def remove_item(data: dict, token: str = Depends(get_token)):
    return forward_request("cart_service", "/cart/remove", method="POST", token=token, json=data)

@router.get("/list")
def list_cart(token: str = Depends(get_token)):
    return forward_request("cart_service", "/cart/list", token=token)