def str_reverse(string):
    new_string = ""
    for i in range(len(string)-1,-1,-1):
        new_string += string[i]
    return(new_string)

def join(delimiter,items):
    string = ""
    for i in range(0,len(items)):
        string += str(items[i])
        if i < len(items)-1:
            string += delimiter
    return(string)

def startswitch(search,string):
    for i in range(0,len(search)):
        if search[i] != string[i]:
            return False
    return True

def endswith(search,string):
    rev_search = str_reverse(search)
    rev_string = str_reverse(string)
    return(startswitch(rev_search,rev_string))

def trim(string):
    while startswitch(" ",string):
        new_string = ""
        for i in range(1,len(string)):
            new_string += string[i]
        string = new_string
    
    while endswith(" ",string):
        new_string = ""
        for i in range(0,len(string)-1):
            new_string += string[i]
        string = new_string
    return(string)




print(trim("     ba baka pak    "))
