from fastapi import FastAPI, APIRouter, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from app.producer import publish_message

app = FastAPI()  # This is the app Uvicorn looks for

# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins for development; change to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

router = APIRouter()

@router.post("/send-notification")
def send_notification(payload: dict):
    try:
        publish_message(payload)
        return {"message": "Notification queued successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

app.include_router(router)  # Include your router in the app
