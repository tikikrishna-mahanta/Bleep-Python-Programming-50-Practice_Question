numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

even_numbers = []
odd_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)
