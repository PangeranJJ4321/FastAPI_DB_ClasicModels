from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import timedelta
from auth.auth import (
    Token, authenticate_user, create_access_token, get_password_hash,
    fake_users_db, ACCESS_TOKEN_EXPIRE_MINUTES,
    get_current_active_user, User
)

class AuthController:
    def __init__(self):
        self.router = APIRouter(tags=["Authentication"], prefix="/auth")
        self._setup_routes()
    
    def _setup_routes(self):
        @self.router.post("/token", response_model=Token)
        async def login_for_access_token(form_data: OAuth2PasswordRequestForm = Depends()):
            user = authenticate_user(fake_users_db, form_data.username, form_data.password)
            if not user:
                raise HTTPException(
                    status_code=status.HTTP_401_UNAUTHORIZED,
                    detail="Incorrect username or password",
                    headers={"WWW-Authenticate": "Bearer"},
                )
            access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
            access_token = create_access_token(
                data={"sub": user.username}, expires_delta=access_token_expires
            )
            return {"access_token": access_token, "token_type": "bearer"}
        
        @self.router.get("/users/me", response_model=User)
        async def read_users_me(current_user: User = Depends(get_current_active_user)):
            return current_user
        
        @self.router.get("/test-auth")
        async def test_auth(current_user: User = Depends(get_current_active_user)):
            return {"message": f"Authenticated as {current_user.username}"}
            
        @self.router.get("/debug")
        async def debug_auth():
            # Menampilkan username yang ada di database
            users = list(fake_users_db.keys())
            return {
                "available_users": users
                
            }