print("CAESAR CIPHER")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

def encode(secret_message,secret_code):
    encode_message = ''
    for char in secret_message:
        if char.isalpha():
            is_upper = char.isupper()
            char_lower = char.lower()
            idx = alphabet.index(char_lower)
            new_idx = (idx + secret_code) % len(alphabet)
            new_char = alphabet[new_idx]
            if is_upper:
                new_char = new_char.upper()
            encode_message += new_char
        else:
            encode_message += char
    return encode_message


def decode(secret_message, secret_code):
    decode_message = ''
    for char in secret_message:
        if char.isalpha():
            is_upper = char.isupper()
            char_lower = char.lower()
            idx = alphabet.index(char_lower)
            new_idx = (idx - secret_code) % len(alphabet)
            new_char = alphabet[new_idx]
            if is_upper:
                new_char = new_char.upper()
            decode_message += new_char
        else:
            decode_message += char
    return decode_message
def type_message_code():
    secret_message = input("Enter your message: ")
    secret_code = int(input("Enter secret code: "))
    return secret_message,secret_code

while True:
    choice = input("Enter 'encode' to encrypt, enter 'decode' to decrypt: ")
    if choice == "encode":
        secret_message, secret_code = type_message_code()
        encode_message = encode(secret_message,secret_code)
        print(f"Here's the encoded result: {encode_message}")
    elif choice == "decode":
        secret_message, secret_code = type_message_code()
        decode_message = decode(secret_message,secret_code)
        print(f"Here's the decoded result: {decode_message}")
    else:
        print("You must enter encode or decode,nothing else.")
        continue


    again = input("Enter 'yes' if you want to go again. Otherwise program will be exit. ").lower()
    if again != "yes":
       break
