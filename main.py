from fastapi import FastAPI, HTTPException, status
from fastapi.responses import JSONResponse
from fastapi.params import Query
from datetime import datetime
import pandas as pd
import joblib

app = FastAPI(
    title="Bitcoin Price Prediction Model",
    version="1.0.0"
)

# Load the Bitcoin Prediction Model
model = joblib.load("model/saved_btc_model.pkl")

@app.post("/predict-bitcoin-price", status_code=200)
async def predict_bitcoin_price(prediction_date: str = Query(..., description="Use date formart: MM/DD/YYYY")):
    try:
        date_parsed = datetime.strptime(prediction_date, '%m/%d/%Y')
        date_features = pd.DataFrame([[date_parsed.year, date_parsed.month, date_parsed.day]], columns=['Year', 'Month', 'Day'])
        prediction = model.predict(date_features)
        return JSONResponse(
            status_code=status.HTTP_200_OK,
            content={"predicted_price": prediction[0]}
        )
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=str(e)
        )

# To run the server, use the command: uvicorn main:app --reload