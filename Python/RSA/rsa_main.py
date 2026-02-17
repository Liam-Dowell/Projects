import random
from sympy import randprime


def rsa_main():
    print("Would you like to decode or encode a message.")
    print("1. Encode")
    print("2. Decode")
    print("3. Quit")
    choice = int(input(":> "))
    if choice == 1:
        rsa_encode()
    elif choice == 2:
        rsa_decode()
    else:
        print("Auf wiedersehen")

def rsa_encode():
    #get two random prime numbers
    p = is_prime()
    q = is_prime()

    print(q)
    print(p)

    #make sure they dont equal each other
    while p == q:
        q = 0
        q = is_prime()
    n = p * q

    #do euler's totient 
    phi = (p - 1)  * (q - 1)
    print("Do you want to use the default public key 65537(y/n)?")
    choice = input(":> ")
    if choice == "n":
        print("Enter your public key you want to use.")
        public_key = int(input(":> "))
        e = public_key
    else:
        e = 65537
    print("test")
    d = 1
    mod = False
    while mod == False:
        check = e * d % phi
        if check == 1:
            mod = True
        else:
            d += 1
    print(d)
    print("What message do you want to encode")
    m = input(":> ")
    encoded_m = int.from_bytes(m.encode(), "big")
    print(encoded_m)
        

def rsa_decode():
    print("fajfo")
    
def is_prime():
    num = randprime(2**127, 2**128)
    return num

rsa_main()