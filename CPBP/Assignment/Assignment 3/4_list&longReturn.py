# Write a function that takes a list of words and returns the length of the longest one.

def longest_word_length(words):
    max_length = 0
    for word in words:
        if len(word) > max_length:
            max_length = len(word)
    return max_length

# Example list of words
words_list = ["apple", "banana", "strawberry", "kiwi"]
print("The length of the longest word is:", longest_word_length(words_list))
