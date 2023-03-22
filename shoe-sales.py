from collections import Counter

shoe_count = int(input())
shoe_sizes = list(map(int, input().split()))
cust_count = int(input())
shoe_set = list(Counter(shoe_sizes).keys())
shoe_counter = list(Counter(shoe_sizes).values())
shoe_dict = dict(zip(shoe_set, shoe_counter))

sales = 0
for i in range(cust_count):
    size, price = input().split()
    size, price = int(size), int(price)
    if size in shoe_set and shoe_dict[size] > 0:
        sales = sales + price
        print(sales)
        shoe_dict[size]-=1
    
print(sales)

