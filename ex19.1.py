def bluth (name_of_actor, age_of_actor, relation):
    print "The actor's name is %s !" % name_of_actor
    print "The age of %s is %d !" % (name_of_actor, age_of_actor)
    print "The %s's relation is %s !" % (name_of_actor, relation)
    print "Thank you for all your help, It was indeed helpful!"


print "Ver 1"
bluth ("Micheal", 45, "Sane Son")

print "Ver 2"
actor = "Buster"
age = 31
relationship = "Youngest Son"

bluth (actor , age + 2, relationship)

