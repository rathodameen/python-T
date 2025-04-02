# # num=102
# # prime_n_f = True

# # while prime_n_f :
# #     num+=1 #106
# #     fact=0
# #     for i in range (1,num+1,1):
# #         if num%i == 0:
# #             fact+=1
# #     print(num,fact)
# #     if fact==2:
# #         prime_n_f = False
# #         print(num,"is the next prime")

# # Break the loop if  Condition matches with the given number?
# num=int(input("enter the number :"))
# while num>=38:
#     num=num+1
#     if num<38:
#         break


n = int(input("Enter the number :"))
count = 0
num = n + 1

while True:
    fact = 0
    for i in range(1, num + 1):  # Check factors from 1 to num
        if num % i == 0:
            fact += 1
    
    if fact == 2:  # Prime numbers have exactly two factors
        count += 1
        if count == 2:
            print(num)  # Expected output: 17
            break
    
    num += 1

# break statement
target = int(input("number :"))
num = 1
while True:
    print(num)
    if num == target:
        print("Breaking loop as number matched:", target)
        break
    num += 1

# Task 3: Print numbers from 1 to 100 but skip multiples of 3
num = 1
while num <= 100:
    if num % 3 == 0:
        num += 1
        continue
    print(num)
    num += 1

