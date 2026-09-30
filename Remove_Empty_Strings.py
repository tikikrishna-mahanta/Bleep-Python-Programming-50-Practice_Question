items = input("Enter strings separated by commas: ").split(",")

result = [item for item in items if item.strip()]

print("Result:", result)
