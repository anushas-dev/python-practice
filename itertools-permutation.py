from itertools import permutations

given_word, k = input().split()
k = int(k)
possible_substr = list(permutations(given_word, k))
list_of_str = ["".join(x) for x in possible_substr]
list_of_str.sort()
for i in list_of_str:
    print(i)