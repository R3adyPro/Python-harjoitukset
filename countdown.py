import time

countdown_time = int(input('Where you want to start the countdown? '))
for i in range(countdown_time):
    print(countdown_time)
    countdown_time = countdown_time - 1
    time.sleep(1.0)

print('Lift off!')