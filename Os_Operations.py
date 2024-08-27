import os

f = os.open('C:\Users\Lenovo\Downloads\Demo Python.txt','r')
contents = os.read(f,1024)
os.close(f)

# files = os.listdir(".")
# print(files)


# import os
# # Create a new directory
# os.mkdir("newdir")


# import os

# # Run the "ls" command and get the output as a file-like object
# f = os.popen("ls")

# # Read the contents of the output
# output = f.read()
# print(output)  # Output: ['myfile.txt', 'otherfile.txt']

# # Close the file-like object
# f.close()