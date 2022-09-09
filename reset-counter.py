from prettytable import PrettyTable
 
fruit_table = PrettyTable(["Product(A)", "No.(B)"])

products = ["Apple", "Apple","Apple", "Orange","Orange","Orange","Orange","Orange","Melon","Melon", "Peach","Peach","Peach"]

counter = 0
for i in range(0, len(products)-1):

    if products[i] == products[i+1]:
        counter+= 1
        fruit_table.add_row([products[i],counter])
    else:
        fruit_table.add_row([products[i],counter+1])
        counter=0

print(fruit_table)