from sympy import randprime

def rsa_encode():
    #get two random prime numbers
    p = is_prime()
    q = is_prime()

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
        e_choice = int(input(":> "))
        e = e_choice
    else:
        e = 65537
    d = 1
    d = pow(e, -1, phi)
    print("What message do you want to encode")
    m = input(":> ")
    encoded_m = int.from_bytes(m.encode(), "big")
    public_key = (n, e)
    private_key = (n, d)
    encrypted = encrypt(encoded_m, public_key)
    print(f"your text was translated into {encrypted}")
    print(n)

def encrypt(encoded_m, public_key):
    n, e = public_key
    return pow(encoded_m, e, n)
    
def is_prime():
    num = randprime(2**255, 2**256)
    return num
