numb = [1, 2, 3, 4, 5, 6, 777]

for i in range(len(numb)):
    if numb[i] % 2 ==0:
        numb[i] = "odd"
print(numb)