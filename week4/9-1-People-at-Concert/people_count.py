from random  import randint, shuffle

def generate_test(count):
    names = ["Ivo", "Maria", "Anetta", "Philip", "Rado", "Gergana"]

    result = []

    for name in names:
        result = result + [name] * randint(1, count)
    
    shuffle(result)

    return result

print(generate_test(5))


def get_people_count(activity):
    unique = []
    for people in activity:
        if people not in unique:
            unique += [people]
    return len(unique)
print(get_people_count(generate_test(5)))
