def is_prime(num):

    if num<=1:
        return False

    for i in range(2,num):
        if num%i==0:
            return False

    return True

num = 30

if is_prime(num):
    print("It's a prime number")
else:
    print("It's not a prime number")