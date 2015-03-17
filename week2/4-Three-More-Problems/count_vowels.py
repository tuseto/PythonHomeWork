n = input("Enter string: ")

vowels = ["a","e","i","o","u","y","A","E","I","O","U","Y"]
counter = 0

for vowel in vowels:
    for letter in n:
        if vowel == letter:
            counter += 1
print(counter)
