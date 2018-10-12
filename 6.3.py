# TODO 6.3 Processing records

# You are going to finish the program below to write data to a file

# entering book information
books = 3

# open the file books.txt for writing remove the """ """ to test
books_file = open('book.txt', 'w')

# use a for loop to get title and author from the user use the range 1, books + 1
for books in range(1, books + 1):
    # get the data in the loop
    title = input("enter a title of a book: ")
    author = input("Enter the authors name: ")
# write the data as a record in the loop, make sure to include the \n at the end of the line
    books_file.writelines(title + '\n')
    books_file.writelines(author + '\n')
# close the file
books_file.close()
