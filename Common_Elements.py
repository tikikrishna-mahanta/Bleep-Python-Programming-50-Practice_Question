list1 = input("Enter first list values separated by spaces: ").split()
list2 = input("Enter second list values separated by spaces: ").split()

common = []

for item in list1:
    if item in list2 and item not in common:
        common.append(item)

print("Common elements:", common)
