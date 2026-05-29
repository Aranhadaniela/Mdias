from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.donation_routes import router as donation_router

app = FastAPI(
    title="M Dias Branco API",
    description="API para formulário de solicitação de doação",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(donation_router, prefix="/api")


@app.get("/")
def home():
    return {
        "message": "API M Dias Branco rodando com sucesso!"
    }