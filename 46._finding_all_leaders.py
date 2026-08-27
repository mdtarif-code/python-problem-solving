# An element is a leader if it is greater than every element to its right.

def is_leader(numbers):
    leaders=[]
    largest=numbers[len(numbers)-1]
    for i in range(len(numbers)):
        if numbers[(len(numbers)-1)-i]>=largest:
            leaders.append(numbers[(len(numbers)-1)-i])
            largest = numbers[(len(numbers)-1)-i]

    leaders.reverse()
    return leaders

numbers = [16, 17, 4, 3, 5, 2]
result = is_leader(numbers)
print(result)