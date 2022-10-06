# Write a Python program to triple all numbers of a given list of integers. Use Python map.
# sample list: [1, 2, 3, 4, 5, 6, 7]
# Triple of list numbers:
# [3, 6, 9, 12, 15, 18, 21]

# Using python map
sample_list = [1,2,3,4,5,6,7]
def multiplication(sample_list):
    return sample_list * 3

final_list = list(map(multiplication,sample_list))
print('final list = ', final_list)


# Using lambda with map 
sample_list = [1,2,3,4,5,6,7]
data = list(map(lambda sample_list : sample_list * 3, sample_list))
print('final list = ',data)