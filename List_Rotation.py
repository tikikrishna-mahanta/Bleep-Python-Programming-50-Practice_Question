numbers = input("Enter numbers separated by spaces: ").split()
numbers = list(map(int, numbers))

k = int(input("Enter rotation positions: "))

if numbers:
    k = k % len(numbers)
    rotated = numbers[k:] + numbers[:k]
    print("Rotated list:", rotated)
else:
    print("List is empty.")
