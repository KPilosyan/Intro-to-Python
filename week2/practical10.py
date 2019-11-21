import datetime, time, calendar
#2
    #a)
    dateTime = time.asctime() 
    print(dateTime)
    #b)
    localTime = time.localtime()
    print("Year:", localTime[0])
    #c)
    print("Month:", localTime[1])
    #d)
    print("Day of Week:", localTime.tm_wday)

#3)
