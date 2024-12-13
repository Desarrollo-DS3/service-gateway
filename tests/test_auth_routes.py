from fastapi.testclient import TestClient
from unittest.mock import patch
from main import app  

client = TestClient(app)


@patch("routes.auth_routes.forward_request")
def test_login(mock_forward_request):
   
    mock_forward_request.return_value = "mocked_token"

    # Enviar una solicitud POST a la ruta de login
    response = client.post(
        "/api/auth/login",  
        json={"username": "testuser", "password": "testpassword"}
    )

    # Verificar que la respuesta sea correcta
    assert response.status_code == 200
    assert response.json() == {
        "access_token": "mocked_token",
        "token_type": "bearer"
    }

    # Verificar que `forward_request` fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "auth_service", "/login", method="POST", json={"username": "testuser", "password": "testpassword"}
    )

@patch("routes.auth_routes.forward_request")
def test_register_user(mock_forward_request):
    
    mock_forward_request.return_value = {"message": "User registered successfully"}

    # Enviar una solicitud POST al endpoint de registrar usuario
    response = client.post(
        "/api/auth/register/user",
        json={"username": "newuser", "password": "newpassword123"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "User registered successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "auth_service", "/register/user", method="POST", json={"username": "newuser", "password": "newpassword123"}
    )

@patch("routes.auth_routes.forward_request")
def test_register_warehouse_assistant(mock_forward_request):
    
    mock_forward_request.return_value = {"message": "Warehouse assistant registered successfully"}

    # Enviar una solicitud POST al endpoint de registrar asistente de almacén
    response = client.post(
        "/api/auth/register/warehouse-assistant",
        json={"username": "assistantuser", "password": "assistantpassword123"}
    )

    # Verificar que la respuesta sea la esperada
    assert response.status_code == 200
    assert response.json() == {"message": "Warehouse assistant registered successfully"}

    # Verificar que forward_request fue llamado correctamente
    mock_forward_request.assert_called_once_with(
        "auth_service", "/register/warehouse-assistant", method="POST", json={"username": "assistantuser", "password": "assistantpassword123"}
    )