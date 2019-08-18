print('Guess a number game, you will have 10 chances')
import random
r = random.randint(1, 100)
i = 10 #chances left
while i > 0:
	i = i - 1
	g = input('Please enter a number between 1 and 100:')
	g = int(g)
	if g == r:
		print('Congratulation !!!, You\'ve guessed the correct number !')
		break
	else:
		if i > 0:
			print('%s is not the correct number !' % (g))
			if g > r:
				print('The number you guessed was to high ! You still have', i, 'chances.')
			elif g < r:
				print('The number you guessed was to low ! You still have', i, 'chances.')
		else: 
			print('No chances left !')


