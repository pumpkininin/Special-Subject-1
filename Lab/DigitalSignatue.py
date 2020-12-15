import random as rd

def is_prime(a):
    if a == 2:
        return True
    if a < 2 or a % 2 == 0:
        return False
    for n in range(3, int(a**0.5)+2, 2):
        if a % n == 0:
            return False
    return True

def find_d(a,b,n):

    while (a < 0):
        a += n
        print("update a = ", a)
    if (a > n):
        a = a % n
        print("update a = ", a)
    while (b < 0):
        b += n
        print("update b = ", b)
    if (b > n):
        b = b % n
        print("update b = ", b)

    divisor_arr = list()
    dividend_arr = list()
    quotient_arr = list()
    remainder_arr = list()
    # keep dividing till remainder = 0 and store all process in 4 list
    while True:
        dividend_arr.append(n)
        divisor_arr.append(a)
        quotient_arr.append(-int(n / a))
        remainder_arr.append(n % a)
        remainder = n % a
        n = a
        a = remainder
        if (remainder == 0):
                break
    # gcd is the remainder of the division before remainder = 0
    if (len(remainder_arr) == 1):
        gcd = remainder_arr[0]
    else:
        gcd = remainder_arr[-2]

    if (gcd == 0):
        gcd = divisor_arr[-1]

    # create 2 list s_arr and r_arr to store all process in form d = n.s + a.r
    s_arr = [1 for i in range(len(quotient_arr))]
    r_arr = list()

    for i in range(len(quotient_arr)):
        r_arr.append(quotient_arr[i])
    # update 2 list r and s
    for i in range(3, len(quotient_arr) + 1):
        s_arr[-i] = r_arr[-(i - 1)]
        r_arr[-i] = r_arr[-i] * r_arr[-(i - 1)] + s_arr[-(i - 1)]

    d = r_arr[0]
    if(d < 0):
        d = d + dividend_arr[0]
    return d

def RSA(d,c,n):
    remainder_arr = list()
    while not d == 0:
        remainder_arr.append(d%2)
        d = int(d/2)
    mod_arr = list()
    for i in range(len(remainder_arr)):
        if(remainder_arr[i] == 0):
            continue
        else:
            pow = 2**i
            mod_arr.append(c**pow % n)
    result = 1
    for i in mod_arr:
        result *= i
    result = result % n
    return result

def coprime(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def encrypt(private_key, mess):
    d, n =private_key
    cipher = [pow(ord(char), d, n) for char in mess]
    return cipher


def decrypt(public_key, encrypted_mess):
    e, n = public_key
    messChar = [chr(pow(char, e, n)) for char in encrypted_mess]

    # Return the array of bytes as a string
    return ''.join(messChar)


def main():
    while True:
        p = int(input("Enter a prime number (p): "))
        if not (is_prime(p)):
            print("Not a prime number. Try agian!")
            continue
        else:
            break
    while True:
        q = int(input("Enter another prime number (q): "))
        if not(is_prime(q)):
            print("Not a prime number. Try agian!")
            continue
        else:
            break
    z = (p-1)*(q-1)
    n = p * q
    #choose e
    e = rd.randrange(1, z)
    while coprime(e, z) != 1:
        e = rd.randrange(1, z)
    print(e)
    #find_d(e,1,z)
    d = find_d(e,1,z)
    #public key (e,n) private key(d,n)
    print("your public key is ({0:d}, {1:d}) and private key is ({2:d}, {1:d})".format(e,n,d))
    mess = str(input("Enter the message to encrypt: "))
    e_mess = encrypt((d,n), mess)
    print(''.join(map(lambda x: str(x), e_mess)))
    d_mess = decrypted_msg = decrypt((e,n), e_mess)
    print("Your decrypted message is: ")
    print(d_mess)
    if(mess == d_mess):
        print("successful")
    else:
        print("error")



main()
