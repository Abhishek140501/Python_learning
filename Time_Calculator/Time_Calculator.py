def add_time(start, duration, day=None):
    days_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    time_part, meridian_part = start.split()
    start_hour, start_minute = map(int, time_part.split(':'))

    # Convert to 24-hour format
    if meridian_part.upper() == 'PM' and start_hour != 12:
        start_hour += 12
    if meridian_part.upper() == 'AM' and start_hour == 12:
        start_hour = 0

    dur_hour, dur_minute = map(int, duration.split(':'))

    # Add minutes
    final_minute = start_minute + dur_minute
    extra_hour = final_minute // 60
    final_minute %= 60

    # Add hours and calculate days
    final_hour = start_hour + dur_hour + extra_hour
    extra_day = final_hour // 24
    final_hour %= 24

    # Convert back to 12-hour format
    if final_hour == 0:
        display_hour = 12
        meridian = 'AM'
    elif final_hour < 12:
        display_hour = final_hour
        meridian = 'AM'
    elif final_hour == 12:
        display_hour = 12
        meridian = 'PM'
    else:
        display_hour = final_hour - 12
        meridian = 'PM'

    # Format minutes
    final_minute_str = f"{final_minute:02d}"

    # Handle day of week
    new_day = ''
    if day:
        day_index = days_of_week.index(day.capitalize())
        new_day_index = (day_index + extra_day) % 7
        new_day = f", {days_of_week[new_day_index]}"

    # Day suffix
    if extra_day == 1:
        day_suffix = ' (next day)'
    elif extra_day > 1:
        day_suffix = f" ({extra_day} days later)"
    else:
        day_suffix = ''

    # Build final result
    new_time = f"{display_hour}:{final_minute_str} {meridian}{new_day}{day_suffix}"
    return new_time

print(add_time('3:00 PM', '3:10'))

print(add_time('11:30 AM', '2:32', 'Monday'))

print(add_time('11:43 AM', '00:20'))

print(add_time('10:10 PM', '3:30'))

print(add_time('11:43 PM', '24:20', 'tueSday'))

print(add_time('6:30 PM', '205:12'))