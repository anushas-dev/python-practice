sample_string = list(input())
converted_string = []
for i in sample_string:
    converted_string.append(i.swapcase())
print("".join(converted_string))
