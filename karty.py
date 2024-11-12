import numpy as np

length = 99
final_median = 50
final_mean = 45
final_range = 100
start_value = 3

#O(1-∞)
while True :
    num_array = np.random.randint(start_value, start_value + final_range, 99)
    num_array[0] = start_value
    num_array[length-1] = start_value + final_range
    print (num_array)
    if (num_array.mean == final_mean and num_array.min == start_value and num_array.max == start_value+final_range and np.median(num_array) == final_median):
        break