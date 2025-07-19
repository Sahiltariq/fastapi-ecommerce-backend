import os
from typing import List, Optional
from fastapi import FastAPI, status, HTTPException
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv
from bson import ObjectId
from models import ProductCreate, ProductResponse, OrderCreate, OrderResponse

# ------------------- ENV + MongoDB Setup -------------------

load_dotenv()

app = FastAPI()

MONGO_URI = os.getenv("MONGODB_URI")
if not MONGO_URI:
    raise Exception("MONGODB_URI not found in .env")

client = AsyncIOMotorClient(
    MONGO_URI,
    tls=True,
    tlsAllowInvalidCertificates=True  # Avoid this in production
)

db = client["ecommerce_db"]
products_col = db["products"]
orders_col = db["orders"]

# ---------------------------- PRODUCTS ----------------------------

@app.post("/products", response_model=ProductResponse, status_code=status.HTTP_201_CREATED)
async def create_product(product: ProductCreate):
    try:
        result = await products_col.insert_one(product.model_dump())
        created = await products_col.find_one({"_id": result.inserted_id})
        if not created:
            raise HTTPException(status_code=500, detail="Failed to fetch created product")

        created["_id"] = str(created["_id"])
        return ProductResponse(**created).model_dump(by_alias=True)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Product creation error: {str(e)}")

@app.get("/products", response_model=List[ProductResponse])
async def list_products(
    name: Optional[str] = None,
    size: Optional[str] = None,
    limit: int = 10,
    offset: int = 0
):
    try:
        query = {}
        if name:
            query["name"] = {"$regex": name, "$options": "i"}
        if size:
            query["sizes"] = {"$in": [size]}

        cursor = products_col.find(query).skip(offset).limit(limit)
        products = []
        async for doc in cursor:
            doc["_id"] = str(doc["_id"])
            products.append(ProductResponse(**doc).model_dump(by_alias=True))
        return products

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Product listing error: {str(e)}")

# ---------------------------- ORDERS ----------------------------

@app.post("/orders", response_model=OrderResponse, status_code=status.HTTP_201_CREATED)
async def create_order(order: OrderCreate):
    try:
        order_data = order.model_dump()

        for item in order_data["items"]:
            item["product_id"] = ObjectId(item["product_id"])

        result = await orders_col.insert_one(order_data)
        created = await orders_col.find_one({"_id": result.inserted_id})
        if not created:
            raise HTTPException(status_code=500, detail="Failed to fetch created order")

        created["_id"] = str(created["_id"])
        for item in created["items"]:
            item["product_id"] = str(item["product_id"])

        return OrderResponse(**created).model_dump(by_alias=True)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Order creation error: {str(e)}")

@app.get("/orders/{user_id}", response_model=List[OrderResponse])
async def list_orders(user_id: str, limit: int = 10, offset: int = 0):
    try:
        cursor = orders_col.find({"user_id": user_id}).skip(offset).limit(limit)
        orders = []
        async for doc in cursor:
            doc["_id"] = str(doc["_id"])
            for item in doc["items"]:
                item["product_id"] = str(item["product_id"])
            orders.append(OrderResponse(**doc).model_dump(by_alias=True))
        return orders

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Order listing error: {str(e)}")
