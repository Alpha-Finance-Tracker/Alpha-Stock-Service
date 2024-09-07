from fastapi import APIRouter, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from app.api.services.intrinsic_calculator_service import IntrinsicCalculatorService
from app.models.calculators.fair_value_calculator import FairValue
from app.models.calculators.future_price_calculator import StockPredictor
from app.utilities.responses import StockDataUnavailable

from app.utilities.token_verification import verify_token

stock_calculator = APIRouter(prefix='/stock_calculator')

security = HTTPBearer()



@stock_calculator.get('/Intrinsic_value')
async def intrinsic_value(symbol: str,
                          credentials: HTTPAuthorizationCredentials = Depends(security)):
    await verify_token(credentials.credentials)
    try:
        return await IntrinsicCalculatorService(symbol).intrinsic_value_service()

    except StockDataUnavailable as e:
        raise e


@stock_calculator.get('/fair_value')
async def fair_value(symbol: str,
                     credentials: HTTPAuthorizationCredentials = Depends(security)):
    await verify_token(credentials.credentials)

    try:
        return FairValue(symbol).calculate()
    except StockDataUnavailable as e:
        raise e


@stock_calculator.get('price_predictor')
async def stock_prediction(symbol: str,
                           credentials: HTTPAuthorizationCredentials = Depends(security)):
    await verify_token(credentials.credentials)
    return await StockPredictor(symbol).calculate()

