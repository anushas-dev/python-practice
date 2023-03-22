N = input()
K = int(input())

list_of_digits = list(N)
dig_len = len(list_of_digits) - K

possible_num = []
for i in range(len(list_of_digits) - dig_len + 1):
    possible_num.append(int("".join(list_of_digits[i:dig_len+i])))

possible_num.sort()
print(possible_num[-1])
