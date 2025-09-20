from pydantic import BaseModel
from typing import Dict, Any

class UnifiedRequest(BaseModel):
    data: Dict[str, Any]

class TicketResponse(BaseModel):
    id: int
    user_name: str
    email: str
    issue_type: str
    description: str
