print "You enter a dark room with two doors. Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
	print "There's a giant bear here eating a cheese cake. What do you do?"
	print "1. Take the Cake."
	print "2. Scream at the bear."
	
	bear = raw_input("> ")
	
	if bear == "1":
		print "The bear eats your face off. Good Job!"
	elif bear == "2":
		print "The bear eats your legs off. Good Job!"
		print "1. Crawl and look for a gun."
		print "2. Die Alone."
			
		bear_choice = raw_input("> ")
		
		if bear_choice == "1":
			print "Shoot the Bear with the Gun and take his legs."
		elif bear_choice == "2":
			print "Find a Twilight book and die alone."
		else: 
			print "Pray to Jesus."
	else:
		print "Well, doing %s is probably better. Bear runs away." % bear
		
elif door == "2":
	print "You state into the endless abyss at Cthulu's retina."
	print "1. Blueberries"
	print "2. Yellow jacket clothespins."
	print "3. Understanding revolvers yelling melodies."
	
	insanity = raw_input("> ")
	
	if insanity == "1" or insanity == "2":
		print "Your body survives powered by a mind of jello. Good job!"
	else:
		print "The insanity rots your eyes into a pool of muck. Good job!"
		
else:
	print "You stumble around and fall on a knife and die. Good Job."