def count_of_vowels(st):
    lst = ["a","e","i","o","u"]
    count = 0
    new_string = st.lower()

    for i in new_string:
        if i in lst:
            count +=1
            
    return count


str1 = "Programming"
result = count_of_vowels(str1)
print(result)