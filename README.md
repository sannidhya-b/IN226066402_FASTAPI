# 🛒 FastAPI E-Commerce Store API
### Feb Internship 2026 — FastAPI Assignment

---

## 👩‍💻 Intern Details
| Field | Details |
|-------|---------|
| **Intern ID** | IN226066402 |
| **Name** | Sannidhya |
| **Assignment** | FastAPI — Day 1, Day 2, Day 4 & Day 5 Practice Tasks |

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
├── ASSIGNMENT 2/
│   ├── BONUS_OUTPUT1.png
│   ├── BONUS_OUTPUT2.png
│   ├── BONUS_OUTPUT3.png
│   ├── Q1_OUTPUT.png
│   ├── Q2_OUTPUT.png
│   ├── Q3_OUTPUT.png
│   ├── Q4_OUTPUT.png
│   ├── Q5_OUTPUT.png
│   └── main.py
├── ASSIGNMENT 3/
│   ├── Bonus_Output1.png
│   ├── Bonus_Output2.png
│   ├── Bonus_Output3.png
│   ├── Q1_Output1.png
│   ├── Q1_Output2.png
│   ├── Q1_Output3.png
│   ├── Q2_Output1.png
│   ├── Q2_Output2.png
│   ├── Q2_Output3.png
│   ├── Q2_Output4.png
│   ├── Q3_Output1.png
│   ├── Q3_Output2.png
│   ├── Q3_Output3.png
│   ├── Q3_Output4.png
│   ├── Q4_Output1.png
│   ├── Q4_Output2.png
│   ├── Q4_Output3.png
│   ├── Q4_Output4.png
│   ├── Q4_Output5.png
│   ├── Q4_Output6.png
│   ├── Q5_Output.png
│   └── main.py
└── ASSIGNMENT 4/
    ├── Bonus_Output1.png
    ├── Bonus_Output2.png
    ├── Bonus_Output3.png
    ├── Q1_Output1.png
    ├── Q1_Output2.png
    ├── Q2_Output.png
    ├── Q3_Output1.png
    ├── Q3_Output2.png
    ├── Q4_Output1.png
    ├── Q4_Output2.png
    ├── Q5_Output1.png
    ├── Q5_Output2.png
    ├── Q5_Output3.png
    ├── Q5_Output4.png
    ├── Q5_Output5.png
    ├── Q6_Output1.png
    ├── Q6_Output2.png
    ├── Q6_Output3.png
    ├── Q6_Output4.png
    ├── Q6_Output5.png
    ├── Q6_Output6.png
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

## 📌 Day 4 — API Endpoints (CRUD)

| # | Method | Endpoint | Description |
|---|--------|----------|-------------|
| Q1 | POST | `/products` | Add new product with auto ID & duplicate check |
| Q2 | PUT | `/products/{id}` | Update price and/or stock status |
| Q3 | DELETE | `/products/{id}` | Delete product, 404 if not found |
| Q4 | All | Full CRUD | Complete lifecycle — Add, Update, Delete Smart Watch |
| Q5 | GET | `/products/audit` | Inventory summary dashboard |
| ⭐ | PUT | `/products/discount` | Apply category-wide discount percentage |

---

## 📌 Day 5 — Cart System Endpoints

| # | Method | Endpoint | Description |
|---|--------|----------|-------------|
| Q1 | POST | `/cart/add?product_id=1&quantity=2` | Add item to cart |
| Q2 | GET | `/cart` | View cart with grand total |
| Q3 | POST | `/cart/add?product_id=3` | Out of stock → 400 error |
| Q4 | POST | `/cart/add?product_id=1&quantity=1` | Update existing cart item quantity |
| Q5 | DELETE | `/cart/{product_id}` | Remove item from cart |
| Q5 | POST | `/cart/checkout` | Checkout and place orders |
| Q6 | All | Full flow | 2 customers complete cart flow |
| ⭐ | POST | `/cart/checkout` | Empty cart → 400 Bad Request |

---

## 🧪 Day 5 — Test URLs
```
POST  http://127.0.0.1:8000/cart/add?product_id=1&quantity=2
POST  http://127.0.0.1:8000/cart/add?product_id=2&quantity=1
GET   http://127.0.0.1:8000/cart
POST  http://127.0.0.1:8000/cart/add?product_id=3   → 400 out of stock
POST  http://127.0.0.1:8000/cart/add?product_id=99  → 404 not found
DELETE http://127.0.0.1:8000/cart/2
POST  http://127.0.0.1:8000/cart/checkout
GET   http://127.0.0.1:8000/orders
```

---

## 🛍️ Product Data

| ID | Name | Price | Category | In Stock |
|----|------|-------|----------|----------|
| 1 | Wireless Mouse | ₹499 | Electronics | ✅ |
| 2 | Notebook | ₹99 | Stationery | ✅ |
| 3 | USB Hub | ₹799 | Electronics | ❌ |
| 4 | Pen Set | ₹49 | Stationery | ✅ |

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

## ✅ Day 4 Submission Checklist
- [x] Q1 — `POST /products` adds Laptop Stand with ID 5 and status 201
- [x] Q1 — `POST /products` adds Sticky Notes with ID 6 and status 201
- [x] Q1 — `POST /products` with "Wireless Mouse" returns 400 duplicate error
- [x] Q2 — `PUT /products/2?in_stock=true` restocks USB Hub correctly
- [x] Q2 — `PUT /products/2?in_stock=true&price=649` updates both fields
- [x] Q2 — `PUT /products/99?price=100` returns 404 Not Found
- [x] Q3 — `DELETE /products/4` removes Pen Set successfully
- [x] Q3 — `DELETE /products/4` again returns 404 Not Found
- [x] Q4 — Full 6-step CRUD lifecycle for Smart Watch completed
- [x] Q5 — `GET /products/audit` returns correct inventory summary
- [x] ⭐ Bonus — `PUT /products/discount` reduces all Electronics prices by 10%

## ✅ Day 5 Submission Checklist
- [x] Q1 — Wireless Mouse (subtotal 998) and Notebook (subtotal 99) added to cart
- [x] Q2 — `GET /cart` shows item_count: 2 and grand_total: 1097
- [x] Q3 — Adding USB Hub (id=3) returns 400, Adding id=99 returns 404
- [x] Q4 — Adding Mouse again shows "Cart updated", qty=3, grand_total=1596
- [x] Q5 — Notebook removed, checkout works, cart empty after, order in GET /orders
- [x] Q6 — 2-customer flow: 3 total orders in GET /orders at the end
- [x] ⭐ Bonus — `POST /cart/checkout` on empty cart returns 400, no order created

---

*Built for FastAPI Internship Training · Day 1, Day 2, Day 4 & Day 5 Assignments 🚀*
