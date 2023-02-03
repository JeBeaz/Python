from datetime import datetime, timedelta

def calculate_hours_worked(clock_in, lunch_duration, clock_out):
    clock_in_time = datetime.strptime(clock_in, "%I:%M %p")
    clock_out_time = datetime.strptime(clock_out, "%I:%M %p")
    total_lunch_duration = timedelta(minutes=0)
    for lunch in lunch_duration:
        total_lunch_duration += timedelta(minutes=lunch)
    return (clock_out_time - clock_in_time) - total_lunch_duration

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
total_hours_worked = timedelta(minutes=0)
for day_of_week in days_of_week:
    clock_in = input("Enter clock-in time (HH:MM AM/PM) for {}: ".format(day_of_week))
    lunch_durations = []
    lunch = input("Enter lunch duration in minutes (or press enter to finish): ")
    while lunch != "":
        try:
            lunch_duration = int(lunch)
        except ValueError:
            print("Invalid input, please enter a number.")
            lunch = input("Enter lunch duration in minutes (or press enter to finish): ")
            continue
        lunch_durations.append(lunch_duration)
        lunch = input("Enter lunch duration in minutes (or press enter to finish): ")
    clock_out = input("Enter clock-out time (HH:MM AM/PM) for {}: ".format(day_of_week))
    hours_worked = calculate_hours_worked(clock_in, lunch_durations, clock_out)
    total_hours_worked += hours_worked
    hours = int(hours_worked.total_seconds() / 3600)
    minutes = int((hours_worked.total_seconds() / 60) % 60)
    print("Hours worked on {}: {}:{:02d}".format(day_of_week, hours, minutes))

if day_of_week == "Friday":
    hours = int(total_hours_worked.total_seconds() / 3600)
    minutes = int((total_hours_worked.total_seconds() / 60) % 60)
    print("Total hours worked this week: {}:{:02d}".format(hours, minutes))







