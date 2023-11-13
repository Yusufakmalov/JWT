from pydantic import BaseModel

# Model for enter to account(Log in)
class LoginModel(BaseModel):
    username: str
    password: str

# Model for registration
class RegisterModel(BaseModel):
    username: str
    password: str
    email: str


class Token(BaseModel):
    access_token: str
    token_type: str