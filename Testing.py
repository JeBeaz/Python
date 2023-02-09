import tkinter as tk

def calculate_total_hours():
    start_time = start_time_entry.get()
    end_time = end_time_entry.get()

    start_hour, start_minute = map(int, start_time.split(":"))
    end_hour, end_minute = map(int, end_time.split(":"))
    
    if start_time.endswith("PM") and start_hour != 12:
        start_hour += 12
    if end_time.endswith("PM") and end_hour != 12:
        end_hour += 12
    if start_time.endswith("AM") and start_hour == 12:
        start_hour = 0
    if end_time.endswith("AM") and end_hour == 12:
        end_hour = 0
    
    total_minutes = (end_hour - start_hour) * 60 + (end_minute - start_minute)
    if lunch_duration.get():
        total_minutes -= int(lunch_duration.get())

    total_hours = total_minutes / 60
    total_hours_string = f"{int(total_hours)}:{total_minutes % 60:02d}"
    result_label.config(text=f"Total hours worked: {total_hours_string}")

root = tk.Tk()
root.geometry("1600x900")
root.title("Hours Tracker")

start_time_label = tk.Label(root, text="Start Time (HH:MM AM/PM):")
start_time_label.pack()

start_time_entry = tk.Entry(root)
start_time_entry.pack()

end_time_label = tk.Label(root, text="End Time (HH:MM AM/PM):")
end_time_label.pack()

end_time_entry = tk.Entry(root)
end_time_entry.pack()

lunch_duration_label = tk.Label(root, text="Lunch Duration (minutes):")
lunch_duration_label.pack()

lunch_duration = tk.Entry(root)
lunch_duration.pack()

calculate_button = tk.Button(root, text="Calculate", command=calculate_total_hours)
calculate_button.pack()

result_label = tk.Label(root)
result_label.pack()

root.mainloop()


