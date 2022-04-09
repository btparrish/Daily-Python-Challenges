#total time spent coding was 11:45:69

from asyncio import ProactorEventLoop


txt_file = open(r"filepath")
read_file = txt_file.read()
list_of_strings = read_file.split("\n")
#convert all strings to ints
for i in range(len(list_of_strings)):
    list_of_strings[i] = int(list_of_strings[i])
depths = list_of_strings
#loop through the list of depths and determine whether or not the subsequent measurment is greater than the previous
num_greater = 0
for i in range(1,len(depths)):
    prev = depths[i-1]
    sub = depths[i]
    if sub>prev:
        num_greater+=1
print(num_greater)

#sum sliding windows of 3 depths and compare subsequent sliding window to previous sliding window
num_window_greater = 0
for i in range(0,len(depths)):
    prev_window = depths[i:(i+3)]
    next_window = depths[(i+1):(i+4)]
    if sum(next_window)>sum(prev_window):
        num_window_greater+=1
print(num_window_greater)
