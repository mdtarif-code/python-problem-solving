def longest_consecutive(number):
    longest = 0
    for i in number:
        if i-1 not in number:
            current = i
            count = 1
            while current+1 in number:
                current += 1
                count += 1

            if count>longest:
                longest = count

    return longest


numbers = [100, 4, 200, 1, 3, 2]
result = longest_consecutive(numbers)
print(result)