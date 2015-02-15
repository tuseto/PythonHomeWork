searched_word = input("Enter word: ")
n = int(input("Enter number: "))

count = 1
numbers = []
words_list = []

while count <= n:
    word = input("Enter word: ")
    words_list = words_list + [word]
    count += 1
    
count = 0
include_times = 0

while count <= n - 1:
    if searched_word in words_list[count]:
        include_times += 1
    count += 1
print(str(searched_word) + " is found " + str(include_times) + " times")


    
    

    

    

   





