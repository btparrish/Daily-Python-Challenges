#total time spent coding was 08:45:31

opened_file = open(r"C:\Users\bentp\Desktop\Python\Advent of Code Challenges\day3.txt")
read_file = opened_file.read()
binary_strings = read_file.split("\n")
print(binary_strings)

#loop through a range iterable object the length of one of the strings in the list, and additionally loop through every binary in the binary_strings list at that particular position in the range function and count the number of ones and zeros at each position
final_binary = ""
for i in range(len(binary_strings[0])):
    num_ones = 0
    num_zeros = 0
    for binary in binary_strings:
        if binary[i] == "0":
            num_zeros+=1
        elif binary[i] == "1":
            num_ones+=1
    if num_ones >= num_zeros:
        final_binary+="1"
    else:
        final_binary+="0"
#print the gamma rate
gamma_rate = int(final_binary,2)

#alter code above to generate epsilon rate
final_binary = ""
for i in range(len(binary_strings[0])):
    num_ones = 0
    num_zeros = 0
    for binary in binary_strings:
        if binary[i] == "0":
            num_zeros+=1
        elif binary[i] == "1":
            num_ones+=1
    if num_ones < num_zeros:
        final_binary+="1"
    else:
        final_binary+="0"
epsilon_rate = int(final_binary,2)

print(gamma_rate*epsilon_rate)
