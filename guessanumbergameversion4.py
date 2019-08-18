print('Guess a number game')
import random
start = eval(input('Please enter the start of the range of the numbers: '))
end = eval(input('Please enter the end of the range of the numbers: '))
r = random.randint(start, end)
i = eval(input('How many chances do you want to guess ?:　')) #chances left
while i > 0:
	i = i - 1
	num = eval(input('Please enter a number between {0} to {1}: '.format(start, end)))	
	if num == r:
		print('Congratulation !!!, You\'ve guessed the correct number !')
		break
	else:
		if i > 0:
			print('%s is not the correct number !' % (num))
			if num > r:
				print('The number you guessed was to high ! You still have', i, 'chances.')
			elif num < r:
				print('The number you guessed was to low ! You still have', i, 'chances.')
		else: 
			print('No chances left !')
