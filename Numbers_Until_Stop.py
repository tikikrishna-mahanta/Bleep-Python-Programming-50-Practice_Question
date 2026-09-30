numbers = []

while True:
    value = input("Enter a number or type 'stop': ")

    if value.lower() == "stop":
        break

    try:
        number = float(value)
        numbers.append(number)
    except ValueError:
        print("Invalid input. Please enter a number.")

if numbers:
    numbers.sort()

    minimum = min(numbers)
    maximum = max(numbers)
    average = sum(numbers) / len(numbers)

    middle = len(numbers) // 2

    if len(numbers) % 2 == 0:
        median = (numbers[middle - 1] + numbers[middle]) / 2
    else:
        median = numbers[middle]

    print("Minimum:", minimum)
    print("Maximum:", maximum)
    print("Average:", average)
    print("Median:", median)
else:
    print("No numbers were entered.")
