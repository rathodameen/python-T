#task
#1.printing the factors of the given number
#2.printing the table but it only have to print the even multiples

#task 1 
n = int(input("Enter the n value :"))
fact = 0
for i in range (1,n+1,1):
    if n%i==0 :
        fact = fact+1
if fact == 2 :
    print("Prime")
else :
    print("Not prime")
   


#task 2
num = int(input("Enter the number :"))
for i in range(1,6):
    print(i)
    for j in range(1,11):
        if j%2==0:
            print(i,"X",j,"=",j*i)
