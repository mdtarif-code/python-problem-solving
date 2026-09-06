def longest_consecutive(numbers):
    seen = set(numbers) # using set for better complexity as set easy to traverse
    longest = 0
    for i in seen:
        if i-1 not in seen:
            current = i
            count = 1
            while current+1 in seen:
                current += 1
                count += 1

            if count>longest:
                longest = count

    return longest


numbers = [100, 4, 200, 1, 3, 2]
result = longest_consecutive(numbers)
print(result)