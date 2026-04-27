import requests
from typing import List

from src.providers.base_provider import BaseProvider
from src.models.position import Position


class YodleeProvider(BaseProvider):
    """
    Yodlee provider implementation for fetching positions (holdings)
    across multiple accounts (e.g., Fidelity accounts).
    """

    BASE_URL = "https://api.yodlee.com/ysl"

    def __init__(self, access_token: str):
        self.access_token = access_token

    def _headers(self) -> dict:
        return {
            "Authorization": f"Bearer {self.access_token}",
            "Api-Version": "1.1",
            "Content-Type": "application/json",
        }

    # -----------------------------
    # Public API
    # -----------------------------
    def get_positions(self) -> List[Position]:
        """
        Fetch all positions across all linked accounts.
        """
        accounts = self._get_accounts()
        all_positions: List[Position] = []

        for account in accounts:
            account_id = account.get("id")
            account_name = account.get("accountName", "")
            account_number = account.get("accountNumber", "")

            holdings = self._get_holdings(account_id)

            for h in holdings:
                position = self._map_holding_to_position(
                    h, account_name, account_number
                )
                all_positions.append(position)

        return all_positions

    # -----------------------------
    # Private helpers
    # -----------------------------
    def _get_accounts(self) -> List[dict]:
        """
        Fetch all accounts linked to the Yodlee user.
        """
        url = f"{self.BASE_URL}/accounts"
        response = requests.get(url, headers=self._headers())

        self._validate_response(response)

        data = response.json()
        return data.get("account", [])

    def _get_holdings(self, account_id: int) -> List[dict]:
        """
        Fetch holdings for a specific account.
        """
        url = f"{self.BASE_URL}/accounts/{account_id}/holdings"
        response = requests.get(url, headers=self._headers())

        self._validate_response(response)

        data = response.json()
        return data.get("holding", [])

    def _map_holding_to_position(
        self, holding: dict, account_name: str, account_number: str
    ) -> Position:
        """
        Normalize Yodlee holding → internal Position model.
        """

        return Position(
            account_name=account_name,
            account_number=account_number,
            ticker=holding.get("symbol", "") or holding.get("cusip", ""),
            description=holding.get("description", ""),
            quantity=float(holding.get("quantity", 0)),
            market_value=float(holding.get("marketValue", 0)),
            avg_cost=float(holding.get("costBasis", 0)),
        )

    def _validate_response(self, response: requests.Response):
        """
        Basic error handling for API responses.
        """
        if response.status_code != 200:
            raise Exception(
                f"Yodlee API error: {response.status_code} - {response.text}"
            )
