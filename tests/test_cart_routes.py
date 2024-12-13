from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

@patch("routes.cart_routes.forward_request")
def test_add_item(mock_forward_request):
   
    mock_forward_request.return_value = {"message": "Item added successfully"}

    # Enviar una solicitud POST al endpoint de agregar item
    response = client.post(
        "/api/cart/add",
        headers={"Authorization": "Bearer testtoken"},
        json={"item_id": 1, "quantity": 2}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "Item added successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "cart_service", "/cart/add", method="POST", token="testtoken", json={"item_id": 1, "quantity": 2}
    )

@patch("routes.cart_routes.forward_request")
def test_remove_item(mock_forward_request):
   
    mock_forward_request.return_value = {"message": "Item removed successfully"}

    # Enviar una solicitud POST al endpoint de remover item
    response = client.post(
        "/api/cart/remove",
        headers={"Authorization": "Bearer testtoken"},
        json={"item_id": 1}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "Item removed successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "cart_service", "/cart/remove", method="POST", token="testtoken", json={"item_id": 1}
    )

@patch("routes.cart_routes.forward_request")
def test_list_cart(mock_forward_request):
    
    mock_forward_request.return_value = {
        "items": [
            {"item_id": 1, "name": "Item1", "quantity": 2},
            {"item_id": 2, "name": "Item2", "quantity": 1}
        ]
    }

    # Enviar una solicitud GET al endpoint de listar el carrito
    response = client.get(
        "/api/cart/list",
        headers={"Authorization": "Bearer testtoken"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {
        "items": [
            {"item_id": 1, "name": "Item1", "quantity": 2},
            {"item_id": 2, "name": "Item2", "quantity": 1}
        ]
    }

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "cart_service", "/cart/list", token="testtoken"
    )
