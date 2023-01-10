# caesar cypher
def cls():
    print("\n" * 10)

# cls()

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']



def encrypt(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        position = alphabet.index(letter)
        new_position = position + shift_amount
        if new_position > 25:
            new_position = new_position - 26
        new_letter = alphabet[new_position]
        cipher_text += new_letter
    print(f"The encoded text is {cipher_text}")

def decrypt(encrypted_text, shift_amount):
    plain_text = ""
    for letter in encrypted_text:
        position = alphabet.index(letter)
        new_position = position - shift_amount
        if (new_position < 0):
            new_position = new_position + 26
        new_letter = alphabet[new_position]
        plain_text += new_letter
    print(f"Your decoded message is: {plain_text}")


    
direction = input("Type 'encode' to encrypt, 'decode' to decrypt: \n").lower()
word = (input('give me a word: ')).lower()
num = int(input('give me a number: '))

if direction == 'decode':
    decrypt(word, num)
elif direction == 'encrypt':
    encrypt(word, num)
else:
    print(f"Your inputs were invalid try again.")


####### THIS IS WORKING!!! ##############
#    moved = alphabet.index(char) + 3
#   print(f"now it's {alphabet[moved]}")
#########################################


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.
# def encrypt(direction, text, shift):
#     text_list = list(text)
#     if (direction == "encode"):
#         print(f"You chose to ENCODE your message")
#     else:
#         print("You want to DECODE your message")
#     print(f"Here is your message-as-a-list: {text_list}")
#     print(f"And you chose {shift} for your shift.")
#     print(text_list[0])
#     output_text = []
    # for t in text:
    #     output = text[t + shift]
    # print(f"Here is the encrypted message: {output}")

    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.  
    #e.g. 
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message. 

