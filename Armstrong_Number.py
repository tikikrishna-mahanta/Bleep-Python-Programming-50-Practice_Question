number = int(input("Enter a number: "))

original_number = number
digits = len(str(number))
total = 0

while number > 0:
    digit = number % 10
    total += digit ** digits
    number //= 10

if total == original_number:
    print("Armstrong Number")
else:
    print("Not an Armstrong Number")
