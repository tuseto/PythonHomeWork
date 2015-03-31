
def starts_with(string):
        if string[0] == " ":
            return True
        else:
            return False

def ends_with(string):
        if string[len(string)-1] == " ":
            return True
        else:
            return False

def trim_left(string):
    while starts_with(string):
        new_string = ""
        for i in range(1,len(string)):
            new_string += string[i]
        string = new_string
    return (string)

def trim_right(string):
    while ends_with(string):
        new_string = ""
        for i in range(0,len(string)-1):
            new_string += string[i]
        string = new_string
    return (string)

def trim(string):
    string = trim_left(string)
    string = trim_right(string)
    new_string = ""
    for i in range(0,len(string)):
        if string[i] != " " or string[i+1] != " ":
            new_string += string[i]
    return(new_string)

#---------With continue operator
#
# def trim(string):
#     string = trim_left(string)
#     string = trim_right(string)
#     new_string = ""
#     for i in range(0,len(string)):
#         if string[i] == " " and string[i+1] == " ":
#             continue
#         else:
#             new_string += string[i]
#     return(new_string)


print(trim("Python   Django"))