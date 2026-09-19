# Given a string and K (size of window) 
# find maximum vowels in k consecutive characters

def max_vowel(text,k):
    new_text = text.lower()
    vowel = ['a','e','i','o','u']
    vowel_count = 0
    for i in new_text[:3]:
        if i in vowel:
            vowel_count += 1

    maxx_vowel = vowel_count
    for i in range(len(new_text)-k):
        if new_text[i] in vowel:
            vowel_count -= 1

        if new_text[i+k] in vowel:
            vowel_count += 1

        maxx_vowel = max(maxx_vowel,vowel_count)

    return maxx_vowel
    
text = "abciiidef"
k = 3
result = max_vowel(text,k)
print(result)