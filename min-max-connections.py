"""
Here's a Python function that takes in the input parameters 
and returns the minimum and maximum number of telephone connections
"""

def Minmax(A, B):
    # Minimum number of connections is achieved when each locality has 2 houses
    # Maximum number of connections is achieved when one locality has all but one house
    min_connections = (A // B) * (A // B - 1) // 2 * (B - A % B) + (A // B + 1) * (A // B) // 2 * (A % B)
    max_connections = (A - B + 1) * (A - B) // 2
    return min_connections, max_connections