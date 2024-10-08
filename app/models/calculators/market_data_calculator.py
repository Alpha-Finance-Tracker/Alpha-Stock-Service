import logging

from app.models.base_models.stock_calculator import StockCalculator
from app.utilities.responses import CalculationError


class AverageMarketData(StockCalculator):

    def __init__(self, market_data):
        self.market_data = market_data

    async def calculate(self):
        try:

            if 'Adj Close' not in self.market_data.columns or self.market_data.empty:
                raise ValueError("Missing 'Adj Close' column or data is empty.")

            self.market_data['daily_return'] = self.market_data['Adj Close'].pct_change()
            daily_returns = self.market_data['daily_return'].dropna()
            average_daily_return = daily_returns.mean()

            return float(average_daily_return * 252)

        except (ZeroDivisionError, ValueError, TypeError) as e:
            logging.error(f"Calculation error: {e}")
            raise CalculationError()
