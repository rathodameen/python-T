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
