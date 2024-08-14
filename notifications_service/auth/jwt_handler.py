import jwt
import os

from fastapi import HTTPException, Request
from dotenv import load_dotenv

load_dotenv()


SECRET_KEY=os.getenv("SECRET_KEY")

def JWTBearer():
    def verify_jwt(request: Request):
        token = request.headers.get("Authorization")
        if not token:
            raise HTTPException(status_code=403, detail="Token is missing")
        try:
            payload = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=403, detail="Token has expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=403, detail="Invalid token")
    return verify_jwt