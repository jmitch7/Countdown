from time import sleep


minutes = 0
hours = 0

sec = input(('What number? '))
sec = int(sec)
print(str(sec) + ' sec')
sleep(1)

while sec >= 2 and minutes < 59:
	sec = sec - 1
	print(str(sec) + ' sec')
	sleep(1)
	if sec == 59:
		minutes = minutes +1
		print(str(minutes) + ' min')
		sleep(1)
		sec = 0
		if minutes == 59:
			minutes = 0
			hours = hours + 1
			print(hours)
			sleep(1)

if sec == 1:
	print('BLASTOFF!!!')