print("CAESAR CIPHER")
special_char = ["!", "+", "-", "*", "@", "="]
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h",
            "i", "j", "k", "l", "m", "n", "o", "p",
            "q", "r", "s", "t", "u", "v", "w", "x",
            "y", "z"]
uppercase_alphabet = [letter.upper() for letter in alphabet]
print('The program supports the following characters: \n', alphabet, "\n", uppercase_alphabet, "\n", special_char)

print("Characters that are not letters will not be encoded.\n")

def encode(secret_message, shifting):
    encode_message = ''

    for char in secret_message:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            char_lower = char.lower()
            idx = alphabet.index(char_lower)
            new_idx = (idx + shifting) % len(alphabet)
            new_char = alphabet[new_idx]
            if is_upper:
                new_char = new_char.upper()
            encode_message += new_char
        elif char in special_char:
            encode_message += char
        else:
            print("The program does not support this character.")
            encode_message = None
            break
    return encode_message


def decode(secret_message, secret_code):
    decode_message = ''
    for char in secret_message:
        if char.lower() in alphabet:
            is_upper = char.isupper()
            char_lower = char.lower()
            idx = alphabet.index(char_lower)
            new_idx = (idx - secret_code) % len(alphabet)
            new_char = alphabet[new_idx]
            if is_upper:
                new_char = new_char.upper()
            decode_message += new_char
        elif char in special_char:
            decode_message += char
        else:
            print("The program does not support this character.")
            decode_message = None
            break
    return decode_message

def type_message_code():
    secret_message = input("Enter your message: ")
    while True:
        try:
            shifting = int(input("Enter shift: "))
            break
        except ValueError:
            print("Shift must be integer.")
            continue
    return secret_message, shifting

while True:
    choice = input("Enter 'encode' to encrypt, enter 'decode' to decrypt: ").strip()
    if choice == "encode":
        secret_message, shifting = type_message_code()
        encode_message = encode(secret_message, shifting)
        if encode_message != None:
            print(f"Here's the encoded result: {encode_message}")
    elif choice == "decode":
        secret_message, shifting = type_message_code()
        decode_message = decode(secret_message, shifting)
        if decode_message != None:
            print(f"Here's the decoded result: {decode_message}")
    else:
        print("You must enter encode or decode, nothing else.")
        continue


    again = input("Enter 'yes' if you want to go again. Otherwise program will be exit. ").lower()
    if again != "yes":
       break
