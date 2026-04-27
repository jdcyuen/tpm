from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from src.db.session import get_db
from src.services.portfolio_service import PortfolioService

router = APIRouter()


@router.get("/portfolio")
def get_portfolio(db: Session = Depends(get_db)):
    service = PortfolioService(db)
    return service.get_portfolio()
