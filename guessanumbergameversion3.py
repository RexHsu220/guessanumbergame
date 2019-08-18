print('Guess a number game')
import random
start = input('Please enter the start of the range of the numbers: ')
start = int(start)
end = input('Please enter the end of the range of the numbers: ')
end = int(end)
r = random.randint(start, end)
i = input('How many chances do you want to guess ?:　') #chances left
i = int(i)
while i > 0:
	i = i - 1
	num = input('Please enter a number between {0} to {1}: '.format(start, end))
	num = int(num)
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


