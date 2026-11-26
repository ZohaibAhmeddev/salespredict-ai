from fastapi import APIRouter
from app.services.sales_service import (
    get_sales_records,
    get_sales_summary
)

router = APIRouter(
    prefix ="/sales",
    tags = ["Sales"]
)

@router.get("/")
def get_sales():
    records = get_sales_records()

    return {
        "message": "Sales Api is working!",
        "data": records,
        "total_records": len(records)
    }

@router.get("/summary")
def sale_summary():
    return get_sales_summary()
