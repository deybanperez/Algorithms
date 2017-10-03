import math
number1 = 3141592653589793238462643383279502884197169399375105820974944592
number2 = 2718281828459045235360287471352662497757247093699959574966967627

def karatsuba(n1, n2):
    if n1 < 10 or n2 < 10:
        return n1*n2

    l_max = max(len(str(n1)), len(str(n2)))
    l_max2 = math.ceil(l_max/2)
    pow_div = pow(10, l_max2)

    a = n1 // pow_div
    b = n1 % pow_div
    c = n2 // pow_div
    d = n2 % pow_div

    s1 = karatsuba(a, c)
    s2 = karatsuba(b, d)
    s3 = karatsuba(a+b, c+d)
    s4 = s3 - s2 - s1;
    return (pow(10, (l_max2 * 2)) * s1) + (pow_div * s4) + s2

result = karatsuba(number1, number2)

print("Result is: " + str(result))
