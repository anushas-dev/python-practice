from itertools import combinations
given_word, k = input().split()
k = int(k)

given_word = list(given_word)
given_word.sort()
given_word = "".join(given_word)
for i in range(1,k+1):
    possible_list = list(combinations(given_word, i))
    list_to_sort = ["".join(x) for x in possible_list]
    list_to_sort.sort()
    for i in list_to_sort:
        print(i)