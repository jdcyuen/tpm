class ProviderFactory:
    @staticmethod
    def get_provider(name: str):
        if name == "yodlee":
            from src.providers.yodlee_provider import YodleeProvider

            return YodleeProvider()

        raise ValueError(f"Unknown provider: {name}")
