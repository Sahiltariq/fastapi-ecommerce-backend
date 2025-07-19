E-commerce API (FastAPI + MongoDB)
📦 Project Overview
This is a basic e-commerce backend built with FastAPI and MongoDB (Atlas). It supports:

CRUD operations for products

Placing and fetching orders by user

Filtering and pagination

Hosted on Render

⚙️ Setup Instructions
bash
Copy
Edit
# Clone the repository
git clone https://github.com/yourusername/fastapi-ecommerce-backend.git
cd fastapi-ecommerce-backend

# Create and activate a virtual environment
python -m venv venv
source venv/bin/activate  # use `venv\Scripts\activate` on Windows

# Install dependencies
pip install -r requirements.txt
Create a .env file in the root directory:
ini
Copy
Edit
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/ecommerce_db
Run the app locally:
bash
Copy
Edit
uvicorn main:app --reload
🚀 Deployment Notes
▶️ Using Render
Build command:

bash
Copy
Edit
pip install -r requirements.txt
Start command:

bash
Copy
Edit
uvicorn main:app --host 0.0.0.0 --port $PORT
Environment Variables:

MONGODB_URI=mongodb+srv://ruhaansahil443:3u1BGw9tA8h6Ikj5@cluster0.0znzg8z.mongodb.net/ecommerce_db?retryWrites=true&w=majority&tls=true

Deployed URL:
🔗 https://fastapi-ecommerce-backend-1.onrender.com

📡 API Endpoints
✅ POST /products
json
Copy
Edit
{
  "name": "T-Shirt",
  "sizes": ["S", "M"],
  "price": 19.99,
  "description": "Cotton tee"
}
✅ GET /products?name=shirt&size=M&limit=5&offset=0
✅ POST /orders
json
Copy
Edit
{
  "user_id": "user123",
  "items": [
    {
      "product_id": "abc123",
      "quantity": 2,
      "size": "M"
    }
  ]
}
✅ GET /orders/{user_id}?limit=10&offset=0
🧪 Example curl Commands
bash
Copy
Edit
# List products
curl https://fastapi-ecommerce-backend-1.onrender.com/products

# Create a product
curl -X POST https://fastapi-ecommerce-backend-1.onrender.com/products \
  -H "Content-Type: application/json" \
  -d '{"name":"T-Shirt","sizes":["M"],"price":19.99,"description":"Cotton tee"}'

# Place an order
curl -X POST https://fastapi-ecommerce-backend-1.onrender.com/orders \
  -H "Content-Type: application/json" \
  -d '{"user_id":"user123","items":[{"product_id":"abc123","quantity":1,"size":"M"}]}'
