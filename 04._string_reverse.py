def reversed_string(s):
    new_str = ""
    for i in range(len(s)-1, -1, -1):
        new_str += s[i]
    return new_str

str1 = "python"
result = reversed_string(str1)
print(result)
