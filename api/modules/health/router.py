from fastapi import APIRouter
from core.odoo_client import OdooClient

router = APIRouter()

odoo = OdooClient()

@router.get("/test-odoo")
def test_odoo():
    return odoo.execute(
        "university.student",
        "search_read",
        [[]],
        {"limit": 5}
    )