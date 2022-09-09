matrix = [[j for j in range(3)] for i in range(3)] 
print(matrix)

def get_even_func(numbers):
    even_numbers = [num for num in numbers if not num % 2]
    return even_numbers

print(get_even_func([1, 2, 3, 4, 5, 6]))

x = 20
def my_function():
  x = 30
  print(x, end=' ')

my_function()
print(x, end=' ')
