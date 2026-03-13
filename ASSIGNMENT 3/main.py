from fastapi import FastAPI, Query, Response, status
from pydantic import BaseModel, Field
from typing import Optional, List

app = FastAPI(title="My E-commerce Store API - Day 4")

# ── Product Data ──────────────────────────────────────────────
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499,  "category": "Electronics", "in_stock": True},
    {"id": 2, "name": "USB-C Hub",      "price": 999,  "category": "Electronics", "in_stock": True},
    {"id": 3, "name": "Notebook",       "price": 149,  "category": "Stationery",  "in_stock": True},
    {"id": 4, "name": "Pen Set",        "price": 49,   "category": "Stationery",  "in_stock": False},
]

orders   = []
feedback = []

# ── Helper ────────────────────────────────────────────────────
def find_product(product_id: int):
    for p in products:
        if p["id"] == product_id:
            return p
    return None

# ── Pydantic Models ───────────────────────────────────────────
class NewProduct(BaseModel):
    name:     str  = Field(..., min_length=2, max_length=100)
    price:    int  = Field(..., gt=0)
    category: str  = Field(..., min_length=2)
    in_stock: bool = True

class OrderRequest(BaseModel):
    customer_name: str = Field(..., min_length=2, max_length=100)
    product_id:    int = Field(..., gt=0)
    quantity:      int = Field(..., gt=0, le=50)

class CustomerFeedback(BaseModel):
    customer_name: str           = Field(..., min_length=2, max_length=100)
    product_id:    int           = Field(..., gt=0)
    rating:        int           = Field(..., ge=1, le=5)
    comment:       Optional[str] = Field(None, max_length=300)

class OrderItem(BaseModel):
    product_id: int = Field(..., gt=0)
    quantity:   int = Field(..., gt=0, le=50)

class BulkOrder(BaseModel):
    company_name:  str             = Field(..., min_length=2)
    contact_email: str             = Field(..., min_length=5)
    items:         List[OrderItem] = Field(..., min_length=1)


# ══════════════════════════════════════════════════════════════
# GET ENDPOINTS
# ══════════════════════════════════════════════════════════════

@app.get("/products")
def get_all_products():
    return {"products": products, "total": len(products)}

@app.get("/products/filter")
def filter_products(
    category:  str = Query(None, description="Filter by category"),
    max_price: int = Query(None, description="Maximum price"),
    min_price: int = Query(None, description="Minimum price"),
):
    result = products
    if category:
        result = [p for p in result if p["category"] == category]
    if max_price:
        result = [p for p in result if p["price"] <= max_price]
    if min_price:
        result = [p for p in result if p["price"] >= min_price]
    return {"filters": {"category": category, "min_price": min_price, "max_price": max_price},
            "results": result, "total": len(result)}

@app.get("/products/instock")
def get_instock():
    available = [p for p in products if p["in_stock"] == True]
    return {"in_stock_products": available, "count": len(available)}

@app.get("/products/deals")
def get_deals():
    cheapest  = min(products, key=lambda p: p["price"])
    expensive = max(products, key=lambda p: p["price"])
    return {"best_deal": cheapest, "premium_pick": expensive}

@app.get("/products/summary")
def product_summary():
    in_stock   = [p for p in products if     p["in_stock"]]
    out_stock  = [p for p in products if not p["in_stock"]]
    expensive  = max(products, key=lambda p: p["price"])
    cheapest   = min(products, key=lambda p: p["price"])
    categories = list(set(p["category"] for p in products))
    return {
        "total_products":     len(products),
        "in_stock_count":     len(in_stock),
        "out_of_stock_count": len(out_stock),
        "most_expensive":     {"name": expensive["name"], "price": expensive["price"]},
        "cheapest":           {"name": cheapest["name"],  "price": cheapest["price"]},
        "categories":         categories,
    }

@app.get("/store/summary")
def store_summary():
    in_stock_count  = len([p for p in products if p["in_stock"]])
    out_stock_count = len(products) - in_stock_count
    categories      = list(set([p["category"] for p in products]))
    return {
        "store_name":     "My E-commerce Store",
        "total_products": len(products),
        "in_stock":       in_stock_count,
        "out_of_stock":   out_stock_count,
        "categories":     categories,
    }

@app.get("/products/search/{keyword}")
def search_products(keyword: str):
    results = [p for p in products if keyword.lower() in p["name"].lower()]
    if not results:
        return {"message": "No products matched your search"}
    return {"keyword": keyword, "results": results, "total_matches": len(results)}

@app.get("/products/category/{category_name}")
def get_by_category(category_name: str):
    result = [p for p in products if p["category"] == category_name]
    if not result:
        return {"error": "No products found in this category"}
    return {"category": category_name, "products": result, "total": len(result)}

# ── Q5: Audit endpoint — MUST be above /products/{product_id} ─
@app.get("/products/audit")
def product_audit():
    in_stock_list  = [p for p in products if     p["in_stock"]]
    out_stock_list = [p for p in products if not p["in_stock"]]
    stock_value    = sum(p["price"] * 10 for p in in_stock_list)
    priciest       = max(products, key=lambda p: p["price"])
    return {
        "total_products":     len(products),
        "in_stock_count":     len(in_stock_list),
        "out_of_stock_names": [p["name"] for p in out_stock_list],
        "total_stock_value":  stock_value,
        "most_expensive":     {"name": priciest["name"], "price": priciest["price"]},
    }

