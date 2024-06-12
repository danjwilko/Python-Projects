alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p',
            'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
def caeser(start_text, shift_amount, cipher_direction):
    end_text = ''
    if cipher_direction == 'decode':
        shift_amount *= -1
    for letter in start_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        end_text = end_text + alphabet[new_position]
    print(f"The {cipher_direction}d text is {end_text}")


""" My verson was this:
def caeser(text, shift):
    encode_string = ''
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            if direction == 'encode':
                index = (position + shift)
            else:
                index = (position - shift)
            encode_letter = alphabet[index]
            encode_string = encode_string + encode_letter
    print(encode_string)"""

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
caeser(start_text=text, shift_amount=shift, cipher_direction=direction)
