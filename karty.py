import numpy as np

length = 99
final_median = 50
final_mean = 45
final_range = 100
start_value = 3

#O(∞)
while True :
    num_array = np.random.randint(start_value, start_value + final_range, 99)
    print (num_array)
    if (num_array.mean == final_mean and num_array.min == start_value and num_array.max == start_value+final_range and np.median(num_array) == final_median):
        break