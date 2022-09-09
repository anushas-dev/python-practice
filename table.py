from tabulate import tabulate

mydata = [
    ["A",2,100,0],
    ["B",3,200,0],
    ["C",0,35,2],
    ["D",4,150,0],
    ["E",2,35,0],
    ["F",5,48,2],
]
 
# create header
head = ["Level 1", "Level 2", "Value 1", "Value 2"]
 
# display table
print(tabulate(mydata, headers=head, tablefmt="grid"))