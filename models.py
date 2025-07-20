from pydantic import BaseModel, Field
from typing import List, Optional

class ProductModel(BaseModel):
    name: str
    price: float
    description: Optional[str] = None
    size: Optional[str] = None

class OrderModel(BaseModel):
    user_id: str
    product_ids: List[str]
