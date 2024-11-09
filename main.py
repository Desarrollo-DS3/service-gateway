from fastapi import FastAPI
from config import API_PREFIX
from routes.auth_routes import router as auth_router
from routes.stock_routes import router as stock_router
from routes.cart_routes import router as cart_router
from routes.transaction_routes import router as transaction_router

app = FastAPI()

app.include_router(auth_router, prefix=f"{API_PREFIX}/auth")
app.include_router(stock_router, prefix=f"{API_PREFIX}/stock")
app.include_router(cart_router, prefix=f"{API_PREFIX}/cart")
app.include_router(transaction_router, prefix=f"{API_PREFIX}/transaction")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
