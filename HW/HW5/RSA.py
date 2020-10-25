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


def main():
    p = int(input("p: "))
    q = int(input("q: "))
    e = int(input("e: "))
    z = (p-1)*(q-1)
    n = p * q
    #find_d(e,1,z)
    d = find_d(e,1,z)
    print(d)
    print(RSA(d,39,n))
    print(RSA(937,667,2537))


main()
