numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

unique_numbers = list(set(numbers))

if len(unique_numbers) < 2:
    print("Second largest and second smallest cannot be found.")
else:
    largest = max(unique_numbers)
    smallest = min(unique_numbers)

    unique_numbers.remove(largest)
    unique_numbers.remove(smallest)

    second_largest = max(unique_numbers)
    second_smallest = min(unique_numbers)

    print("Second Largest:", second_largest)
    print("Second Smallest:", second_smallest)
