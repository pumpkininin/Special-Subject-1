def find_x(a, b, n):
    while(a<0):
        a+=n
        print("update a = ",a)
    if(a>n):
        a = a% n
        print("update a = ",a)
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
        quotient_arr.append(-int(n/a))
        remainder_arr.append(n%a)
        remainder = n % a
        n = a
        a = remainder
        if(remainder == 0):
            break
    # gcd is the remainder of the division before remainder = 0
    if(len(remainder_arr)==1):
        gcd = remainder_arr[0]
    else:
        gcd = remainder_arr[-2]

    if(gcd == 0):
        gcd = divisor_arr[-1]

    # create 2 list s_arr and r_arr to store all process in form d = n.s + a.r
    s_arr = [1 for i in range(len(quotient_arr))]
    r_arr = list()

    for i in range(len(quotient_arr)):
        r_arr.append(quotient_arr[i])
    # update 2 list r and s
    for i in range(3,len(quotient_arr)+1):
        s_arr[-i] = r_arr[-(i-1)]
        r_arr[-i] = r_arr[-i] * r_arr[-(i-1)] + s_arr[-(i-1)]
    # create a list named result to store all possible solution
    result = list()
    x0 = int(r_arr[0]*b/gcd)
    while True:
        if(x0 < 0):
            x0 += int(dividend_arr[0] / gcd)

            continue
        elif( 0<= x0 <= dividend_arr[0]):
            result.append(x0)
            x0 += int(dividend_arr[0] / gcd)
        else:
            break
    #print all process
    print("dividend  | divisor  | quotient | remainder")
    for i in range(len(dividend_arr)):
        print("{0:10d}|{1:10d}|{2:10d}|{3:10d}".format(dividend_arr[i], divisor_arr[i], -quotient_arr[i], remainder_arr[i]))
    print("GCD:",gcd)
    for i in range(2,len(dividend_arr)+1):
        print("step {5:3d}: {0:3d} = {1:3d}*({2:3d}) + {3:3d}*({4:3d})".format(gcd, dividend_arr[-i],s_arr[-i], divisor_arr[-i], r_arr[-i],i-1))
    print("X0 = {0:5d}*{1:5d}/{2:5d} = {3:5d} (mod {4:5d}/{2:5d})".format(r_arr[0],b,gcd, result[0],dividend_arr[0]))
    print("All posibble solution: ", result)



def main():
    print("find x where a*x = b mod n")
    a = int(input("enter a: "))
    b = int(input("enter b: "))
    n = int(input("enter n: "))
    find_x(a,b,n)


main()