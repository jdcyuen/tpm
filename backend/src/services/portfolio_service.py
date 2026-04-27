from src.repositories.portfolio_repository import PortfolioRepository


class PortfolioService:
    def __init__(self, db):
        self.repo = PortfolioRepository(db)

    def get_portfolio(self):
        """
        Returns portfolio data formatted for API/UI consumption.
        """

        rows = self.repo.get_full_portfolio()

        portfolio = []

        for r in rows:
            portfolio.append(
                {
                    "accountName": r.account_name,
                    "accountNumber": r.account_number,
                    "ticker": r.ticker,
                    "description": r.description,
                    "quantity": float(r.quantity) if r.quantity else 0,
                    "marketValue": float(r.market_value) if r.market_value else 0,
                }
            )

        return {"data": portfolio, "count": len(portfolio)}
