def possible_pairs(n, x):
    count = 0
    for i in range(1, n+1):
        for j in range(1, n+1):
            if i % j >= x:
                count += 1
    return count

test_cases = int(input())
for i in range(test_cases):
    n, r = map(int, input().split())
    
    left, right = 0, n-1
    while left < right:
        mid = (left + right + 1) // 2
        if possible_pairs(n, mid) >= r:
            left = mid
        else:
            right = mid - 1
    
    if possible_pairs(n, left) >= r:
        print(left)
    else:
        print(-1)
