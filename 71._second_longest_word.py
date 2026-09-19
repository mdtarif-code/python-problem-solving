def second_longest_word(text):
    words = text.split()
    maxx = -float('inf')
    longest=""
    second_maxx = -float('inf')
    second_longest= ""
    for word in words:
        if len(word)>maxx:
            second_maxx = maxx
            second_longest = longest
            maxx = len(word)
            longest = word
        elif len(word)>second_maxx and len(word)<maxx:
            second_maxx = len(word)
            second_longest = word

    return second_longest

text = "Python is very useful"
result = second_longest_word(text)
print(result)