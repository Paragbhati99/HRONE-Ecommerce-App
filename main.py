'''from fastapi import FastAPI
from routers import products, orders

app = FastAPI()

app.include_router(products.router)
app.include_router(orders.router)'''


import webbrowser
from fastapi import FastAPI
from routers import products, orders

app = FastAPI()

app.include_router(products.router)
app.include_router(orders.router)

# Open Swagger Docs when app starts
@app.on_event("startup")
async def startup_event():
    webbrowser.open("http://127.0.0.1:8000/docs")
print("Swagger Docs opened in default browser")