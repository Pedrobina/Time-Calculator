def add_time(start, duration, dayOfWeek=False):
    str_start_hour = str_start_minute = str_duration_hour = str_duration_minute = " "
    start_hour = start_minute = duration_hour = duration_minute = 0

    # Check the size of the started time
    if len(start) > 7:
        str_hour = start[0]+start[1]
        str_minute = start[3]+start[4]
    else:
        str_hour = start[0]
        str_minute = start[2] + start[3]

    # Check the size of the duration
    if len(duration) > 4:
        str_duration_hour = duration[0]+duration[1]
        str_duration_minute = duration[3]+duration[4]
    else:
        str_duration_hour = duration[0]
        str_duration_minute = duration[2] + duration[3]

    hour = int(str_hour)
    minute = int(str_minute)
    duration_hour = int(str_duration_hour)
    duration_minute = int(str_duration_minute)



    print("Started Time: " + str_hour, str_minute)
    print("Duration: " + str_duration_hour, str_duration_minute)


   # return new_time