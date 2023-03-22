import string
def print_rangoli(size):
    import string
    alpha = string.ascii_lowercase
    n = size
    lines = []    
    for i in range(n):
        s = "-".join(alpha[i:n])
        lines.append((s[::-1]+s[1:]).center(4*n-3, "-"))
    print('\n'.join(lines[:0:-1]+lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)