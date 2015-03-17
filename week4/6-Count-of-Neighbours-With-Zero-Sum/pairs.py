def count_zero_neighbours(numbers):
    count = 0
    for i in range(0, len(numbers)-1):
        if numbers[i] + numbers[i + 1] == 0:
                count += 1
    return count

print(count_zero_neighbours([1,2,1,-2,0,0]))
