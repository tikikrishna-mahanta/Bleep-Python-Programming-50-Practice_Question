def longest_word(sentence):
    words = sentence.split()

    if not words:
        return ""

    longest = words[0]

    for word in words:
        if len(word) > len(longest):
            longest = word

    return longest


sentence = input("Enter a sentence: ")

print("Longest word:", longest_word(sentence))
