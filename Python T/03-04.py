string = "a c sedjnhe dnft INFR SENRIFWE  wdnr fj cf vrr frg r vnfbbv"
valid = True
i = 0  
while i < len(string):
    if not ('A' <= string[i] <= 'Z' or 'a' <= string[i] <= 'z' or string[i] == ' '):
        valid = False
        break
    i += 1
if valid:
    print("Valid")
else:
    print("Invalid")

###
n = int(input("Enter the value of n: "))
count = 0  
num = 1    
def cb(prime):  
    print("The ",n,"th prime number is: ",prime)
while count < n:
    num += 1
    factors = 0  
    for i in range(1, num + 1):
        if num % i == 0:
            factors += 1  
    if factors == 2:  
        count += 1  
cb(num) 
