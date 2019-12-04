"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
open(filename, mode)
1st argument is a string containing the filename
2nd argument (optional) is another string containing a few characters describing the way in which the file will be used.
mode:
    'r' = read only --> will be assumed if mode is omitted
    'w' = write only
    'a' = opens to append data to the end of the file
    'r+' = opens file for both reading and writing
Files are opened in text mode --> read and write strings from and to the file, which are encoded ina specific encoding. If encoding is not specified, it is platform dependent
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE
with open('foo.txt', 'r' ) as f:
    ## Reading 1:
    # read_data = f.read() #will print out the entire file
    # print(read_data)

    ## Reading 2 - 3:
    # read_data = f.readline() #will print out the very first line of file
    # print(read_data, end="")

    # read_data = f.readline() #will print out the second line if the one above is un-commented of file
    # print(read_data, end="")

    ##Reading 4 --> iterating over each line --> not reading all the lines at once which will not cause a memory issue.
    for line in f:
        print(line, end="")

print(f.closed)


# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make 
# sure that it contains what you expect it to contain

# YOUR CODE HERE
with open('bar.txt', 'r') as f:
    for line in f: 
        print(line, end="")

print (f.closed)