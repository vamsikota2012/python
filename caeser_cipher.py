# Below 2 functions handle upper case letter
def caeser_encrypt_upper(text):
    result = ""
    for i in range(len(text)):
        char_position = ord(text[i])
        char_position = char_position - 65
        new_char_position = char_position + 13
        new_char_position = new_char_position % 26
        new_char_position = new_char_position +65
        result = result + chr(new_char_position)
    return result

print(caeser_encrypt_upper('SAMPLE'))

def caeser_decrypt_upper(encrypted_text):
    result = ""
    for i in range(len(encrypted_text)):
        char_position = ord(encrypted_text[i])
        char_position = char_position - 65
        new_char_position = char_position - 13
        new_char_position = new_char_position % 26
        new_char_position = new_char_position + 65
        result = result + chr(new_char_position)
    return result

print(caeser_decrypt_upper('FNZCYR'))


# Below 2 functions handle lower case letter

def caeser_encrypt(text):
    result = ""
    for i in range(len(text)):
        char_position = ord(text[i])
        char_position = char_position - 97
        new_char_position = char_position + 13
        new_char_position = new_char_position % 26
        new_char_position = new_char_position +97
        result = result + chr(new_char_position)
    return result


print(caeser_encrypt('sample'))

def caeser_decrypt(encrypted_text):
    result = ""
    for i in range(len(encrypted_text)):
        char_position = ord(encrypted_text[i])
        char_position = char_position - 97
        new_char_position = char_position - 13
        new_char_position = new_char_position % 26
        new_char_position = new_char_position + 97
        result = result + chr(new_char_position)
    return result

print(caeser_decrypt('fnzcyr'))

