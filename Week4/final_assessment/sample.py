import time
new_time = input("Time: ")
hours, minutes = new_time.split(':')
total_minutes = int(hours)*60 + int(minutes)

print(total_minutes)
