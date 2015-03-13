def winter_is_coming(seasons):
    counter = 0
    for season in seasons:
        if season == "winter":
            counter = 0
        counter += 1
    return counter >= 5

print(winter_is_coming(["summer", "winter", "summer",
                        "summer", "summer",
                        "summer", "summer"]))
