import base64
def main():
    #main accepts no arguements
    #it takes input from the user to see if they want to decode or encode their string
    #it runs the function they want

    #make them run it atleast once
    again = True

    #loop until they said quit
    while again == True:
        print()
        print("Welcome to the Base64 cipher.")
        print("What would you like to do?")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        choice = int(input(":> "))
        if choice == 1:
            encode64()
        elif choice == 2:
            decode64()
        elif choice == 3:
            print("Auf Weidersehen!")
            again = False
        else:
            print("Invalid Choice")
            print("Try again")
            print()
    
def encode64():
    #encode64 accepts no arguements
    #it asks the user for a message they want to encode
    #it encodes it with base64
    #it outputs the decoded message

    #take input
    print("What text would you like to encrypt?")
    message = input(":> ")

    #encode the string into bytes
    data_bytes = message.encode('utf-8')

    #encode the bytes into base64
    encoded_message = base64.b64encode(data_bytes)

    #decode the base64 bytes into base64 string
    base64message = encoded_message.decode('utf-8')

    #output it
    print(f"{message} in base64 is {base64message}")

def decode64():

    print("What is your ciphered text that you would like to decode?")
    encrypted_message = input(":> ")

    #encode into bytes
    base_byte_data = encrypted_message.encode('utf-8')

    #decode the byte 64 into just byte
    byte_data = base64.b64decode(base_byte_data)

    #decode the bytes into a string
    message = byte_data.decode('utf-8')

    #output results
    print(f"Your encrypted message {encrypted_message} is {message}.")

main()