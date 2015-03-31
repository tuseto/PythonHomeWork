def taken_name(surname_husband,surname_wife):
    counter = 0
    pointer = 0
    for el in surname_wife:
        counter=0
        if surname_husband[0] == el:
            for i in range(0, len(surname_husband)):
                if surname_husband[i] == surname_wife[pointer + i]:
                    counter += 1

        if counter == len(surname_husband):
            return True

        pointer += 1
    return False


print(taken_name("Petrov", "Ivanova-Petrova"))
