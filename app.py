import matplotlib.pyplot as plt
import pandas as pd
from flask import Flask, render_template, request
from agents.crop_agent import recommend_crop
from agents.weather_agent import analyze_weather
from agents.market_agent import market_analysis
from agents.master_agent import generate_final_report
from agents.yeild_agent import predict_yield
from agents.disease_agent import detect_disease_risk

app = Flask(__name__)
data = pd.read_csv("data/crop_production.csv")

@app.route("/", methods=["GET", "POST"])
def home():

    crop = ""
    weather_advice = ""
    market_info = ""
    final_report = ""
    yield_prediction = ""
    disease_risk = ""

    if request.method == "POST":

        rainfall = int(request.form["rainfall"])
        soil = request.form["soil"]

        crop = recommend_crop(rainfall, soil)
        weather_advice = analyze_weather(rainfall)
        market_info = market_analysis(crop)
        yield_prediction = predict_yield(crop, rainfall)
        disease_risk = detect_disease_risk(crop, rainfall)
        
        final_report = generate_final_report(
            crop,
            weather_advice,
            market_info
        )
        
        final_report += f"\n\n{yield_prediction}"
        final_report += f"\n\nDisease Analysis:\n{disease_risk}"

    return render_template(
        "index.html",
        crop=crop,
        weather_advice=weather_advice,
        market_info=market_info,
        final_report=final_report,
        yield_prediction=yield_prediction,
        disease_risk=disease_risk
    )

@app.route("/dashboard")
def dashboard():
    crop_counts = data["Crop"].value_counts()

    plt.figure(figsize=(6,4))
    crop_counts.plot(kind="bar")

    plt.title("Crop Production Analysis")
    plt.tight_layout()

    plt.savefig("static/chart1.png")
    plt.close()

    rainfall = data.groupby("Crop")["Rainfall"].mean()

    plt.figure(figsize=(6,4))
    rainfall.plot(kind="line", marker="o")

    plt.title("Average Rainfall Requirement")
    plt.tight_layout()

    plt.savefig("static/chart2.png")
    plt.close()

    soil = data["Soil"].value_counts()

    plt.figure(figsize=(6,4))
    soil.plot(kind="pie", autopct="%1.1f%%")

    plt.title("Soil Distribution")
    plt.ylabel("")

    plt.tight_layout()

    plt.savefig("static/chart3.png")
    plt.close()

    return render_template(
        "dashboard.html",
        chart1="static/chart1.png",
        chart2="static/chart2.png",
        chart3="static/chart3.png"
    )

if __name__ == "__main__":
    app.run(debug=True)