def find_x(a, b, n):
    divisor_arr = list()
    dividend_arr = list()
    quotient_arr = list()
    remainder_arr = list()
    while True:
        dividend_arr.append(n)
        divisor_arr.append(a)
        quotient_arr.append(-int(n/a))
        remainder_arr.append(n%a)
        remainder = n % a
        n = a
        a = remainder
        if(remainder == 0):
            break
    remainder_string_arr = list()
    for i in range(len(dividend_arr)):
        string = str(remainder_arr[i]) + " = " + str(dividend_arr[i]) + " + " + str(divisor_arr[i]) + " *"+ "("+str(quotient_arr[i])+")"
        remainder_string_arr.append(string)
        print(string)
    print(remainder_string_arr)
    s_arr = [1 for i in range(len(quotient_arr))]
    r_arr = list()
    tmp = [1 for i in range(len(quotient_arr))]

    for i in range(len(quotient_arr)):
        r_arr.append(quotient_arr[i])
    for i in range(3,len(quotient_arr)+1):
        s_arr[-i] = r_arr[-(i-1)]

        r_arr[-i] = r_arr[-i] * r_arr[-(i-1)] + s_arr[-(i-1)]

    print(s_arr)
    print(r_arr)

def main():
    a = 28
    b = 8
    n = 48
    print(find_x(a,b,n))


main()