# Task1 Take 9 digit number,take one digit check whether that digit is present or not , print the count of that digit and positions
num=938524820
temp=num
digit=int(input("Enter the digit to be checked"))
count=0
pos=0
while num>0:
    d=num%10
    if d==digit:
        count+=1
        print(f"position {pos}")
    num=num//10
    pos+=1
if count==0:
    print("not present")
else:
    print(f"count of {digit} is {count}")


# Task2: Take a number check whether that no is in descending order or not
num=765439
prev=0
is_asc=True
while num!=0:
    digit=num%10
    if prev>digit:
        is_asc=False
        break 
    prev=digit
    num=num//10
if is_asc:
    print('accending orde')
else:
    print("not accending")
