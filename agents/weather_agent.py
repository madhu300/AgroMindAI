def analyze_weather(rainfall):

    if rainfall > 75:
        return "Heavy rainfall expected. Reduce irrigation."

    elif rainfall > 50:
        return "Moderate rainfall conditions."

    else:
        return "Low rainfall detected. Increase water management."