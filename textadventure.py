start = '''
You are a renowned detective in your community. You just found out that there
was a murder at costco, your favorite store. You go to Costco immediately and
check out the crime scene. You don't feel like working today, but you also want
start investigating the murder scene because you are the best detective in town
and you know nobody else besides you can solve it. Do you want to go to your
friend's house and party, or do you want to start the murder investigation?
'''


print(start)


print('''Type 'party' to go to your friend's house or 'investigate' to start 
working on the murder case.''')
user_input = input()

if user_input == "party":
	print('''You decide to go to your friend's party and you find out that she 
	is the murderer! Do you want to help them out? Type 'yes' if you want to 
	help and type 'no' if you don't want to help''')
	user_input = input()
	if user_input == "yes":
		print('''You become accomplices with your friend/murderer and you rob 
		banks together and get rich and nbody finds out! Woohoo!!''')
		user_input = input()
	elif user_input == "no":
		print('''Oh no!! Your friend/murderer secretly hates you and decides to 
		frame you for her crime.''')
 
elif user_input == "investigate":
	print('''You choose to start investigating the murderer and you found the 
	murderer's house! You go inside and find her! You find a gun! Should you 
	shoot her with it? Type 'yes' if you want to shoot them and type 'no' if 
	you don't want to shoot them''')
	user_input = input()
	if user_input == "yes":
		print('''You kill the murderer but everyone thinks he committed suicide, 
		so I guess that's alright.''')
		user_input = input()
	elif user_input == "no":
		print('''The murderer snatches the gun from you because you're dumb, and 
		she kills you.''')
else:
	print("That wasn't an option!!")