
def hash_them(keys, values):
    arr = {}
    for i in range(0, len(keys)):
        if i < len(values):
            arr[keys[i]] = values[i]
        else:
            arr[keys[i]] = None
    return arr

print(hash_them(["Ivan", "Maria","gosho"], [1]))
