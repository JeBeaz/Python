import datetime

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
work_week = {day: {'clock_in': None, 'clock_out': None, 'lunch_duration': 0} for day in days}

def format_time(t):
    hours, remainder = divmod(t.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)
    return '{:02d}:{:02d}'.format(hours, minutes)

def time_input(prompt):
    while True:
        time_str = input(prompt).strip()
        try:
            if time_str:
                time = datetime.datetime.strptime(time_str, '%I:%M %p').time()
                return time
            else:
                return None
        except ValueError:
            print("Invalid time format. Please enter time in the format 'HH:MM AM/PM'.")

def lunch_duration_input(prompt):
    while True:
        lunch_duration_str = input(prompt).strip()
        if not lunch_duration_str:
            return 0
        try:
            lunch_duration = int(lunch_duration_str)
            if lunch_duration >= 0:
                return lunch_duration
            else:
                print("Invalid lunch duration. Lunch duration must be a positive integer.")
        except ValueError:
            print("Invalid lunch duration. Lunch duration must be a positive integer.")

for day in days:
    work_day = work_week[day]
    print(f'{day}:')
    clock_in = time_input("Enter clock in time (or press enter to skip): ")
    if clock_in:
        work_day['clock_in'] = clock_in
        clock_out = time_input("Enter clock out time: ")
        work_day['clock_out'] = clock_out
        lunch_duration = lunch_duration_input("Enter lunch duration in minutes (or press enter to skip): ")
        work_day['lunch_duration'] = lunch_duration
    print()

total_duration = datetime.timedelta()
for day in days[:-1]:
    work_day = work_week[day]
    clock_in = work_day['clock_in']
    clock_out = work_day['clock_out']
    lunch_duration = work_day['lunch_duration']
    if clock_in and clock_out:
        clock_in_datetime = datetime.datetime.combine(datetime.date.today(), clock_in)
        clock_out_datetime = datetime.datetime.combine(datetime.date.today(), clock_out)
        work_duration = clock_out_datetime - clock_in_datetime - datetime.timedelta(minutes=lunch_duration)
        total_duration += work_duration
        print(f'{day}: {format_time(work_duration)}')

hours_remaining = 40*60*60 - total_duration.total_seconds()
hours_remaining = max(hours_remaining, 0)











