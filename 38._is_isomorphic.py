def is_isomorphic(text1, text2):

    if len(text1) != len(text2):
        return False

    dict1 = {}
    dict2 = {}
    for i in range(len(text1)):
        if text1[i] not in dict1:
            dict1[text1[i]] = text2[i]
        else:
            if dict1[text1[i]] != text2[i]:
                return False
        
        if text2[i] not in dict2:
            dict2[text2[i]] = text1[i]
        else:
            if dict2[text2[i]] != text1[i]:
                return False

    return True

    

text1 = "egg"
text2 = "add"
result = is_isomorphic(text1,text2)
print(result)