def star_pattern_a(n):
    for i in range(1, n+1):
        print(" "*(n-i) + "*"*(2*i-1))


n = int(input("Enter the number of rows: "))
star_pattern_a(n)
