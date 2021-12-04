"""
--- Day 2: Dive! ---
Now, you need to figure out how to pilot this thing.

It seems like the submarine can take a series of commands like forward 1, down 2, or up 3:

forward X increases the horizontal position by X units.
down X increases the depth by X units.
up X decreases the depth by X units.
Note that since you're on a submarine, down and up affect your depth, and so they have the opposite result of what you might expect.

The submarine seems to already have a planned course (your puzzle input). You should probably figure out where it's going. For example:

forward 5
down 5
forward 8
up 3
down 8
forward 2
Your horizontal position and depth both start at 0. The steps above would then modify them as follows:

forward 5 adds 5 to your horizontal position, a total of 5.
down 5 adds 5 to your depth, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13.
up 3 decreases your depth by 3, resulting in a value of 2.
down 8 adds 8 to your depth, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15.
After following these instructions, you would have a horizontal position of 15 and a depth of 10. (Multiplying these together produces 150.)

Calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?
"""
#import raw_movements as string from another python file in directory
import movements
raw_movements = movements.raw_movements

#convert raw movements string into list of raw "movements"
raw_movements = raw_movement_string.split("\n")

#initialize a two entry python list that serves as a coordinate system denoting the x position first (forward and back), and the y position second (up and down)
current_position = [0,0]

#loop through the list of separated string movement entries and split into direction and magnitude denotation. then, use differentiated direction and magnitude to modify
#the "current_position" variable piecewise for each entry in the "raw_movements" list
for movement in raw_movements:
  movement_tuple = movement.split(" ")
  if movement_tuple[0] == "forward":
    current_position[0]+=int(movement_tuple[1])
  elif movement_tuple[0] == "up":
    current_position[1]-=int(movement_tuple[1])
  elif movement_tuple[0] == "down":
    current_position[1]+=int(movement_tuple[1])
print(current_position)

#the solution to the problem demands the product of the position dimentions, which will be computed and printed below
solution = current_position[0]*current_position[1]
print(solution)

"""
--- Part Two ---
Based on your calculations, the planned course doesn't seem to make any sense. You find the submarine manual and discover that the process is actually slightly more complicated.

In addition to horizontal position and depth, you'll also need to track a third value, aim, which also starts at 0. The commands also mean something entirely different than you first thought:

down X increases your aim by X units.
up X decreases your aim by X units.
forward X does two things:
It increases your horizontal position by X units.
It increases your depth by your aim multiplied by X.
Again note that since you're on a submarine, down and up do the opposite of what you might expect: "down" means aiming in the positive direction.

Now, the above example does something different:

forward 5 adds 5 to your horizontal position, a total of 5. Because your aim is 0, your depth does not change.
down 5 adds 5 to your aim, resulting in a value of 5.
forward 8 adds 8 to your horizontal position, a total of 13. Because your aim is 5, your depth increases by 8*5=40.
up 3 decreases your aim by 3, resulting in a value of 2.
down 8 adds 8 to your aim, resulting in a value of 10.
forward 2 adds 2 to your horizontal position, a total of 15. Because your aim is 10, your depth increases by 2*10=20 to a total of 60.
After following these new instructions, you would have a horizontal position of 15 and a depth of 60. (Multiplying these produces 900.)

Using this new interpretation of the commands, calculate the horizontal position and depth you would have after following the planned course. What do you get if you multiply your final horizontal position by your final depth?

"""

#initialize a three entry python list that denotes dimensional values of the submarines current position. as above, index = 0 corresponds to the submarine's x position
#index =1 corresponds to the submarine's y position, and index = 2 corresponds to the submarine's "aim" as described in the prompt
current_position = [0,0,0]
#recreate the loop operation as above but accounting for "aim" with the third dimension denoted in the "current position" variable
for movement in raw_movements:
  movement_tuple = movement.split(" ")
  if movement_tuple[0] == "forward":
    current_position[0]+=int(movement_tuple[1])
    current_position[1]+=(int(movement_tuple[1])*current_position[2])
  elif movement_tuple[0] == "up":
    current_position[2]-=int(movement_tuple[1])
  elif movement_tuple[0] == "down":
    current_position[2]+=int(movement_tuple[1])
print(current_position)

#the solution to the problem demands the product of the position dimentions, which will be computed and printed below
solution = current_position[0]*current_position[1]
print(solution)
