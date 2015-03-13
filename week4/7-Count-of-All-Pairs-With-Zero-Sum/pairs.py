def count_zero_pairs(numbers):
    count = 0
    for i in range(0, len(numbers)):
        for n in range(i, len(numbers)):
            if numbers[i] + numbers[n] == 0:
                count += 1
    return count

print(count_zero_pairs([0, 2, -2, 5, 10]))
