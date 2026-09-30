numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

largest = max(numbers)
smallest = min(numbers)
average = sum(numbers) / len(numbers)

print("Largest:", largest)
print("Smallest:", smallest)
print("Average:", average)
