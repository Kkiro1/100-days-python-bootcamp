from art import logo
import string

print(logo)

def caesar_cipher(direction, text, shift) -> str:
    alphabet = string.ascii_lowercase
    result = ""
    
    shift = shift % 26
    
    for ch in text.lower():
        if ch.isalpha():
            old_place = alphabet.index(ch)
            if direction == "encode":
                new_place = (old_place + shift) % 26
            elif direction == "decode":
                new_place = (old_place - shift) % 26
            else:
                result += ch
                continue
            result += alphabet[new_place]
        else:
            # Keep spaces, numbers, punctuation unchanged
            result += ch
    
    return result
        
            
print("Welcome to the Caesar Cipher!\n")

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").strip().lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

final_text = caesar_cipher(direction, text, shift)

if direction == "encode":
    print(f"\nHere's the encoded result: {final_text}")
elif direction == "decode":
    print(f"\nHere's the decoded result: {final_text}")
else:
    print("Invalid direction! Please type 'encode' or 'decode'.")