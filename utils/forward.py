import requests
from fastapi import HTTPException
from config import MICROSERVICE_URLS
import pybreaker

circuit_breaker = pybreaker.CircuitBreaker(fail_max=5,
                                            reset_timeout=30)

def forward_request(service_name: str, path: str, method: str = "GET", token: str = None, json: dict = None):
    base_url = MICROSERVICE_URLS.get(service_name)
    if not base_url:
        raise HTTPException(status_code=500, detail="Service URL not found")

    headers = {"Authorization": f"Bearer {token}"} if token else {}
    url = f"{base_url}{path}"
    
    try:
        response = circuit_breaker.call(requests.request, method=method, url=url, headers=headers, json=json)
        
        if response.status_code not in [200, 201]:
            detail = response.text
            raise HTTPException(status_code=response.status_code, detail=detail)
        
        if not response.content:
            raise HTTPException(status_code=204, detail="No content returned from the service")
        
        try:
            return response.json()
        except ValueError:
            raise HTTPException(status_code=500, detail="Response is not valid JSON")
    
    except requests.RequestException as e:
        raise HTTPException(status_code=500, detail=f"Request to {url} failed: {str(e)}")
    except pybreaker.CircuitBreakerError:
        raise HTTPException(status_code=503, detail="Service is temporarily unavailable. Please try again later.")