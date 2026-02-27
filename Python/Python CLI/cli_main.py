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
        else:
            print("Invalid choice")
    

def port_scanner():
    print("Welcome to the port scanner")
    print("Do you want to enter an ip or hostname?")
    choice = input(":> ")
    if "ip" in choice:
        print("What is the ip?")
        ip = input(":> ")
        test = socket.socket(ip)
        print(test)

    elif "hostname" in choice:
        print("What is the host name?")
        hostname = input(":> ")
        test = socket.socket(hostname)
        print(test)
    else:
        print("Invalid answer")
def hash_cracker():
    print("Welcome to the hash crack")
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

main()