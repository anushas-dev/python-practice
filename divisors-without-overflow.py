def count_divisors_without_overflow(X):
    count = 0
    for D in range(1, X+1):
        quotient = X // D
        if bin(quotient)[2:].count('1') <= bin(D)[2:].count('1'):
            count += 1
    print(count)

count_divisors_without_overflow(5)