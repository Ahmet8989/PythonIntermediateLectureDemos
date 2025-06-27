import datetime

# result = dir(datetime)
# print(result)

now = datetime.datetime.now()
result2 = now.year
result3 = now.month
result4 = now.day
result5 = now.hour
result6 = datetime.datetime.ctime(now)

print(result2)
print("==========")
print(result3)
print("==========")
print(result4)
print("==========")
print(result5)
print("==========")
print(result6)
print("==========")

result7 = datetime.datetime.strftime(now, "%A %B %Y")
result8 = datetime.datetime.strftime(now, "%d %X")
print(result7)
print("==========")
print(result8)
print("==========")

t = "23 May 2023 hour 10:12:13"
dt = datetime.datetime.strptime(t, "%d %B %Y hour %H:%M:%S")
print(dt)

day = datetime.datetime(1983, 5, 9, 12, 30, 10)
print(day)
print("==========")
result9 = datetime.datetime.timestamp(day) # to seconds
result10 = datetime.datetime.fromtimestamp(result9) # from seconds to datetime
result11 = now - day # timedelta 
print(result9)
print("==========")
print(result10)
print("==========")
print(result11)
print("==========")