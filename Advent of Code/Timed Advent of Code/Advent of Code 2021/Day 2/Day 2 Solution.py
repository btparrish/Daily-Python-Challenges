#total time spent coding was 11:39:84

opened_txt = open(r"file path")
read_txt = opened_txt.read()
raw_entries = read_txt.split("\n")

#split raw entries up into tuples where the first entry is the direction and the second entry is the magnitiude
processed_tuples = []
for entry in raw_entries:
    raw_tuple = entry.split(" ")
    raw_tuple[1] = int(raw_tuple[1])
    processed_tuples.append(raw_tuple)

#initialize a list that serves as our current cartesian coordinates
current_pos = [0,0]

#loop through the list of processed movements and modify the current_pos variable based on values
for movement in processed_tuples:
    if movement[0] == "forward":
        current_pos[0]+=movement[1]
    elif movement[0] == "down":
        current_pos[1]+=movement[1]
    elif movement[0] == "up":
        current_pos[1]-=movement[1]

print(current_pos[0]*current_pos[1])

#recreate the above processing program but considering the variable "aim" as well, where aim is the z coordinate

current_pos_with_aim = [0,0,0]
#loop through the list of processed movements and modify the current_pos variable based on values
for movement in processed_tuples:
    if movement[0] == "forward":
        current_pos_with_aim[0]+=movement[1]
        current_pos_with_aim[1]+= (movement[1]*current_pos_with_aim[2])
    elif movement[0] == "down":
        current_pos_with_aim[2]+=movement[1]
    elif movement[0] == "up":
        current_pos_with_aim[2]-=movement[1]

print(current_pos_with_aim[0]*current_pos_with_aim[1])
