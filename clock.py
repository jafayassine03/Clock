import time
import os

day = True
show_seconds = True

alarm_time = input("Set alarm (HH:MM) or press Enter to skip: ").strip()
alarm_triggered = False

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
    print()
    print(f"          {time_display}")

    current_hour = int(time.strftime("%H", now))

    if 5 <= current_hour < 12:
        greeting = "Good Morning"
    elif 12 <= current_hour < 18:
        greeting = "Good Afternoon"
    else:
        greeting = "Good Evening"

    print()
    print(f"         {greeting}")
    print()
    print(f"     {date_display}")

    if alarm_time:
        print()
        print(f"     Alarm: {alarm_time}")

    current_time = time.strftime("%H:%M", now)

    if alarm_time and current_time == alarm_time and not alarm_triggered:
        print()
        print("     ALARM! ALARM! ALARM!")
        for _ in range(5):
            print("\a", end="", flush=True)
            time.sleep(0.5)
        alarm_triggered = True

    print()
    print(" Press CTRL + C to stop")

    time.sleep(1)
