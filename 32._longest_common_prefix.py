def longest_common_prefix(words):

    prefix = words[0]

    if prefix == "":
        return ""
    
    for word in words[1:]:

        while len(prefix) > len(word):
            prefix = prefix[:-1]

        while prefix != word[:len(prefix)]:
            prefix = prefix[:-1]

    return prefix


            
words = ["flower", "flow", "flight"]
result = longest_common_prefix(words)
print(result)