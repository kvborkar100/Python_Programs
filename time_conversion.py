# Using the Python language, have the function TimeConvert(num) take the num parameter being passed 
# and return the number of hours and minutes the parameter converts to 
# (ie. if num = 63 then the output should be 1:3). Separate the number of hours and minutes with a colon. 


def time_conversion(time):
    minutes, hours = 0, 0
    if time < 60:
        minutes = time
    else:
        hours = time//60
        minutes = time - hours * 60
    print("Hours = {} Minutes = {}".format(hours,minutes))


t = int(input('Enter time in minutes = '))
time_conversion(t)

