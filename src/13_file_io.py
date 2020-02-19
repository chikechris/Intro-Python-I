"""
Python makes performing file I/O simple. Take a look
at how to read and write to files here: 
https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# Open up the "foo.txt" file (which already exists) for reading
# Print all the contents of the file, then close the file

# YOUR CODE HERE

with open('src/foo.txt') as f:

    for line in f:
        print(line)

# print(read_data.split('\n'))

# Open up a file called "bar.txt" (which doesn't exist yet) for
# writing. Write three lines of arbitrary content to that file,
# then close the file. Open up "bar.txt" and inspect it to make
# sure that it contains what you expect it to contain

# YOUR CODE HERE

three_lines = ['Hello again computer science\n',
               'will need to get a new job\n', 'will need to get a job\n']
new_f = open('src/bar.txt', 'w')
for i in range(len(three_lines)):
    print(i)
    new_f.write(f'new line {three_lines[i]}')