def generate_final_report(crop, weather, market):

    score = 0
    
    if "Heavy" in weather:
        score += 25
    elif "Moderate" in weather:
        score += 20
    else:
        score += 10

    if "High" in market:
        score += 40
    elif "Medium" in market:
        score += 25
    else:
        score += 10

    if crop != "No suitable crop found":
        score += 30

    if score >= 80:
        risk = "Low Risk"
    elif score >= 50:
        risk = "Moderate Risk"
    else:
        risk = "High Risk"

    final_message = f"""
    Recommended Crop: {crop}

    Farm Intelligence Score: {score}/100

    Risk Level: {risk}

    AI Recommendation:
    Continue cultivation with optimized irrigation and market planning.
    """
    return final_message