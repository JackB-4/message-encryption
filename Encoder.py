#Multiple Caesar Shift Encryption V1
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
    length = len(message)
    letters = []
    for x in range(0, length):
        letters.append(message[x])
    for y in range(0, length, 3):
        if letters[y] != ' ':
            letters[y] = chr(ord(letters[y]) + 5)
    for z in range(1, length, 3):
        if letters[z] != ' ':
            letters[z] = chr(ord(letters[z]) - 2)
    for a in range(2, length, 3):
        if letters[a] != ' ':
            letters[a] = chr(ord(letters[a]) + 7)
    print(*letters, sep= '')
    main()
def encrypt():
    message = input("Input the message you want encrypted.")
    length = len(message)
    letters = []
    for x in range(0, length):
        letters.append(message[x])
    for y in range(0, length, 3):
        if letters[y] != ' ':
            letters[y] = chr(ord(letters[y]) - 5)
    for z in range(1, length, 3):
        if letters[z] != ' ':
            letters[z] = chr(ord(letters[z]) + 2)
    for a in range(2, length, 3):
        if letters[a] != ' ':
            letters[a] = chr(ord(letters[a]) - 7)
    print(*letters, sep= '')
    main()

main()