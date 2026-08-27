def longest_word(string):
    str_list = string.split(" ")
    longest = ""
    for i in str_list:
        if len(i)>len(longest):
            longest = i

    return longest

text = "Python is a powerful programming language"
result = longest_word(text)
print(result)