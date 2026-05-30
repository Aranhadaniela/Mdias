from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.routes.program_routes import router as program_router
from app.routes.donation_routes import router as donation_router

app = FastAPI(
    title="M Dias Branco API",
    description="API para formulário de solicitação de doação",
    version="1.0.0"
)

origins = [
    "https://m-dias-branco-responsabilidade-social.powerappsportals.com",
    "http://localhost:3000",
    "http://localhost:8000",
    "http://127.0.0.1:8000"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(donation_router, prefix="/api")
app.include_router(program_router, prefix="/api")

@app.get("/")
def home():
    return {
        "message": "API M Dias Branco rodando com sucesso!"
    }