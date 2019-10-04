print('猜數字遊戲')
import random

def game():
	start = eval(input('請輸入範圍最小值: '))
	end = eval(input('請輸入範圍最大值: '))
	r = random.randint(start, end)
	i = eval(input('你想要猜幾次 ?: ')) #chances left
	lnum = 0
	while i > 0:
		i = i - 1
		num = eval(input('請輸入一個{0}到{1}之間的數字: '.format(start, end)))	
		if num == r:
			print('恭喜你，你猜對了 !')
			break
		else:
			if i > 0:
				print('%s 不是正確的數字 !' % (num))
				if num > r:
					if num >= end:
						i = 0
						print('你是不是智障阿都提示過你了 %s 太高你還猜 %s 我她媽不給你玩了' % (lnum, num)) 
					else:
						end = num
						lnum = num
						print('你猜的數字太高了 ! 你還有', i, '次機會.')
				elif num < r:
					if num <= start:
						i = 0
						print('你是不是智障阿都提示過你了 %s 太低你還猜 %s 我她媽不給你玩了' % (lnum, num))
					else:
						start = num
						lnum = num
						print('你猜的數字太低了 ! 你還有', i, '次機會.')
			else: 
				print('你沒有機會了小智障 !')
game()

while True:
	reg = eval(input('小智障還要繼續玩嗎 ? 要的話請輸入 1，不要的話就按 2 然後滾: '))
	if reg == 1:
		game()
	elif reg == 2:
		break
	else: 
		print('輸入 1 或 2 拉智障')















