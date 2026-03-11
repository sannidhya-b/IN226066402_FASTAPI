# 🛒 FastAPI E-Commerce Store API
### Feb Internship 2026 — FastAPI Assignment

## 👩‍💻 Intern Details
| Field | Details |
|-------|---------|
| **Intern ID** | IN226066402 |
| **Name** | Sannidhya |
| **Assignment** | FastAPI — Day 1 & Day 2 Practice Tasks |

---

## 📂 Project Structure
```
IN226066402_FASTAPI/
├── ASSIGNMENT 1/
│   ├── BONUS_OUTPUT.png
│   ├── main.py
│   ├── Q1_OUTPUT.png
│   ├── Q2_OUTPUT.png
│   ├── Q3_OUTPUT.png
│   ├── Q4_OUTPUT.png
│   └── Q5_OUTPUT.png
└── ASSIGNMENT 2/
    ├── BONUS_OUTPUT1.png
    ├── BONUS_OUTPUT2.png
    ├── BONUS_OUTPUT3.png
    ├── Q1_OUTPUT.png
    ├── Q2_OUTPUT.png
    ├── Q3_OUTPUT.png
    ├── Q4_OUTPUT.png
    ├── Q5_OUTPUT.png
    └── main.py
```

---

## 🚀 How to Run

### 1. Install dependencies
```bash
py -m pip install fastapi uvicorn
```

### 2. Run the server
```bash
py -m uvicorn main:app --reload
```

### 3. Open in browser
```
http://127.0.0.1:8000
```

### 4. Test all endpoints in Swagger UI
```
http://127.0.0.1:8000/docs
```

---

## 📌 Day 1 — API Endpoints

| # | Method | Endpoint | Description |
|---|--------|----------|-------------|
| Q1 | GET | `/products` | Get all 7 products with total count |
| Q2 | GET | `/products/category/{category_name}` | Filter products by category |
| Q3 | GET | `/products/instock` | Get only in-stock products |
| Q4 | GET | `/store/summary` | Get full store overview |
| Q5 | GET | `/products/search/{keyword}` | Search products by name (case-insensitive) |
| ⭐ | GET | `/products/deals` | Get cheapest & most expensive product |

---

## 📌 Day 2 — API Endpoints

| # | Method | Endpoint | Description |
|---|--------|----------|-------------|
| Q1 | GET | `/products/filter?min_price=400` | Filter by min & max price |
| Q2 | GET | `/products/{id}/price` | Get only name & price of a product |
| Q3 | POST | `/feedback` | Submit customer feedback with validation |
| Q4 | GET | `/products/summary` | Full product dashboard stats |
| Q5 | POST | `/orders/bulk` | Place bulk order with confirmed/failed list |
| ⭐ | POST | `/orders` | Place order (starts as "pending") |
| ⭐ | GET | `/orders/{order_id}` | Get order by ID |
| ⭐ | PATCH | `/orders/{order_id}/confirm` | Confirm a pending order |

---

## 🧪 Day 1 — Test URLs

```
GET http://127.0.0.1:8000/products
GET http://127.0.0.1:8000/products/category/Electronics
GET http://127.0.0.1:8000/products/instock
GET http://127.0.0.1:8000/store/summary
GET http://127.0.0.1:8000/products/search/mouse
GET http://127.0.0.1:8000/products/deals
```

## 🧪 Day 2 — Test URLs

```
GET  http://127.0.0.1:8000/products/filter?min_price=400
GET  http://127.0.0.1:8000/products/filter?min_price=100&max_price=600
GET  http://127.0.0.1:8000/products/1/price
GET  http://127.0.0.1:8000/products/summary
POST http://127.0.0.1:8000/feedback        → test in Swagger UI
POST http://127.0.0.1:8000/orders/bulk     → test in Swagger UI
POST http://127.0.0.1:8000/orders          → test in Swagger UI
GET  http://127.0.0.1:8000/orders/1
PATCH http://127.0.0.1:8000/orders/1/confirm
```

---

## 🛍️ Product Data

| ID | Name | Price | Category | In Stock |
|----|------|-------|----------|----------|
| 1 | Wireless Mouse | ₹499 | Electronics | ✅ |
| 2 | USB-C Hub | ₹999 | Electronics | ✅ |
| 3 | Notebook | ₹149 | Stationery | ✅ |
| 4 | Pen Set | ₹49 | Stationery | ❌ |
| 5 | Laptop Stand | ₹1299 | Electronics | ✅ |
| 6 | Mechanical Keyboard | ₹2499 | Electronics | ✅ |
| 7 | Webcam | ₹1899 | Electronics | ❌ |

---

## ✅ Day 1 Submission Checklist

- [x] Q1 — `/products` returns total: 7
- [x] Q2 — `/products/category/Electronics` works
- [x] Q3 — `/products/instock` shows only available products
- [x] Q4 — `/store/summary` shows full store overview
- [x] Q5 — `/products/search/mouse` returns Wireless Mouse
- [x] ⭐ Bonus — `/products/deals` returns cheapest and most expensive

## ✅ Day 2 Submission Checklist

- [x] Q1 — `/products/filter?min_price=400` returns correct products
- [x] Q2 — `/products/1/price` returns only name and price
- [x] Q3 — `POST /feedback` with rating=6 returns 422 validation error
- [x] Q4 — `/products/summary` returns all 5 stats
- [x] Q5 — `POST /orders/bulk` handles confirmed and failed items
- [x] ⭐ Bonus — New order starts as "pending", PATCH confirms it

---

*Built for FastAPI Internship Training · Day 1 & Day 2 Assignments 🚀*
