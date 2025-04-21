# program to separate odd & even elements from list 
num=[2,4,5,6,7,99,102,111,8,9,10]
even=[]   
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even numbers are",even)
print("odd numbers are",odd)


##program to separate unique elements from list and add "*" at EOL
num=[2,4,5,6,7,99,102,111,9,5,6,4,8,9,10]
unique=[]
for i in num:
    if i not in unique:
        unique.append(i)
print("unique elements are",unique)
