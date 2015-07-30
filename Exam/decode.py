def decode_word(encrypted_word, cipher):
    dec_word = ''
    for el in encrypted_word:
        for key in cipher:
            if cipher[key] == el:
                dec_word += key
    return (dec_word)

print (decode_word("bbbbbbbbbbbbbbbbbbbbbbbbbbb", {'a': 'b'}))