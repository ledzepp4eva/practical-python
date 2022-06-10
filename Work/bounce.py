# bounce.py
#
# Exercise 1.5

start_height = 100
stop_height = 0

for h in range(1, 11):
    start_height = round(start_height * 0.6, 4)
    print(h, start_height)

