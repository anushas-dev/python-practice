from tabulate import tabulate
from prettytable import PrettyTable

# 1st Example 
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

# 2nd Example 
# Specify the Column Names while initializing the Table
student_table = PrettyTable(["Student Name", "Hobby", "Club", "Happiness Quotient"])
 
# Add rows
student_table.add_row(["Leo", "Stamp Collection", "Dance", "91.2 %"])
student_table.add_row(["Ali", "Desgining", "Art", "93.5 %"])
student_table.add_row(["Seol", "Juggling", "Music", "92.23 %"])
student_table.add_row(["Benny", "Ballet", "Book", "92.7 %"])
student_table.add_row(["Sharpie", "Shoe Making", "Music", "98.2 %"])
student_table.add_row(["Ron", "Dancing", "Dance", "94.1 %"])
student_table.add_row(["Amy", "Acting", "Theatre", "95.0 %"])
 
print(student_table)