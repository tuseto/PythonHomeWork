def max_score(beers, fries):
    beers = sorted(beers)
    fries = sorted(fries)
    max_value = 0
    for i in range(0, len(beers)):
        max_value += beers[i] * fries[i]
    return max_value

print(max_score([1000, 1010, 1020, 1030, 1040], [834, 500, -1, 0, 60]))
