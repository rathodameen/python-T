import math
a, b, c = 4, 5, 6
def lcm_of_three(a, b, c):
    lcm_ab = math.lcm(a, b)
    return math.lcm(lcm_ab, c)
print("LCM of", a, b, c, "is:", lcm_of_three(a, b, c))
