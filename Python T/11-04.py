#find the missing number in the list
num=[1,2,3,4,5,6,7,8,9]
missing_num=[i for i in range(1,10) if i not in num]
print("missing numbers are",missing_num)


# 2. Take a dictionary with salaries and Find percentage of the salaries
# Input: {"Ameen": 1000, "Rathod": 2000, "Shivaji": 3000}
# Output: {"Ameen": 33.33, "Rathod": 66.67, "Shivaji": 100.00}  
dic={"Ameen":1000,"Rathod":2000,"Shivaji":3000}
total=0
for i in dic:
    total+=dic[i]
print("total is",total)
for i in dic:
    percentage=(dic[i]/total)*100
    print(i,percentage)
