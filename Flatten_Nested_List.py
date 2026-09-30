def flatten_list(items):
    result = []

    for item in items:
        if isinstance(item, list):
            result.extend(flatten_list(item))
        else:
            result.append(item)

    return result


nested_list = [[1, 2], [3, [4, 5]], [6, [7, [8]]]]

print("Nested list:", nested_list)
print("Flattened list:", flatten_list(nested_list))
