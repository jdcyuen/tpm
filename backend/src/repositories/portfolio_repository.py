from sqlalchemy.orm import Session
from sqlalchemy import text


class PortfolioRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_latest_snapshot(self):
        """
        Returns the most recent portfolio snapshot across all positions.
        """

        query = text("""
            SELECT *
            FROM snapshots
            ORDER BY snapshot_date DESC
            LIMIT 1
        """)

        result = self.db.execute(query)
        return result.fetchall()

    def get_positions_by_snapshot(self, snapshot_id: int):
        """
        Returns all positions for a given snapshot.
        """

        query = text("""
            SELECT *
            FROM positions
            WHERE snapshot_id = :snapshot_id
        """)

        result = self.db.execute(query, {"snapshot_id": snapshot_id})
        return result.fetchall()

    def get_full_portfolio(self):
        """
        Join positions + accounts + securities for UI display.
        """

        query = text("""
            SELECT
                a.account_name,
                a.account_number,
                s.ticker,
                s.description,
                p.quantity,
                p.market_value
            FROM tpm.positions p
            JOIN tpm.accounts a ON p.account_id = a.id
            JOIN tpm.securities s ON p.security_id = s.id
        """)

        result = self.db.execute(query)
        return result.fetchall()