@app.get("/products/{product_id}")
def get_product(product_id: int, response: Response):
    product = find_product(product_id)
    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Product not found"}
    return {"product": product}

@app.get("/products/{product_id}/price")
def get_product_price(product_id: int):
    for product in products:
        if product["id"] == product_id:
            return {"name": product["name"], "price": product["price"]}
    return {"error": "Product not found"}


# ══════════════════════════════════════════════════════════════
# Q1 — POST: Add a New Product
# ══════════════════════════════════════════════════════════════

@app.post("/products", status_code=201)
def add_product(new_product: NewProduct, response: Response):
    # Check for duplicate name
    for p in products:
        if p["name"].lower() == new_product.name.lower():
            response.status_code = status.HTTP_400_BAD_REQUEST
            return {"error": f"Product '{new_product.name}' already exists"}

    # Auto-generate next ID
    next_id = max(p["id"] for p in products) + 1
    product = {
        "id":       next_id,
        "name":     new_product.name,
        "price":    new_product.price,
        "category": new_product.category,
        "in_stock": new_product.in_stock,
    }
    products.append(product)
    return {"message": "Product added", "product": product}


# ══════════════════════════════════════════════════════════════
# Q2 — PUT: Update a Product (restock / price change)
# ══════════════════════════════════════════════════════════════

@app.put("/products/discount")
def bulk_discount(
    category:         str = Query(..., description="Category to discount"),
    discount_percent: int = Query(..., ge=1, le=99, description="% off"),
):
    updated = []
    for p in products:
        if p["category"] == category:
            p["price"] = int(p["price"] * (1 - discount_percent / 100))
            updated.append(p)
    if not updated:
        return {"message": f"No products found in category: {category}"}
    return {
        "message":          f"{discount_percent}% discount applied to {category}",
        "updated_count":    len(updated),
        "updated_products": updated,
    }

@app.put("/products/{product_id}")
def update_product(
    product_id: int,
    response:   Response,
    price:      Optional[int]  = Query(None, description="New price"),
    in_stock:   Optional[bool] = Query(None, description="Stock status"),
):
    product = find_product(product_id)
    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Product not found"}
    if price is not None:
        product["price"] = price
    if in_stock is not None:
        product["in_stock"] = in_stock
    return {"message": "Product updated", "product": product}


# ══════════════════════════════════════════════════════════════
# Q3 — DELETE: Remove a Product
# ══════════════════════════════════════════════════════════════

@app.delete("/products/{product_id}")
def delete_product(product_id: int, response: Response):
    product = find_product(product_id)
    if not product:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": "Product not found"}
    products.remove(product)
    return {"message": f"Product '{product['name']}' deleted"}


# ══════════════════════════════════════════════════════════════
# POST Endpoints (from Day 2)
# ══════════════════════════════════════════════════════════════

@app.post("/feedback")
def submit_feedback(data: CustomerFeedback):
    feedback.append(data.dict())
    return {
        "message":        "Feedback submitted successfully",
        "feedback":       data.dict(),
        "total_feedback": len(feedback),
    }

@app.post("/orders/bulk")
def place_bulk_order(order: BulkOrder):
    confirmed, failed, grand_total = [], [], 0
    for item in order.items:
        product = next((p for p in products if p["id"] == item.product_id), None)
        if not product:
            failed.append({"product_id": item.product_id, "reason": "Product not found"})
        elif not product["in_stock"]:
            failed.append({"product_id": item.product_id, "reason": f"{product['name']} is out of stock"})
        else:
            subtotal = product["price"] * item.quantity
            grand_total += subtotal
            confirmed.append({"product": product["name"], "qty": item.quantity, "subtotal": subtotal})
    return {"company": order.company_name, "confirmed": confirmed,
            "failed": failed, "grand_total": grand_total}

@app.post("/orders")
def place_order(order: OrderRequest):
    product = next((p for p in products if p["id"] == order.product_id), None)
    if not product:
        return {"error": "Product not found"}
    if not product["in_stock"]:
        return {"error": f"{product['name']} is out of stock"}
    order_id = len(orders) + 1
    new_order = {
        "order_id":      order_id,
        "customer_name": order.customer_name,
        "product":       product["name"],
        "quantity":      order.quantity,
        "total_price":   product["price"] * order.quantity,
        "status":        "pending",
    }
    orders.append(new_order)
    return {"message": "Order placed successfully", "order": new_order}

@app.get("/orders/{order_id}")
def get_order(order_id: int):
    for order in orders:
        if order["order_id"] == order_id:
            return {"order": order}
    return {"error": "Order not found"}

@app.patch("/orders/{order_id}/confirm")
def confirm_order(order_id: int):
    for order in orders:
        if order["order_id"] == order_id:
            order["status"] = "confirmed"
            return {"message": "Order confirmed", "order": order}
    return {"error": "Order not found"}
