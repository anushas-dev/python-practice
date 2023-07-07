t = int(input())

for i in range(t):
    number_of_cycles = int(input())
    height = 1

    for j in range(1,number_of_cycles+1):
        if j%2==1:
            height = height*2
        else:
            height = height + 1
    print(height)
