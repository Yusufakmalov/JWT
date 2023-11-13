from fastapi import FastAPI


from passlib.context import CryptContext

SECRET_KEY = "itaitsasurprisemotherfucker"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 31

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')



# SWAGGER
app = FastAPI(docs_url='/')

@app.get('/home')
async def home():
    return 'This is home page'

@app.post('/register')
async def register():
    return 'Register page'

@app.post('/login')
async def login():
    return 'login page'

