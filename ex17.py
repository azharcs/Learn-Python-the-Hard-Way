from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "We are copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?

indata = open(from_file).read()

print "The %r is %d bytes long" % (from_file, len (indata))

print "Does the output file exist? %r" % exists (to_file)

output = open (to_file, 'w').write(indata)

#output = open(to_file, 'w')
#output.write(indata)

print "Alright, all done."
