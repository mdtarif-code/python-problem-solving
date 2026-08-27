def longest_substring(str):

    longest = 0
    for i in range(len(str)):
        current = []
        for j in range(i,len(str)):

            if str[j] not in current:
                current.append(str[j])
                if longest<len(current):
                    longest = len(current)
            else:
                break
                

    return longest

text = "pwwkew"
result = longest_substring(text)
print(result)