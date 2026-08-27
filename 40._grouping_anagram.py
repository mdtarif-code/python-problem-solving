def anagram_group(lst):

    group = {}
    for i in lst:
        key = "".join(sorted(i))
        if key not in group:
            group[key] = [i]
        else:
            group[key].append(i)

    return list(group.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = anagram_group(words)
print(result)