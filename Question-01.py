# Write a Python program to create a lambda function that adds 25 to a given number passed in as an argument.
# sample input: 10
# sample output: 35

# Approach-01
num = int(input('please provide the number to be added = '))
data = (lambda num : num+25)
print('output = ',data(num))



# Approach-02
num = int(input('please provide the number to be added = '))
num1 = int(input('please provide the number to be added = '))
data = (lambda num,num1 : num+num1)
print('output = ',data(num,num1))
