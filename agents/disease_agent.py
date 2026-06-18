def detect_disease_risk(crop, rainfall):

    if crop == "Rice" and rainfall > 75:
        return "High fungal disease risk due to excess rainfall."

    elif crop == "Tomato" and rainfall > 65:
        return "Possible leaf infection risk detected."

    elif crop == "Cotton" and rainfall > 50:
        return "Moderate pest attack probability."

    return "Low disease risk."