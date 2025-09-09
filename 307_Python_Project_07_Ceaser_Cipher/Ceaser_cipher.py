import aphabets_list as al
import ceasar_cipher_logo as ccl

print(ccl.logo)

def encrypt(original_text, shift_amount):
    encode_str = ""
    for char1 in original_text:
        if char1 in al.alphabet:
            char_idx = al.alphabet.index(char1)
            final_char_idx = (char_idx + shift_amount) % len(al.alphabet)
            encode_str += al.alphabet[final_char_idx]
        else:
            encode_str += char1
    print(f"Encoded message: {encode_str}")

def decrypt(original_text, shift_amount):
    decode_str = ""
    for char1 in original_text:
        if char1 in al.alphabet:
            char_idx = al.alphabet.index(char1)
            final_char_idx = (char_idx - shift_amount) % len(al.alphabet)
            decode_str += al.alphabet[final_char_idx]
        else:
            decode_str += char1
    print(f"Decoded message: {decode_str}")

def caesar(direction):
    if direction in ['encode', 'decode']:
        original_text = input("Type your message:\n").lower()
        shift_amount = int(input("Type the shift number:\n"))
        if direction == 'encode':
            encrypt(original_text, shift_amount)
        else:
            decrypt(original_text, shift_amount)
    else:
        print("Wrong input!")

user_choice = True
while user_choice:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    caesar(direction)
    option = input("Do you want to continue? (Y or N): ").lower()
    user_choice = option == 'y'