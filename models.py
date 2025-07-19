from pydantic import BaseModel, Field, ConfigDict
from typing import List, Optional
from bson import ObjectId

# ---------------------------
# Product Schemas
# ---------------------------

class ProductCreate(BaseModel):
    name: str
    sizes: List[str]
    price: float
    description: Optional[str] = None


class ProductResponse(BaseModel):
    id: str = Field(alias="_id")
    name: str
    sizes: List[str]
    price: float
    description: Optional[str] = None  # <- Kept optional if some documents may omit it

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        json_encoders={ObjectId: str},
        extra="allow",
        json_schema_extra={
            "example": {
                "id": "60af8843e1234a5d6b789012",
                "name": "T-Shirt",
                "sizes": ["S", "M", "L"],
                "price": 19.99,
                "description": "Comfortable cotton t-shirt"
            }
        }
    )

# ---------------------------
# Order Schemas
# ---------------------------

class OrderItem(BaseModel):
    product_id: str
    quantity: int
    size: str


class OrderCreate(BaseModel):
    user_id: str
    items: List[OrderItem]


class OrderResponse(BaseModel):
    id: str = Field(alias="_id")
    user_id: str
    items: List[OrderItem]

    model_config = ConfigDict(
        populate_by_name=True,
        from_attributes=True,
        json_encoders={ObjectId: str},
        extra="allow",
        json_schema_extra={
            "example": {
                "id": "60af891be1234a5d6b789013",
                "user_id": "user123",
                "items": [
                    {
                        "product_id": "60af8843e1234a5d6b789012",
                        "quantity": 2,
                        "size": "M"
                    }
                ]
            }
        }
    )
