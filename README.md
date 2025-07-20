
# 🛍️ FastAPI E-Commerce Backend

A simple e-commerce backend API built using **FastAPI**, **MongoDB (Atlas)**, and **Motor** (async MongoDB driver). This project was built as part of the **HROne Backend Intern Hiring Task**.

---

## 📦 Features

- ✅ Create a product
- ✅ List all products (with filtering & pagination)
- ✅ Create an order
- ✅ Get all orders for a user (with pagination)
- 🔗 Connected to MongoDB Atlas (cloud database)
- 🧩 Modular structure with routers
- 📄 Swagger UI for testing APIs

---

## 🚀 Tech Stack

- **Backend:** FastAPI
- **Database:** MongoDB Atlas
- **ODM:** Motor (async PyMongo)
- **Language:** Python 3.11+

---

## 🛠️ API Endpoints

### 📌 `POST /products`
Create a new product.
```json
{
  "name": "T-Shirt",
  "price": 499.99,
  "description": "100% Cotton",
  "size": "large"
}
```

### 📌 `GET /products`
List all products with filters:
- `name` → partial search
- `size` → exact match
- `limit`, `offset` → for pagination

---

### 📌 `POST /orders`
Create an order.
```json
{
  "user_id": "user123",
  "product_ids": ["productid1", "productid2"]
}
```

### 📌 `GET /orders/{user_id}`
Get orders for a user. Supports:
- `limit`, `offset` for pagination.

---

## 📁 Project Structure

```
.
├── main.py               # FastAPI app entry point
├── models.py             # Pydantic models
├── database.py           # MongoDB connection
├── requirements.txt      # Dependencies
├── .env                  # MongoDB URI (keep secret)
├── start.sh              # Start command for Render
├── render.yaml           # Deployment config (optional)
└── routers/
    ├── products.py       # Product APIs
    └── orders.py         # Order APIs
```

---

## 🧪 How to Run Locally

1. Clone the repo:
   ```bash
   git clone https://github.com/your-username/fastapi-ecommerce.git
   cd fastapi-ecommerce
   ```

2. Create a virtual environment & activate:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Create `.env` file:
   ```
   MONGO_URL=mongodb+srv://<your_user>:<password>@cluster0.mongodb.net/?retryWrites=true&w=majority
   ```

5. Run the app:
   ```bash
   uvicorn main:app --reload
   ```

6. Open Swagger UI:
   [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## 🌐 Deployment

- Hosted on: [Render](https://render.com)
- MongoDB: [MongoDB Atlas](https://cloud.mongodb.com)

---

## ✅ Submission

- Base URL: `https://your-render-app.onrender.com`
- Submitted to: [HROne Submission Form](https://forms.office.com/r/UKcJhfZV15)

---

## 🧑‍💻 Author

**Parag Bhati**  
Backend Developer & FastAPI Enthusiast

---

## 📄 License

This project is part of a coding task and is free for educational and demo purposes.
