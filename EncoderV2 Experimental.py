#Multiple Caesar Shift Encryption V2 Experimental
#JackB-4
def main():
    decision = input("Would you like to encrypt or decrypt? (Say either encrypt, decrypt, or exit)")
    if decision == "encrypt":
        encrypt()
    elif decision == "decrypt":
        decrypt()
    elif decision == "exit":
        quit()
    else:
        main()
def decrypt():
    message = input("Input the message you want decrypted.")
    key = input("Input the encryption key for the message. (4 digit number, no spaces)")
    length = len(message)
    letters = []
    for x in range(0, length):
        letters.append(message[x])
    for y in range(0, length, 4):
        if letters[y] != ' ':
            letters[y] = chr(ord(letters[y]) + int(key[0]))
    for z in range(1, length, 4):
        if letters[z] != ' ':
            letters[z] = chr(ord(letters[z]) - int(key[1]))
    for a in range(2, length, 4):
        if letters[a] != ' ':
            letters[a] = chr(ord(letters[a]) + int(key[2]))
    for t in range(2, length, 4):
        if letters[t] != ' ':
            letters[t] = chr(ord(letters[t]) - int(key[3]))
    print(*letters, sep= '')
    main()
def encrypt():
    key = input("Create an encryption key. 4 digit number, no spaces.")
    message = input("Input the message you want encrypted.")
    length = len(message)
    letters = []
    for x in range(0, length):
        letters.append(message[x])
    for y in range(0, length, 4):
        if letters[y] != ' ':
            letters[y] = chr(ord(letters[y]) - int(key[0]))
    for z in range(1, length, 4):
        if letters[z] != ' ':
            letters[z] = chr(ord(letters[z]) + int(key[1]))
    for a in range(2, length, 4):
        if letters[a] != ' ':
            letters[a] = chr(ord(letters[a]) - int(key[2]))
    for t in range(2, length, 4):
        if letters[t] != ' ':
            letters[t] = chr(ord(letters[t]) + int(key[3]))
    print(*letters, sep= '')
    main()

main()