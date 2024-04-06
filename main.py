from fastapi import FastAPI
from pydantic import BaseModel
from utils import generate_description
from utils2 import generate_prescription

# Initialize FastAPI
app = FastAPI()

# Define your data model for product
class Order(BaseModel):
    product: str
    units: int

class Product(BaseModel):
    name: str
    notes: str
    
class Product1(BaseModel):
    name: str
    notes: str


@app.get("/ok")
async def ok_endpoint():
    return {"message": "ok"}

@app.get("/hello")
async def hello_endpoint(name: str = "world"):
    return {"message": f"Hello, {name}!"}

    # post request via the query string of the request
@app.post("/orders")
async def place_orders(product: str, units: int):   # query parameters
    return {"message": f"Order for {units} units of {product} placed successfully"}

    # post request via the body of the request
@app.post("/orders_pydantic")
async def place_orders(order: Order):   # request body
   return {"message": f"Order for {order.units} units of {order.product} placed successfully"}


@app.post("/product_description")
async def generate_product_description(product: Product):
    description = generate_description(f"Disease name: {product.name}, Notes: {product.notes}")
    return {"product_description": description}

@app.post("/prescription")
async def generate_product_prescription(productt: Product1):
    description1 = generate_prescription(f"Prescription: {productt.name}, Notes: {productt.notes}")
    return {"prescription": description1}