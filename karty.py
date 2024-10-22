size = 5
range = 6
median = 7
middleVal=8
start = 5

values = [None] * 5
values[len(values)/2] = median
values[0] = start
values[len(values)-1] = start + middleVal
total = middleVal*size

for val in values:
    if(val == None):
        