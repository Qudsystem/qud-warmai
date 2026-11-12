from fastapi import APIRouter, Depends
from ...core.auth import get_current_user
from ...database.models import User

router = APIRouter()

@router.get("/status")
def system_status(current_user: User = Depends(get_current_user)):
    return {
        "status": "OPERATIONAL",
        "cpu_load": "OPTIMAL",
        "security_level": "OMEGA-RED",
        "active_user": current_user.username
    }
