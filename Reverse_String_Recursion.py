def reverse_string(text):
    if len(text) <= 1:
        return text

    return reverse_string(text[1:]) + text[0]


text = input("Enter a string: ")

print("Reversed string:", reverse_string(text))
