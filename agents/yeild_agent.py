def predict_yield(crop, rainfall):

    if crop == "Rice":

        if rainfall > 75:
            return "Expected Yield: High"

        return "Expected Yield: Medium"

    elif crop == "Cotton":

        if rainfall > 40:
            return "Expected Yield: Good"

        return "Expected Yield: Moderate"

    elif crop == "Wheat":

        return "Expected Yield: Stable"

    return "Expected Yield: Average"