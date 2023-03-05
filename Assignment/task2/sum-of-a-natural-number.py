def sum_of_natural_numbers(n):
    sum = 0
    i = 1
    while i <= n:
        sum += i
        i += 1
    return sum


n = int(input("Enter the value of n: "))
total = sum_of_natural_numbers(n)
print(f"The sum of the first {n} natural numbers is {total}")
