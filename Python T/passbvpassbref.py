#pass by referances
def change_list(lst):
    lst.append(4)  # Modifying list
    print("Inside:", lst)

numbers = [1, 2, 3]
change_list(numbers)
print("Outside:", numbers)  # List is changed

#pass by value
def change_number(x):
    x = 10  # Changing x inside function
    print("Inside:", x)

a = 5
change_number(a)
print("Outside:", a)  # a remains 5


#position and keyword parameters
def show_info(name, age, city="Unknown"):
    print(name, age, city)

show_info("Rathod", 22, city="Mumbai")  # Positional + Keyword
show_info("Alice", 25)  # Uses default city
