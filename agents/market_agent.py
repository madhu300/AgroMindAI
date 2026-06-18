import pandas as pd

market = pd.read_csv("data/market_data.csv")

def market_analysis(crop):

    result = market[market["Crop"].str.lower() == crop.lower()]

    if not result.empty:

        price = result.iloc[0]["MarketPrice"]
        demand = result.iloc[0]["Demand"]

        return f"Market Demand: {demand} | Expected Price: ₹{price}"

    return "No market data available"