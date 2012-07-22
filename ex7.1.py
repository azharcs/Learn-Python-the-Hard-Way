# defining the types of people in integer
x = "There are %d types of people." %10
# assigning variable
binary = "binary"
# assigning variable
do_not = "don't"
# assigning the values of the variable to another.
y = "Those who know %s and those who %s." %(binary, do_not)

# out the values of the above variables
print x
print y


print "I said: %r." %x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious 

w = "This is the left side of ..."
e = "a string with a right side."

# concatenate the two variable strings.
print w + e
