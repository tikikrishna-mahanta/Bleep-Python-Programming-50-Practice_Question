numbers = input("Enter elements separated by spaces: ").split()

frequency = {}

for number in numbers:
    if number in frequency:
        frequency[number] += 1
    else:
        frequency[number] = 1

for number, count in frequency.items():
    print(number, ":", count)
