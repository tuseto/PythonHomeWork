def forecast(days):
    sunshine = 0
    rain = 0
    snow = 0
    for el in days:
        if el == "sunshine":
            sunshine += 1
        elif el == "rain":
            rain += 1
        elif el == "snow":
            snow += 1
    if sunshine > rain and sunshine > snow:
        return("sunshine")

    elif rain > snow and rain > sunshine:
        return("rain")

    elif snow > rain and snow > sunshine:
        return("snow")

    elif snow == rain and snow == sunshine:
        return(days[len(days)-1])
    if snow == rain and snow > sunshine:
        return("sunshine")
    if snow == sunshine and snow > rain:
        return("rain")
    if rain == sunshine and rain >snow:
        return("snow")

print(forecast(["snow", "snow", "rain", "sunshine"]))