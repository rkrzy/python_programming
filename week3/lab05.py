import time

fseconds = time.time()
total_sec = int(fseconds)
total_min = total_sec // 60
minute = total_min % 60
total_hour = total_min // 60
hour = total_hour % 24 + 9

print("현재 한국 시간: " + str(hour) + "시 "+str(minute) + "분")