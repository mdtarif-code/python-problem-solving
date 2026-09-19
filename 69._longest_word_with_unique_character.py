def longest_word_with_unique_character(text):

    words = text.split()
    longest_word = ""
    for word in words:
        seen = set()
        for c in word:
            if c in seen:
                break

            seen.add(c)

        if len(seen)==len(word):
            if len(word)>len(longest_word):
                longest_word = word

    return longest_word


text = "hello world python dat"
result = longest_word_with_unique_character(text)
print(result)