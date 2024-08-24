from fastapi import FastAPI, Depends
from notifications.routes import router as notifications_router
from auth.jwt_handler import JWTBearer

app = FastAPI()

app.include_router(notifications_router, prefix="/notifications", dependencies=[Depends(JWTBearer())])


@app.get("/")
def read_root():
    return {"message": "Welcome to the Notification Service!"}