import random
import encode as e
import decode as d


def rsa_main():
    print("Would you like to decode or encode a message.")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = int(input(":> "))
    if choice == 1:
        e.rsa_encode()
    elif choice == 2:
        d.rsa_decode()
    else:
        print("Auf wiedersehen")

rsa_main()