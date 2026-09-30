def merge_lists(list1, list2):
    result = []

    for item in list1 + list2:
        if item not in result:
            result.append(item)

    return result


list1 = input("Enter first list values separated by spaces: ").split()
list2 = input("Enter second list values separated by spaces: ").split()

print("Merged list:", merge_lists(list1, list2))
