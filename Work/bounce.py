# bounce.py
#
# Exercise 1.5

ball_height = 100
max_bounce = 10
bounce = 1

while bounce <= max_bounce:
	print (ball_height)
	ball_height = ball_height * (3/5)
	bounce = bounce+1;