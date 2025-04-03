#prime and non-prime numbers

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numbers = [10, 11, 15, 17, 19, 20, 25, 29]  # Example list
primes = []
non_primes = []

for num in numbers:
    if is_prime(num):
        primes.append(num)
    else:
        non_primes.append(num)

print("Prime Numbers:", primes)
print("Non-Prime Numbers:", non_primes)



#count skills from a dict
skills = ["Python", "Java", "Python", "C++", "Java", "Python", "C"]  # Example skill list
skill_count = {}

for skill in skills:
    skill_count[skill] = skill_count.get(skill, 0) + 1

print("Skill Counts:", skill_count)
