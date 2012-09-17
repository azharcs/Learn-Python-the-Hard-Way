#importing the module
from sys import argv

#providing arguments 
script, filename = argv

#open the filename and assign it to a variable
txt = open(filename)

# reading the file using read function and print it.
print "Here's your file %r:" % filename
print txt.read()

#typing the filename again or a new filename
print "I'll also ask you to type it again:" 
file_again = raw_input("> ")

#assiging the contents of the file to another variable
txt_again = open (file_again)

print txt_again.read()
