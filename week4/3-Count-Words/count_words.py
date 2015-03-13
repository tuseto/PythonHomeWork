def count_words(words):
    arr = {}
    for word in words:
        if word in arr:
            arr[word] += 1
        else:
            arr[word] = 1
    return(arr)
            

print(count_words(["words", "are", "meaningful", "words", "words", "are"]))
