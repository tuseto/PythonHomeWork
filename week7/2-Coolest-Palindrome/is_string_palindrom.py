def is_string_palindrom(string):
    string = string.lower()
    new_string = ""
    forbidden = [" ",",",".","!","?"]
    for el in string:
        if el not in forbidden:
            new_string += el
    if new_string == reverse(new_string):
        return True
    else:
        return False

def reverse(string):
    rev_string = ""
    for i in range(len(string)-1,-1,-1):
        rev_string += string[i]
    return(rev_string)


print(is_string_palindrom(" kapak! "))