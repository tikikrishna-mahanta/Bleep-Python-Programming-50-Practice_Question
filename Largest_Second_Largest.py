a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

if a >= b and a >= c:
    largest = a
elif b >= a and b >= c:
    largest = b
else:
    largest = c

if a == largest:
    if b >= c:
        second_largest = b
    else:
        second_largest = c
elif b == largest:
    if a >= c:
        second_largest = a
    else:
        second_largest = c
else:
    if a >= b:
        second_largest = a
    else:
        second_largest = b

print("Largest:", largest)
print("Second Largest:", second_largest)