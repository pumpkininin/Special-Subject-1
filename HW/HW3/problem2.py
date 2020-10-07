def find_x(a, b, n):
    divisor_arr = list()
    dividend_arr = list()
    quotient_arr = list()
    remainder_arr = list()
    while True:
        dividend_arr.append(n)
        divisor_arr.append(a)
        quotient_arr.append(int(n/a))
        remainder_arr.append(n%a)
        remainder = n % a
        n = a
        a = remainder
        if(remainder == 0):
            break
    for i in range(1,len(dividend_arr)+1):
        string = str(remainder_arr[-i]) + " = " + str(dividend_arr[-i]) + " - " + str(divisor_arr[-i]) + " *"+ str(quotient_arr[-i])
        print(string)

def main():
    a = 28
    b = 8
    n = 48
    print(find_x(a,b,n))


main()