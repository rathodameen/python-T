# Task 1: Find the second prime after the given number
def second_prime_after(n):
    count = 0
    num = n + 1
    while True:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                break
        else:  # Executes only if the loop wasn't broken
            count += 1
            if count == 2:
                return num
        num += 1

# Example usage
given_number = 10
print("Second prime after", given_number, "is:", second_prime_after(given_number))


# Task 2: Break the loop if condition matches with the given number
def break_on_number(target):
    num = 1
    while True:
        print(num)
        if num == target:
            print("Breaking loop as number matched:", target)
            break
        num += 1

# Example usage
break_on_number(7)


# Task 3: Print numbers from 1 to 100, but skip multiples of 3
def skip_multiples_of_3():
    num = 1
    while num <= 100:
        if num % 3 == 0:
            num += 1
            continue
        print(num)
        num += 1

# Example usage
skip_multiples_of_3()
