
# #Task
# # 1.odd or even 
#odd or even
num = int(input("enter the number:"))
if num % 2 == 0:
    print("even")
else:
    print("odd")

#2. big number
c = int(input("Enter the value of c :"))
d = int(input("Enter the value of d :"))
if c>d :
    print("c is a bigger number :")
elif d>c :
    print("d os a bigger number :")
else :
    print("they are equal")


#3.positive,negative or zero
a = int(input("enter a :"))
b = int(input("Enter the b :"))
if a>0 and b>0 :
    print("the numbers are positive")
elif a<0 and b<0 :
    print("the numbers are negative")
elif a>0 and b<0 :
    print("a is positive and b is negative")
elif a<0 and b>0 :
    print("b is positive and a is negative")
else : 
    print("the numbers are zero")

#4.voting system
age = int(input("Enter your age :"))
if age > 18 :
    print("your eligible for the voting")
else :
    print("your not eligible for voting")

#5.pass or fail
marks = int(input("Enter your marks :"))
if marks >= 40:
    print("Pass")
else:
    print("Fail")


