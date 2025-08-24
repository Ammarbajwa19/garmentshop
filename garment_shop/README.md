# Garment Shop

A minimal FastAPI-based garment shop with inventory, orders, and payments.

## Setup

```bash
# Using Poetry
pip install poetry
cd garment_shop
poetry install
poetry run uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
```

## Features (planned)
- Products with inventory
- Customers
- Orders and order items
- Payments (mock/recorded)
- Reports