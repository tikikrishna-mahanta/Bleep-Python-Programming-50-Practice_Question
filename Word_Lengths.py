sentence = input("Enter a sentence: ")

words = sentence.split()
lengths = [len(word) for word in words]

print("Word lengths:", lengths)
