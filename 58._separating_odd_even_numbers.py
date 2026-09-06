#Given a list of numbers, rearrange it so that:
#All even numbers come first
#All odd numbers come afterward

def separate_odd_even(numbers):

    if not numbers:
        return None

    odds = []
    evens = []
    for i in numbers:
        if i%2==0:
            evens.append(i)
        else:
            odds.append(i)

    return evens+odds

numbers = [3, 8, 5, 2, 7, 4, 1]
result = separate_odd_even(numbers)
print(result)