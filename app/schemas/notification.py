from pydantic import BaseModel
from typing import Literal

class NotificationCreate(BaseModel):
    user_id: str
    type: Literal['email', 'sms', 'in-app']
    message: str
