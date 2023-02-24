def caeser_text_create(inputtext, shift, action):
    output_text = ""
    for letter in text:
        if letter in alphabet:
            if (action == 'decode'):
                input_index = (alphabet.index(letter) - shift) % 26
            else:
                input_index = (alphabet.index(letter) + shift) % 26
            cipher_letter = alphabet[input_index]
        else:
            cipher_letter = letter
        output_text += cipher_letter
    print(f"Original text : {text}")
    print(f"{action}d text : {''.join(output_text)}")


alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

continueEncoding = "Y"
while (continueEncoding == "Y"):
    action = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if (action != "encode" and action != "decode"):
        print("Invalid action")
    else:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caeser_text_create(text, shift, action)
    continueEncoding = input("Do you wish to continue ?  Y or N : ")
