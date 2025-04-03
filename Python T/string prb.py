#taking an para and if it's > 100 not valid
paragraph = "This is an example paragraph with some words. You can replace it with any text you want."

word_count = 0
for word in paragraph.split():  
    word_count += 1

if word_count > 100:
    print("Valid")
else:
    print("Invalid")


#Count of upper and lower numbers in the para\
string = "Hello World! AI is Amazing"  

upper_count = 0
lower_count = 0

for char in string:
    if 'A' <= char <= 'Z':  # Checking uppercase
        upper_count += 1
    elif 'a' <= char <= 'z':  # Checking lowercase
        lower_count += 1

print("Uppercase Letters:", upper_count)
print("Lowercase Letters:", lower_count)

