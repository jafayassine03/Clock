import time
import os

day = True
show_seconds = True

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

while True:
    clear_screen()

    now = time.localtime()

    if day:
        hour = time.strftime("%H", now)
    else:
        hour = time.strftime("%I", now)

    minute = time.strftime("%M", now)

    if show_seconds:
        second = time.strftime("%S", now)
        time_display = f"{hour}:{minute}:{second}"
    else:
        time_display = f"{hour}:{minute}"

    date_display = time.strftime("%A, %d %B %Y", now)

    if not day:
        am_pm = time.strftime("%p", now)
        time_display += f" {am_pm}"

    print("       TERMINAL DIGITAL CLOCK")
    print("      ========================")
    print("\n")

    print(f"          {time_display}")

    current_hour = int(time.strftime("%H", now))

    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    print("\n")
    print(f"         {greeting}")
    print("\n")
    print(f"     {date_display}")

    print("\n")
    print(" Press CTRL + C to stop")

    time.sleep(1)
