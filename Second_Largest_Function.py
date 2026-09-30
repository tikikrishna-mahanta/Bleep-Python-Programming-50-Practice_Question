def second_largest(numbers):
    unique_numbers = list(set(numbers))

    if len(unique_numbers) < 2:
        return None

    unique_numbers.remove(max(unique_numbers))

    return max(unique_numbers)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

result = second_largest(numbers)

if result is None:
    print("Second largest cannot be found.")
else:
    print("Second Largest:", result)
