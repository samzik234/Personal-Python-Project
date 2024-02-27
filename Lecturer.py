import datetime 
x = datetime.datetime.now()
y = datetime.datetime.now()
z = datetime.datetime(2023,6,7, 12,23,27,923311)
z = datetime.datetime(2023,6,7, 12,23,27,923311)
microses = z.microsecond
print(z) 
print(z.year)
print(y.year)
print(x.strftime("%D"))


import datetime

x = datetime.datetime.now()  # Get the current datetime
week_number = x.strftime("%V")  # Get the ISO 8601 week number

print("ISO 8601 week number:", week_number)


