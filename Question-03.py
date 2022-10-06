# Write a Python program to square the elements of a list using map() function.
# Sample List: [4, 5, 2, 9]
# Square the elements of the list:
# [16, 25, 4, 81]

# Using python map
sample_list = [4,5,2,9]
def square(sample_list):
    return sample_list ** 2

final_list = list(map(square,sample_list))
print('final list = ', final_list)


# Using lambda with map 
sample_list = [4,5,2,9]
data = list(map(lambda sample_list : sample_list ** 2, sample_list))
print('final list = ',data)