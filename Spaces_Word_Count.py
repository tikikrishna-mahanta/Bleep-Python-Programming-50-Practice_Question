text = input("Enter a sentence: ")

without_spaces = text.replace(" ", "")
words = text.split()

print("Without spaces:", without_spaces)
print("Number of words:", len(words))
