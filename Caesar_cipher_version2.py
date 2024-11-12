import art
print(art.logo)

alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
            "v", "w", "x", "y", "z"]

def caesar(secret_message,secret_code,choice):
    output_message = ''
    if choice == "decode":
        secret_code *= - 1
    for char in secret_message:
        if char.isalpha():
            is_upper = char.isupper()
            char_lower = char.lower()
            idx = alphabet.index(char_lower)
            new_idx = (idx + secret_code) % len(alphabet)
            new_char = alphabet[new_idx]
            if is_upper:
                new_char = new_char.upper()
            output_message += new_char
        else:
            output_message += char
    print(f"Here is the {choice}d result: {output_message}")

while True:
    choice = input("Enter 'encode' to encrypt, enter 'decode' to decrypt: ")
    if choice == "encode" or choice == "decode":
        secret_message = input("Enter your message: ")
        secret_code = int(input("Enter secret code: "))
        caesar(secret_message, secret_code, choice)
    else:
        print("You must enter encode or decode,nothing else.")
        continue


    again = input("Enter 'yes' if you want to go again. Otherwise program will be exit. ").lower()
    if again != "yes":
        print("Goodbye!")
        break