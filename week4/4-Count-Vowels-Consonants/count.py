def count_vowels_consonants(word):
    vowels = "aeiouyAEIOUY"
    consonants = "bcdfghjklmnpqrstvwxzBCDFGHJKLMNPQRSTVWXZ"   
    arr = {
        "vowels": 0,
        "consonants": 0
        }  
    for letter in word:
       if letter in vowels:
           arr["vowels"] += 1
       elif letter in consonants:
            arr["consonants"] += 1
    return arr
            
print(count_vowels_consonants("aaaAcccD"))
    
