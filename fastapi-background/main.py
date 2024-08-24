
from fastapi import FastAPI, BackgroundTasks
from pydantic import BaseModel

app = FastAPI()

class UserRegistrationRequest(BaseModel):
    email: str

def send_welcome_message(email: str):
    # Simulating sending an email
    print(f"Sending welcome email to: {email}")
    
    
@app.get(path="/")
async def root():
    return {"message": "Welcome to te server"}

@app.post(path="/register/")
async def register_user(payload: UserRegistrationRequest, background_tasks: BackgroundTasks):
    # Simulate user registration logic
    user_created_successfully = True
    
    if user_created_successfully:
        # Adding the send_welcome_message function to background tasks
        background_tasks.add_task(send_welcome_message, payload.email)
        return {"message": "User registered successfully!"}
    else:
        return {"message": "User registration failed."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
