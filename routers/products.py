from fastapi import APIRouter, Query, status
from models import ProductModel
from database import products_collection
from bson import ObjectId
import re

router = APIRouter()

@router.post("/products", status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductModel):
    result = await products_collection.insert_one(product.dict())
    return {"id": str(result.inserted_id)}

@router.get("/products")
async def list_products(
    name: str = None,
    size: str = None,
    limit: int = 10,
    offset: int = 0
):
    query = {}
    if name:
        query["name"] = {"$regex": re.escape(name), "$options": "i"}
    if size:
        query["size"] = size

    products = await products_collection.find(query).skip(offset).limit(limit).to_list(length=limit)
    for product in products:
        product["id"] = str(product["_id"])
        del product["_id"]
    return products
