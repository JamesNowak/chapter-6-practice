# TODO 6.4 Exceptions
# In this exercise you will try to open a file that does not exist, capture the error, and display a custom error message

# create a try statement:
try:
    # open the file superheros.txt for READING (we are not writing, it would create the file)
    abc = open("superheros.txt", 'r')
# close the file
    abc.close()
# create an except IOError, and a print statement telling the user that the file doesn't exist
except IOError:
    print("This file cannot be opened.")
