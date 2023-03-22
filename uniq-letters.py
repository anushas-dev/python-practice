user_input = input()                  # Reading input from STDIN
letters = list(user_input)
uniq_l = []
for i in letters:
    if i not in uniq_l:
        uniq_l.append(i)
print("".join(uniq_l))