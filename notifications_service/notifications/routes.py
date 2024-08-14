from fastapi import APIRouter, HTTPException
from notifications.schemas import NotificationSchema, NotificationResponse
from notifications.utils import send_notification

router = APIRouter()

@router.post("/", response_model=NotificationResponse)
async def create_notification(notification: NotificationSchema):
    success = send_notification(notification)
    if not success:
        raise HTTPException(status_code=500, detail="Notification failed")
    return NotificationResponse(success=True, message="Notification sent successfully")