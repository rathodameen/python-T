#task: Write a program to print the count of   number of Fibonacci numbers in between 0 to 500 ?
num1=0
num2=1
count=0
while num1<=500:
    print(num1,end=" ")
    num3=num1+num2
    num1=num2
    num2=num3
    count+=1
print()
print("count of fibonacci numbers are",count)
