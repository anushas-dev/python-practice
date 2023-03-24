from collections import defaultdict

d = defaultdict(list)
group_a_size, group_b_size = map(int, input().split())

for i in range(1,group_a_size+group_b_size+1):
    _add = input()
    if i <= group_a_size:
        d['group_a'].append(_add)
    if i > group_a_size:
        d['group_b'].append(_add)

group_a = list(d.items())[0][1]
group_b = list(d.items())[1][1]

list_of_indices = []
final_list = []
l = 0
for i in range(group_b_size):
    l = 0
    for j in range(group_a_size):
        if group_b[i] == group_a[j]:
            list_of_indices.extend({j+1})
            l+= 1
    if l < 1:
        a = -1
        list_of_indices.extend({a})
    final_list.append(list_of_indices)
    list_of_indices = []

for _ in range(group_b_size):
    print(*final_list[_],sep=" ")