from sympy import randprime
def rsa_decode():
    i = 2
    p = 5
    q = 3
    print("What is the n?")
    n = int(input(":> "))
    print("What is the e?")
    e = int(input(":> "))
    print("What is the ciphered text?")
    c = int(input(":> "))

    while n % i != 0:
        i += 1
    p = i
    q = int(n / i)

    phi = (p - 1) * (q - 1)
    d = pow(e, -1, phi)

    private_key = (n, d)

    m = decrypt(private_key, c)
    byte_length = (m.bit_length() + 7) // 8
    msg_bytes = m.to_bytes(byte_length, 'big')
    print(m)
    print(f"The message is {msg_bytes}.")

def decrypt(private_key, c):
    n, d = private_key
    m = (c**d) % n
    return m





    
