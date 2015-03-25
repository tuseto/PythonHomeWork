def head(arr):
    return(arr[0])

def last(arr):
    return(arr[len(arr)-1])

def tail(arr):
    new_arr = []
    for i in range(1,len(arr)):
        new_arr += [arr[i]]
    return(new_arr)

def equal_lists(arr1,arr2):
    if len(arr1) == len(arr2):
        for i in range(0,len(arr1)):
            if arr1[i] != arr2[i]:
                return False
    else:
        return False
    return True

def count_item(element,arr):
    counter = 0
    for el in arr:
        if element == el:
            counter += 1
    return (counter)

def take(number,arr):
    new_arr = []
    for i in range(0,min(number,len(arr))):
        new_arr += [arr[i]]
    return (new_arr)

def drop(number,arr):
    new_arr = []
    for i in range(number,len(arr)):
        new_arr += [arr[i]]
    return(new_arr)

def reverse(arr):
    rev_arr = []
    for i in range(len(arr)-1,-1,-1):
        rev_arr += [arr[i]]
    return(rev_arr)