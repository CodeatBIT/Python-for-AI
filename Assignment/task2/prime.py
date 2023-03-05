def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


num = int(input("Enter a number: "))
if is_prime(num):
    print(f"{num} is prime.")
else:
    print(f"{num} is not prime.")
