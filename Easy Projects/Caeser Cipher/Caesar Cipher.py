from alphabet_list import alphabet as alphabet
from art import logo as logo


def encrypt(text, shift):
    coded = []
    for letter in text:
        if letter not in alphabet:
            coded.append(str(letter))
        else:
            coded.append(alphabet.index(letter) + shift)  # find the original index of the letter, then what it would be shifted n times
        # 'hello' would return [7,4,11,11,14] shift 5 to each of those numbers, [12,9,16,16,19]
    for index in range(len(coded)): # using range so i can swap out the values of indexes
        if type(coded[index]) == str:
            pass
        else:
            coded[index] = alphabet[coded[index] % (len(alphabet))]
        # the index now equals -> a letter in the alphabet indicated as ('hello' example above),
        # alphabet[12], alphabet[9], alphabet[16], etc.
        # the modulus operator ensures that if a letter is shifted to a point where an index does not exist,
        # it will start counting from beginning of list. For example the letter 'z' shifted once would end up at index
        # 26, which does not exist. However index 25 % 25(This is the length of the list) == 0, which starts you
        # back at the beginning of the list. If the 2nd number is larger than the first in modulus, it just returns
        # the first number. So, 5 % 6 = 5, 6 % 6 = 0, and 6 % 5 = 1. aka working forwards**

    print(f"The encoded text is: {''.join(coded)}")


def decrypt(text, shift):
    decoded = []
    for letter in text:
        if letter not in alphabet:
            decoded.append(str(letter))
        else:
            decoded.append(alphabet.index(letter) - shift)
    for index in range(len(decoded)):
        if type(decoded[index]) == str:
            pass
        else:
            decoded[index] = alphabet[decoded[index] % (len(alphabet))]  # -1 % 26 = 25
        # for negative numbers modulus just subtracts the first number from the second -7 % 10 = 3 aka working backwards***
    print(f"The decoded text is: {''.join(decoded)}")


def program_choice(direction, text, shift):
    if direction == 'encode':
        encrypt(text, shift)
    elif direction == 'decode':
        decrypt(text, shift)


print(logo)

run = True
while run:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt, or type 'exit' to exit:\n")

    if direction == 'encode' or direction == 'decode':
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        program_choice(direction, text, shift)
        run_again = input("Would you like to run again? (Y/N) ").lower()
        if run_again == 'y':
            continue
        else:
            break
    elif direction == 'exit':
        exit()
    else:
        print("Invalid response, please try again.")

