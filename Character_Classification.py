text = input("Enter a string: ")

vowels = 0
consonants = 0
digits = 0
special_characters = 0

for character in text:
    if character.lower() in "aeiou":
        vowels += 1
    elif character.isalpha():
        consonants += 1
    elif character.isdigit():
        digits += 1
    else:
        special_characters += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special characters:", special_characters)
