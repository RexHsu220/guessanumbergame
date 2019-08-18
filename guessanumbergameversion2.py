print('Guess a number game 2nd Version')
import random
r = random.randint(1, 100)
count = 0
while True:
	count += 1
	num = input('Please enter a number: ')
	num = int(num)
	if num == r:
		print('Congratulation !!! You\'ve guessed the correct number !!!!')
		break
	elif num > r:
		print('Number %s is to high !' % (num))
	elif num < r:
		print('Number %s is to low !' % (num))
	print('You\'ve already guessed', count, 'times')