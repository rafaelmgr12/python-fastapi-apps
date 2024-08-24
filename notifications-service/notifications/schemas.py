from pydantic import BaseModel

class NotificationSchema(BaseModel):
    title: str
    message: str
    user_id: str

class NotificationResponse(BaseModel):
    success: bool
    message: str