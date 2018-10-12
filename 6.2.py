# TODO 6.2 Using loops to process files
# Complete the program below to Read in and Count all of the entries in the states file

# open the file in read mode

states_file = open('states.txt', 'r')
counter = int(0)

# write a for loop to read in all of the lines, and print them on the screen, add 1 to counter for each line
line = states_file.readline()

while line != "":
    counter = counter + 1
    print(counter)
    line = states_file.readline()
    print(line)
# close the file
states_file.close()
