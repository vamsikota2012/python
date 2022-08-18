plain_text = input("Enter plain text to encrypt:  ")
print(len(plain_text))
cipher_text = ''
for i in range(len(plain_text)-1,-1,-1):
    cipher_text = cipher_text + plain_text[i]
print(cipher_text)
