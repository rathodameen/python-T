num=234
privious_num=True
while privious_num:
    num=num-1
    fact=0
    for i in range(2,num):
        if num%i==0:
            fact+=1
            break
        if fact==0:
            print(f"the privious prime num is :{num}")
            privious_num=False
