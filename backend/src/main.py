from fastapi import FastAPI

from src.api.v1.portfolio import router as portfolio_router

app = FastAPI(title="Total Portfolio Manager API", version="1.0.0")


# ----------------------------
# Health check (important for deployment + debugging)
# ----------------------------
@app.get("/health")
def health():
    return {"status": "ok"}


# ----------------------------
# API routes
# ----------------------------
app.include_router(portfolio_router, prefix="/api/v1")
