def is_rotation(str1, str2):
    if len(str1)!=len(str2):
        return False
    
    new_str1 = str1*2
    if str2 in new_str1:
        return True

    return False

string1 = "abcd"
string2 = "abc"
result = is_rotation(string1,string2)
print(result)