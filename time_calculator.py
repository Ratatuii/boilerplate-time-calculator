def add_time(start, duration, *args):
    day_of_week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    start_time, AM_PM = start.split()
    ST_hour, ST_minutes = start_time.split(':')
    FT_hour, FT_minutes = duration.split(':')
    f_day = 0

    result = []
    total_hour = int(ST_hour) + int(FT_hour)

    total_minutes = int(ST_minutes) + int(FT_minutes)
    if total_minutes >= 60:
        total_hour += total_minutes // 60
        total_minutes = total_minutes % 60

    if total_hour >= 12:
        day_left, day_left_hour = total_hour // 12, total_hour % 12
        total_hour = day_left_hour % 12 if day_left_hour % 12 else total_hour
        if total_hour > 12:
            total_hour = total_hour - ((day_left - 1) * 12)

        if day_left > 0:
            if AM_PM == 'PM':
                f_day = ((day_left - 1) // 2) + 1
            else:
                f_day = day_left // 2

        if day_left > 0 and day_left % 2 != 0:
            AM_PM = 'AM' if AM_PM == 'PM' else 'PM'

        result.append(f'{total_hour}:{total_minutes:02d} {AM_PM}')
    else:
        result.append(f'{total_hour}:{total_minutes:02d} {AM_PM}')

    if args:
        day = args[0].title()
        if f_day >= 1:
            index_day = day_of_week.index(day)
            result.append(f", {day_of_week[((index_day + f_day) % 7)]}")
        else:
            result.append(f', {day}')

    if f_day == 1:
        result.append(' (next day)')
    elif f_day > 1:
        result.append(f' ({f_day} days later)')

    return ''.join(result)

