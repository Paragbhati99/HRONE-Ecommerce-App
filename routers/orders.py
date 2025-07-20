from fastapi import APIRouter, status
from models import OrderModel
from database import orders_collection
from bson import ObjectId

router = APIRouter()

@router.post("/orders", status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderModel):
    result = await orders_collection.insert_one(order.dict())
    return {"id": str(result.inserted_id)}

@router.get("/orders/{user_id}")
async def get_orders(user_id: str, limit: int = 10, offset: int = 0):
    query = {"user_id": user_id}
    orders = await orders_collection.find(query).skip(offset).limit(limit).to_list(length=limit)
    for order in orders:
        order["id"] = str(order["_id"])
        del order["_id"]
    return orders
