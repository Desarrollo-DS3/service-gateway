from fastapi import APIRouter, Depends
from routes.auth_routes import get_token
from utils.forward import forward_request

router = APIRouter()

@router.post("/brand/create")
def add_item(data: dict, token: str = Depends(get_token)):
    return forward_request("stock_service", "/brand/create", method="POST", token=token, json=data)

@router.post("/category/create")
def add_item(data: dict, token: str = Depends(get_token)):
    return forward_request("stock_service", "/category/create", method="POST", token=token, json=data)

@router.post("/product/add")
def add_item(data: dict, token: str = Depends(get_token)):
    return forward_request("stock_service", "/product/add", method="POST", token=token, json=data)

@router.get("/brand/list")
def list_brands(token: str = Depends(get_token)):
    return forward_request("stock_service", "/brand/list", token=token)

@router.get("/category/list")
def list_categories(token: str = Depends(get_token)):
    return forward_request("stock_service", "/category/list", token=token)

@router.get("/product/list")
def list_products(token: str = Depends(get_token)):
    return forward_request("stock_service", "/product/list", token=token)

@router.post("/product/supply")
def supply_product(data: dict, token: str = "asdf"):
    return forward_request("stock_service", "/product/supply", method="POST", token=token, json=data)