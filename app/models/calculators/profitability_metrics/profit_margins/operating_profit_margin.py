from app.models.base_models.stock_calculator import StockCalculator
from app.utilities.responses import CalculationError


class OperatingProfitMargin(StockCalculator):

    def __init__(self, operating_incomes, total_revenues):
        self.operating_incomes = operating_incomes
        self.total_revenues = total_revenues

    def __repr__(self):
        return (f"OperatingProfitMargin(operating_incomes={self.operating_incomes}, "
                f"total_revenues={self.total_revenues})")

    async def calculate(self):
        try:
            operating_profit_margin = (self.operating_incomes / self.total_revenues) * 100
            operating_profit_margin = operating_profit_margin.round(2).dropna()
            return operating_profit_margin
        except:
            raise CalculationError()