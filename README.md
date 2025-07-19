# 🛍️ E-commerce API (FastAPI + MongoDB)

A simple e-commerce backend with RESTful APIs for managing products and orders. Built using **FastAPI**, **MongoDB**, and **Motor** (async MongoDB driver).

---

## 📦 Project Overview

This API allows you to:

- Add and list products (with filters)
- Create orders
- Get a user's order history (with pagination)

**Tech Stack:**
- FastAPI (Python backend)
- MongoDB (NoSQL database)
- Motor (Async MongoDB client)
- Pydantic (for data validation)

---

## ⚙️ Setup Instructions

### 1. Clone the repository
```bash
git clone https://github.com/Sahiltariq/fastapi-ecommerce-backend.git
cd fastapi-ecommerce-backend
2. Create a virtual environment

python -m venv venv
# Activate virtual environment:
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
3. Install dependencies
pip install -r requirements.txt
4. Create a .env file
Add the following to .env in your project root:
MONGODB_URI=mongodb+srv://ruhaansahil443:3u1BGw9tA8h6Ikj5@cluster0.0znzg8z.mongodb.net/ecommerce_db?retryWrites=true&w=majority&tls=true
5. Run the development server
uvicorn main:app --reload

6. Explore the API docs:
Swagger UI: http://127.0.0.1:8000/docs

ReDoc: http://127.0.0.1:8000/redoc

📡 API Endpoints
🧾 POST /products
Create a new product
Body:

json
Copy
Edit
{
  "name": "T-Shirt",
  "sizes": ["S", "M", "L"],
  "price": 19.99,
  "description": "Cotton tee"
}
Response: 201 Created

📃 GET /products
List products with optional filters
Query Parameters:

name — partial match (case-insensitive)

size — matches any in sizes array

limit — max results (default: 10)

offset — skip results (default: 0)

Example:

http
Copy
Edit
GET /products?name=shirt&size=M&limit=5&offset=0
🛒 POST /orders
Create a new order
Body:

json
Copy
Edit
{
  "user_id": "user123",
  "items": [
    {"product_id": "687b359206a619e7a6142de9", "quantity": 2, "size": "M"}
  ]
}
Response: 201 Created

📦 GET /orders/{user_id}
Get all orders for a specific user
Example:

http
Copy
Edit
GET /orders/user123?limit=10&offset=0
🧪 Example curl Commands
bash
Copy
Edit
# Create a product
curl -X POST http://127.0.0.1:8000/products ^
  -H "Content-Type: application/json" ^
  -d "{\"name\": \"T-Shirt\", \"sizes\": [\"S\", \"M\", \"L\"], \"price\": 19.99, \"description\": \"Cotton tee\"}"

# List products
curl "http://127.0.0.1:8000/products?name=shirt&size=M"

# Create an order
curl -X POST http://127.0.0.1:8000/orders ^
  -H "Content-Type: application/json" ^
  -d "{\"user_id\": \"user123\", \"items\": [{\"product_id\": \"687b359206a619e7a6142de9\", \"quantity\": 2, \"size\": \"M\"}]}"
🚀 Deployment Notes
🟪 Render (Web Service)
Push your repo to GitHub (already done ✅)

Go to render.com

Create new Web Service → Connect GitHub

Set:

Build Command: pip install -r requirements.txt

Start Command: uvicorn main:app --host 0.0.0.0 --port $PORT

Set environment variable:

MONGODB_URI = your MongoDB Atlas URI
📬 Contact
Have questions?
Reach out via 📧 ruhansahil4361@gmail.com or open an issue.
