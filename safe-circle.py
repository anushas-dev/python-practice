n, k = map(int, input().split())

def safe_circle(person,k):
    if person==1:
        return 1
    else:
        return (safe_circle(person - 1, k) + k - 1) % person + 1

print(safe_circle(n,k))