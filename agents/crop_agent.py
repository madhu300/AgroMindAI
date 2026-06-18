import pandas as pd

data = pd.read_csv("data/crop_production.csv")

def recommend_crop(rainfall, soil):
    filtered = data[
        (data["Rainfall"] >= rainfall - 10) &
        (data["Rainfall"] <= rainfall + 10) &
        (data["Soil"].str.lower() == soil.lower())
    ]

    if not filtered.empty:
        return filtered.iloc[0]["Crop"]

    return "No suitable crop found"