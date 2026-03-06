🛒 FastAPI E-Commerce Store API
Feb Internship 2026 — Day 1 Assignment

👩‍💻 Intern Details
FieldDetailsIntern IDIN226066402NameSannidhyaAssignmentFastAPI — Day 1 Practice TasksDeadline06/03/2026

📂 Project Structure
IN226066402_FASTAPI/
└── ASSIGNMENT 1/
    ├── main.py
    ├── Q1_OUTPUT.png
    ├── Q2_OUTPUT.png
    ├── Q3_OUTPUT.png
    ├── Q4_OUTPUT.png
    ├── Q5_OUTPUT.png
    └── BONUS_OUTPUT.png

🚀 How to Run
1. Install dependencies
bashpy -m pip install fastapi uvicorn
2. Run the server
bashpy -m uvicorn main:app --reload
3. Open in browser
http://127.0.0.1:8000
4. Test all endpoints in Swagger UI
http://127.0.0.1:8000/docs

📌 API Endpoints
#MethodEndpointDescriptionQ1GET/productsGet all 7 products with total countQ2GET/products/category/{category_name}Filter products by categoryQ3GET/products/instockGet only in-stock productsQ4GET/store/summaryGet full store overviewQ5GET/products/search/{keyword}Search products by name (case-insensitive)⭐GET/products/dealsGet cheapest & most expensive product

🧪 Test URLs
GET http://127.0.0.1:8000/products
GET http://127.0.0.1:8000/products/category/Electronics
GET http://127.0.0.1:8000/products/category/Stationery
GET http://127.0.0.1:8000/products/instock
GET http://127.0.0.1:8000/store/summary
GET http://127.0.0.1:8000/products/search/mouse
GET http://127.0.0.1:8000/products/search/BOOK
GET http://127.0.0.1:8000/products/deals

🛍️ Product Data
IDNamePriceCategoryIn Stock1Wireless Mouse₹499Electronics✅2USB-C Hub₹999Electronics✅3Notebook₹149Stationery✅4Pen Set₹49Stationery❌5Laptop Stand₹1299Electronics✅6Mechanical Keyboard₹2499Electronics✅7Webcam₹1899Electronics❌

✅ Submission Checklist

 Q1 — /products returns total: 7
 Q2 — /products/category/Electronics works
 Q3 — /products/instock shows only available products
 Q4 — /store/summary shows full store overview
 Q5 — /products/search/mouse returns Wireless Mouse
 Q5 — /products/search/BOOK also works (case-insensitive)
 All endpoints tested in Swagger UI at /docs
 ⭐ Bonus — /products/deals returns cheapest and most expensive
