from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

@patch("routes.stock_routes.forward_request")
def test_add_brand(mock_forward_request):
    
    mock_forward_request.return_value = {"message": "Brand created successfully"}

    # Enviar una solicitud POST al endpoint de crear marca
    response = client.post(
        "/api/stock/brand/create",
        headers={"Authorization": "Bearer testtoken"},
        json={"brand_name": "NewBrand"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "Brand created successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "stock_service", "/brand/create", method="POST", token="testtoken", json={"brand_name": "NewBrand"}
    )

@patch("routes.stock_routes.forward_request")
def test_add_category(mock_forward_request):
    
    mock_forward_request.return_value = {"message": "Category created successfully"}

    # Enviar una solicitud POST al endpoint de crear categoría
    response = client.post(
        "/api/stock/category/create",
        headers={"Authorization": "Bearer testtoken"},
        json={"category_name": "NewCategory"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "Category created successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "stock_service", "/category/create", method="POST", token="testtoken", json={"category_name": "NewCategory"}
    )

@patch("routes.stock_routes.forward_request")
def test_add_product(mock_forward_request):
    
    mock_forward_request.return_value = {"message": "Product added successfully"}

    # Enviar una solicitud POST al endpoint de agregar producto
    response = client.post(
        "/api/stock/product/add",
        headers={"Authorization": "Bearer testtoken"},
        json={"product_name": "NewProduct", "brand_id": 1, "category_id": 2, "price": 100}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "Product added successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "stock_service", "/product/create", method="POST", token="testtoken", json={
            "product_name": "NewProduct", "brand_id": 1, "category_id": 2, "price": 100
        }
    )

@patch("routes.stock_routes.forward_request")
def test_list_brands(mock_forward_request):
    
    mock_forward_request.return_value = {
        "brands": [
            {"brand_id": 1, "name": "Brand1"},
            {"brand_id": 2, "name": "Brand2"}
        ]
    }

    # Enviar una solicitud GET al endpoint de listar marcas
    response = client.get(
        "/api/stock/brand/list",
        headers={"Authorization": "Bearer testtoken"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {
        "brands": [
            {"brand_id": 1, "name": "Brand1"},
            {"brand_id": 2, "name": "Brand2"}
        ]
    }

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "stock_service", "/brand/list", token="testtoken"
    )

@patch("routes.stock_routes.forward_request")
def test_list_categories(mock_forward_request):
    
    mock_forward_request.return_value = {
        "categories": [
            {"category_id": 1, "name": "Category1"},
            {"category_id": 2, "name": "Category2"}
        ]
    }

    # Enviar una solicitud GET al endpoint de listar categorías
    response = client.get(
        "/api/stock/category/list",
        headers={"Authorization": "Bearer testtoken"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {
        "categories": [
            {"category_id": 1, "name": "Category1"},
            {"category_id": 2, "name": "Category2"}
        ]
    }

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "stock_service", "/category/list", token="testtoken"
    )

@patch("routes.stock_routes.forward_request")
def test_list_products(mock_forward_request):
    
    mock_forward_request.return_value = {
        "products": [
            {"product_id": 1, "name": "Product1", "price": 100},
            {"product_id": 2, "name": "Product2", "price": 150}
        ]
    }

    # Enviar una solicitud GET al endpoint de listar productos
    response = client.get(
        "/api/stock/product/list",
        headers={"Authorization": "Bearer testtoken"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {
        "products": [
            {"product_id": 1, "name": "Product1", "price": 100},
            {"product_id": 2, "name": "Product2", "price": 150}
        ]
    }

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "stock_service", "/product/list", token="testtoken"
    )

@patch("routes.stock_routes.forward_request")
def test_get_product(mock_forward_request):
    
    mock_forward_request.return_value = {"product_id": 1, "name": "Product1", "price": 100}

    # Enviar una solicitud GET al endpoint de obtener producto por ID
    response = client.get(
        "/api/stock/product/get/1",
        headers={"Authorization": "Bearer testtoken"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"product_id": 1, "name": "Product1", "price": 100}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "stock_service", "/product/get/1", token="testtoken"
    )

@patch("routes.stock_routes.forward_request")
def test_supply_product(mock_forward_request):
    
    mock_forward_request.return_value = {"message": "Product supplied successfully"}

    # Enviar una solicitud POST al endpoint de suministrar producto
    response = client.post(
        "/api/stock/product/supply",
        headers={"Authorization": "Bearer testtoken"},
        json={"product_id": 1, "quantity": 50}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "Product supplied successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "stock_service", "/product/supply", method="POST", token="testtoken", json={"product_id": 1, "quantity": 50}
    )

@patch("routes.stock_routes.forward_request")
def test_buy_product(mock_forward_request):
    
    mock_forward_request.return_value = {"message": "Product purchased successfully"}

    # Enviar una solicitud POST al endpoint de comprar producto
    response = client.post(
        "/api/stock/product/buy",
        headers={"Authorization": "Bearer testtoken"},
        json={"product_id": 1, "quantity": 30}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "Product purchased successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "stock_service", "/product/buy", method="POST", token="testtoken", json={"product_id": 1, "quantity": 30}
    )