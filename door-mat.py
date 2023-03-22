def doormat_design():
    N, M = map(int, input("Enter N and M: ").split())
    # Print the top half of the mat
    for i in range(N // 2):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))
    # Print the middle line with "WELCOME"
    print("WELCOME".center(M, "-"))
    # Print the bottom half of the mat
    for i in range(N // 2 - 1, -1, -1):
        pattern = ".|." * (2 * i + 1)
        print(pattern.center(M, "-"))

# doormat_design()