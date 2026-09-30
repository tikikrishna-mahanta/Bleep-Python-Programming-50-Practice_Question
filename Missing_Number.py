n = int(input("Enter the value of N: "))

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

for number in range(1, n + 1):
    if number not in numbers:
        print("Missing number:", number)
        break
