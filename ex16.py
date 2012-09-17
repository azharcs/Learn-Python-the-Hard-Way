from sys import argv

script, filename = argv

print "We are going to erasse %r." % filename
print "If you don't want that, hit CTRL-C"
print "If you want that, hit Return"

raw_input(">")

print "Opening the file %r " % filename
target = open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to a file"

target.write("%r\n%r\n%r\n" % (line1, line2, line3))


print "And finally, we close it."
target.close()

