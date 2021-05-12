def add_time(start, duration, dayOfWeek=False):
    period_of_day = str_duration_hour = str_duration_minute = spend_days_message = " "
    start_hour = start_minute = duration_hour = duration_minute = colon_position = hour_position = 0
    week = ["SUNDAY", "MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY", "SATURDAY"]


    # Check the size of the started time
    if len(start) > 7:
        str_hour = start[0] + start[1]
        str_minute = start[3] + start[4]
        period_of_day = start[6] + start[7]
    else:
        str_hour = start[0]
        str_minute = start[2] + start[3]
        period_of_day = start[5] + start[6]

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

    days = 0

    # Count Minutes
    minute = minute + duration_minute
    if minute > 60:
        duration_hour = duration_hour + int(minute / 60)
        minute = minute % 60


    # Count Hours
    sum_hour = hour + duration_hour
    if sum_hour > 24:
        days = sum_hour/24
        hour = sum_hour % 24
    elif sum_hour == 24:
        days = 1
    elif (sum_hour == 12) & (period_of_day == "PM"):
        days = 1
    else:
        hour = sum_hour

    if hour >= 12:
        if (period_of_day == "PM") & (hour == 12):
            period_of_day = "AM"
            days = days + 1
        elif (period_of_day == "AM") & (hour == 12):
            period_of_day = "PM"
        elif period_of_day == "PM":
            period_of_day = "AM"
            days = days + 1
            hour = hour - 12
        else:
            period_of_day = "PM"
            hour = hour - 12


    # Get the inicial day
    if dayOfWeek:
        count_days = int(days)
        day_of_week_position = week.index(str(dayOfWeek).upper())

        while count_days >= 1:
            if day_of_week_position == 6:
                day_of_week_position = 0
            else:
                day_of_week_position = day_of_week_position + 1
            count_days = count_days - 1

    # Defining message based in days has spend
    if int(days) > 1:
        spend_days_message = " (" + str(int(days)) + " days later)"
    elif int(days) == 1:
        spend_days_message = " (next day)"
    else:
        spend_days_message = ""

    if dayOfWeek:
        spend_days_message = week[day_of_week_position].capitalize() + spend_days_message
        period_of_day = period_of_day + ", "


    # Return of time
    output = ""
    if len(str(minute)) == 1:
        output = str(hour) + ":0" + str(minute) + " " + period_of_day + spend_days_message
    else:
        output = str(hour) + ":" + str(minute) + " " + period_of_day + spend_days_message

    return output



