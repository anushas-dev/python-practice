from collections import deque

tasks = int(input())

d = deque()
for i in range(tasks):
    t = input()
    if 'append' in t or 'appendleft' in t:
        task, n = t.split()
    else:
        task = t   
    if task == 'append':
        d.append(int(n))
    if task == 'appendleft':
        d.appendleft(int(n))
    if task == 'pop':
        d.pop()
    if task == 'popleft':
        d.popleft()
for e in d:
    print(e, end=" ")