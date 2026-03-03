import socket
import time
import threading
def main():
    choice = 0
    while choice != 7:
        print("Welcome to the Python CLI")
        print("What would you like to do?")
        print("1. Port Scanner")
        print("2. Hash Cracker")
        print("3. RSA Tool")
        print("4. Web Scanner")
        print("5. Ciphers")
        print("6. File Forensics")
        print("7. Quit")
        choice = int(input(":> "))
        if choice == 1:
            port_scanner()
        elif choice == 2:
            hash_cracker()
        elif choice == 3:
            rsa_tool()
        elif choice == 4:
            web_scanner()
        elif choice == 5:
            ciphers()
        elif choice == 6:
            file_forensics()
        elif choice == 7:
            break            
        else:
            print("Invalid choice")
    print("Auf Wierdesehen")
    

def port_scanner():
    # port_scanner takes no input
    # it asks the user for the ip or hostname
    # it then asks the user if they want to use a specific port or no
    # if they say yes than it takes input from the user for the port they want to use
    # it tries to connect to that port and outputs if it is open
    # else if the user doesnt want to manually input a port
    # it makes a for loop and tries every port in the for loop
    # it outputs which ports worked
    print("Welcome to the port scanner")
    print("What is the ip or hostname?")
    try:
        target = input(":> ")
        print("Would you like to input a specific port(y/n)?")
        choice = input(":> ")
        if "y" in choice:
            print("What port would you like to check?")
            port = int(input(":> "))
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.settimeout(1)
            try:
                s.connect((target, port))
                print(f"Port {port} is open")
            except:
                print(f"Port {port} is closed.")
        elif "n" in choice:
            port = 0
            filler = 0
            for port in range(1, 2025):
                s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                s.settimeout(.2)
                try:
                    s.connect((target, port))
                    print(f"Port {port} is open")
                except:
                    filler += 1
            s.close()
        else:
            print("Invalid input")
    except:
        print("There was an error")
    print()
def hash_cracker():
    print("Welcome to the hash crack")
    print("Would you like to encrypt or decrypt a hash.")
    choice = input(":> ")
    if "d" in choice:
        decrypter = hash_decrypter()
    elif "e" in choice:
        encrypted = hash_encrypter()
    else:
        print("Invalid")
def rsa_tool():
    print("Welcome to the rsa tool")
    print("What would you like to do?")
    print("1. Encrypt")
    print("2. Decrypt")
    choice = int(input(":> "))
def web_scanner():
    print("Welcome to the web scanner")
def ciphers():
    print("Welcome to the cipher main")
def file_forensics():
    print("Welcome to the file forensics main")

def hash_encrypter():
    print()
def hash_decrypter():
    print("Did you put the hash on default.txt(y/n)?")
    choice = input(":> ")
    if "y" in choice:
        inFile = open("default.txt", "r")
        password = inFile.read()
        if password == " ":
            print("There is nothing on default.txt")
        else:
            length = len(password)
            if length == 32:
                print()
    elif "n" in choice:
        print()
main()