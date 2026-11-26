
def get_sales_records():
    """
    Return sales records.

    Currently returns an empty list.
    PostgreSQL integration will be added later.
    """
    return []


def get_sales_summary():
    """
    Return sales summary.

    Real calculations will be implemented
    after database integration.
    """
    return {
        "total_sales": 0,
        "total_revenue": 0.0,
        "total_orders": 0
    }
