from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app

client = TestClient(app)

@patch("routes.transaction_routes.forward_request")
def test_buy(mock_forward_request):
    
    mock_forward_request.return_value = {"message": "Product bought successfully"}

    # Enviar una solicitud POST al endpoint de compra
    response = client.post(
        "/api/transaction/buy",
        headers={"Authorization": "Bearer testtoken"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "Product bought successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "transaction_service", "/transaction/buy", method="POST", token="testtoken"
    )

@patch("routes.transaction_routes.forward_request")
def test_supply(mock_forward_request):
    
    mock_forward_request.return_value = {"message": "Product supplied successfully"}

    # Enviar una solicitud POST al endpoint de suministro
    response = client.post(
        "/api/transaction/supply",
        headers={"Authorization": "Bearer testtoken"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "Product supplied successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "transaction_service", "/transaction/supply", method="POST", token="testtoken"
    )