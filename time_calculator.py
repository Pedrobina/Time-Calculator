def add_time(start, duration, dayOfWeek=False):
    str_start_hour = str_start_minute = str_duration_hour = str_duration_minute = " "
    start_hour = start_minute = duration_hour = duration_minute = colon_position = hour_position = 0
    week = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    # Check the size of the started time
    if len(start) > 7:
        str_hour = start[0] + start[1]
        str_minute = start[3] + start[4]
    else:
        str_hour = start[0]
        str_minute = start[2] + start[3]

    # Check the size of the duration time
    colon_position = len(duration) - 3
    for x in range(len(duration)):
        if x < colon_position:
            str_duration_hour = str_duration_hour + duration[x]
        elif x > colon_position:
            str_duration_minute = str_duration_minute + duration[x]

    hour = int(str_hour)
    minute = int(str_minute)
    duration_hour = int(str_duration_hour)
    duration_minute = int(str_duration_minute)


    duration_hour

    print("Started Time: " + str_hour, str_minute)
    print("Duration: " + str_duration_hour, str_duration_minute)
    print("Show day of week? ", dayOfWeek)

# return new_time
