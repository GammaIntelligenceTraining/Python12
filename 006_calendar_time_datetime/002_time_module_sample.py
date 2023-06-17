import datetime

# today = datetime.datetime.now()
# print(today.timestamp())
# print(datetime.datetime.fromtimestamp(1686935282.700647))

t = datetime.time(14, 12, 43, 10000)
t2 = datetime.time(12, 5, 13, 10233)
print(t.hour)
print(t.minute)
print(t.second)
print(t.microsecond)
print(type(t))

dt = datetime.datetime(2023, 6, 16, 0, 12, 0)
print(dt)

today = datetime.datetime.now()
# print(today)
# print(today.date())
# print(today.time())

tdelta = datetime.timedelta(days=7, hours=10)
print(today - tdelta)

print(today.strftime('%A %d, %B'))

someday = 'November. 14, 2034 17:45'
newdt = datetime.datetime.strptime(someday, '%B. %d, %Y %H:%M')
print(newdt)
print(type(newdt))