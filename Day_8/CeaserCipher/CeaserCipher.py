from art import logo

def find_pos(char, alphabet):
    i = 0
    for x in alphabet:
        if (char == x):
            break
        i += 1
    return (i)

def ceaser(alphabet, text, shift):
     string = ""
     for char in text:
         string += alphabet[( find_pos(char, alphabet) + shift ) % 26]
     return (string)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

work = True
print(logo)
while work:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int( input("Type the shift number:\n") )
    if (direction == "encode"):
        print("Your encode: " + ceaser(alphabet, text, shift))
    elif (direction == "decode"):
        print(f"Your decode:"+ ceaser(alphabet, text, shift * -1))
    key = input("Do you want to continue? (yes or no)\n").lower()
    if (key == "yes"):
         work = True
    else:
         work = False
