#დავალება 1
letters = ['a', 'b', 'c', 'e', 'f', 'g', 'i', 'o', 'u', 'p', 'r']

vowels = ['a', 'e', 'i', 'o', 'u']

vowel_count = sum(1 for letter in letters if letter in vowels)

print(f"ხმოვნების რაოდენობა: {vowel_count}")


#დავალება 2
numbers = [i for i in range(1, 101) if i % 5 == 0 or i % 3 == 0]

print("5-ის და 3-ის ჯერადები:", numbers)


#დავალება 3
mixed_list = ['a', 'b', 1, 2, 'c', 'd', 3, 'e']

combined_string = ''.join(str(item) for item in mixed_list)

print("ერთ სტრინგში წარმოდგენილი ელემენტები:", combined_string)

#დავალება 4
n = 5

for i in range(n):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))

for i in range(n - 2, -1, -1):
    print(" " * (n - i - 1) + "*" * (2 * i + 1))


#დავალება 5
age = int(input("რამდენი წლის ხარ? "))

if age > 12:
    print("შენ არ ხარ 12 წლის")