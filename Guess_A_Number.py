import random
# test comment
# Comment 2
for x in range(1):
	answer = random.randint(1,21)

message = ''
active = True
while active:
	message = input(' Play a guessing game press enter or no to quit: ')
	if message == 'no':
		active = False

	else:
		for value in range(1,6):
			input_number = input(" pick a number between 1 and 20 : ")
			number = int(input_number)
			if answer > number:
				print("To Low")
			elif answer < number:
				print("To High")
			elif answer == number:
				print("you are correct")
				break
		if answer != number:		
			print('Sorry you only get 5 chances ')

print("Thanks for playing")

		



