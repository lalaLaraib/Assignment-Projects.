import time
def countdown_timer(seconds):
  while seconds > 0:
    mins, sec = divmod(seconds, 60) # minutes and seconds are calculated
    time_format = '{:02d}:{:02d}'.format(mins,sec)
    print(time_format, end='\r')
    time.sleep(1)
    seconds -= 1
  print("00:00 \n Time's Up!")

# user input for timer:
total_seconds = int(input("Enter time in second for countdown:"))
countdown_timer(total_seconds)
