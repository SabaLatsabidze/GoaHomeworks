age = int(input("How old are you?:"))

n = 5  # Number of rows

for i in range(n):
    print(' ' * (n - i - 1) + '*' * (2 * i + 1))

