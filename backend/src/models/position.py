class Position:
    def __init__(
        self,
        account_name: str,
        account_number: str,
        ticker: str,
        description: str,
        quantity: float,
        market_value: float,
        avg_cost: float,
    ):
        self.account_name = account_name
        self.account_number = account_number
        self.ticker = ticker
        self.description = description
        self.quantity = quantity
        self.market_value = market_value
        self.avg_cost = avg_cost
