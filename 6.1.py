# TODO 6.1 Introduction to File Input and Output
# Assign the variable file_variable to open states.txt in read mode

file_variable = open('states.txt', 'r')
file_variable.close()
state_capitals = open('capitals.txt', 'w')
state_capitals.write("Alabama, Montgomery\n")
state_capitals.write("Illinois, Springfield\n")
state_capitals.write("Arizona, Pheonix\n")
state_capitals.close()
