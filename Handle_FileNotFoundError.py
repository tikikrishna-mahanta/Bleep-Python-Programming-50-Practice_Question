filename = input("Enter file name: ")

try:
    with open(filename, "r") as file:
        content = file.read()

    print(content)

except FileNotFoundError:
    print("File not found.")
