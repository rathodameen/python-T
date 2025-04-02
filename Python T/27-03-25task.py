num=357184367867621
while num!=0:
    digit=num%10
    fact=0
    for i in range(1,digit+1,1):
        if digit%i==0:
            fact+=1
    if fact==2:
        print(digit)
    num=num//10


#finding the length of digitsin the number
n=236367
length=0
while n!=0:
    n=n//10
    length+=1
print(length)
