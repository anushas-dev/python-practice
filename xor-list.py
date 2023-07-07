from functools import reduce
N = int(input())

uc = []
vc= []
for i in range(N-1):
    u, v = map(int, input().split())
    uc.append(u)
    vc.append(v)
xor_result = list(a^b for a,b in zip(uc,vc))
print(xor_result)
result = reduce(lambda x, y: x ^ y, xor_result)

print(result)