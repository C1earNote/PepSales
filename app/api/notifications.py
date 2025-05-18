from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.notification import NotificationCreate
from app.services.queue_service import send_to_queue
from app.db.database import SessionLocal
from app.models.notification import Notification

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/notifications")
def create_notification(notification: NotificationCreate):
    try:
        send_to_queue(notification.dict())
        return {"message": "Notification queued successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/users/{user_id}/notifications")
def get_user_notifications(user_id: str, db: Session = Depends(get_db)):
    return db.query(Notification).filter(Notification.user_id == user_id).all()
