import datetime

now = datetime.datetime.now()

print("current date and time:", now)

print("Day of the week:", now.strftime("%A"))

print("day of the week:", now.strftime("%d-%m-%Y"))
print("day of the week:", now.strftime("%I-%m-%p"))
