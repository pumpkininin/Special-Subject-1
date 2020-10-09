def find_x(a, b, n):
    sub_n = n
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
    gcd = remainder_arr[-2]
    s_arr = [1 for i in range(len(quotient_arr))]
    r_arr = list()
    tmp = [1 for i in range(len(quotient_arr))]

    for i in range(len(quotient_arr)):
        r_arr.append(quotient_arr[i])
    for i in range(3,len(quotient_arr)+1):
        s_arr[-i] = r_arr[-(i-1)]
        r_arr[-i] = r_arr[-i] * r_arr[-(i-1)] + s_arr[-(i-1)]
    result = list()
    x0 = int(r_arr[0]*b/gcd)
    while True:
        x0 += int(dividend_arr[0]/gcd)
        if(x0 > 0 and x0 < dividend_arr[0]):
            result.append(x0)
        else:
            break

    print(result)
    print("dividend  | divisor  | quotient | remainder")
    for i in range(len(dividend_arr)):
        print("{0:10d}|{1:10d}|{2:10d}|{3:10d}".format(dividend_arr[i], divisor_arr[i], quotient_arr[i], remainder_arr[i]))
    print("GCD:",gcd)
    for i in range(2,len(dividend_arr)+1):
        print("step {5:3d}: {0:3d} = {1:3d}*({2:3d}) + {3:3d}*({4:3d})".format(gcd, dividend_arr[-i],s_arr[-i], divisor_arr[-i], r_arr[-i],i-1))
    print("X0 = {0:3d}*{1:3d}/{2:3d} = {3:3d} (mod {4:3d}/{2:3d})".format(r_arr[0],b,gcd, result[0],dividend_arr[0]))
    print("All posibble solution: ", result)
def main():
    a = 28
    b = 8
    n = 48
    find_x(a,b,n)


main()