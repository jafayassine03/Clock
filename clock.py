import time
import os
import threading
import random

day = True
show_seconds = True

alarm_time = input("Set alarm (HH:MM) or press Enter to skip: ").strip()
alarm_triggered = False

stopwatch_running = False
stopwatch_seconds = 0
lap_times = []

countdown_running = False
countdown_seconds = 0

world_cities = {
    "1": ("UTC", 0),
    "2": ("New York", -5),
    "3": ("London", 0),
    "4": ("Tokyo", 9),
    "5": ("Sydney", 10)
}
selected_world_city = None

quotes = [
    "Keep pushing forward 🚀",
    "Time waits for no one ⏳",
    "Stay positive, work hard 💪",
    "Dream big, achieve more 🌟",
    "Every second counts ⌛"
]

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def stopwatch():
    global stopwatch_seconds
    while True:
        if stopwatch_running:
            stopwatch_seconds += 1
        time.sleep(1)

def countdown():
    global countdown_seconds, countdown_running
    while True:
        if countdown_running and countdown_seconds > 0:
            countdown_seconds -= 1
            if countdown_seconds == 0:
                print("\nCOUNTDOWN FINISHED!")
                for _ in range(5):
                    print("\a", end="", flush=True)
                    time.sleep(0.5)
                countdown_running = False
        time.sleep(1)

threading.Thread(target=stopwatch, daemon=True).start()
threading.Thread(target=countdown, daemon=True).start()

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
        time_display += f" {time.strftime('%p', now)}"

    print("        TERMINAL DIGITAL CLOCK")
    print("       ========================")
    print()
    print(f"         {time_display}")

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

    if selected_world_city:
        city_name, city_offset = selected_world_city
        utc_now = time.gmtime()
        city_epoch = time.mktime(utc_now) + (city_offset * 3600)
        city_time = time.localtime(city_epoch)
        city_time_str = time.strftime("%H:%M:%S", city_time)
        print(f"     World Time ({city_name}): {city_time_str}")

    sw_h = stopwatch_seconds // 3600
    sw_m = (stopwatch_seconds % 3600) // 60
    sw_s = stopwatch_seconds % 60

    print()
    print(f"     Stopwatch: {sw_h:02}:{sw_m:02}:{sw_s:02}")

    if lap_times:
        print("     Laps:")
        for idx, lap in enumerate(lap_times, 1):
            lh = lap // 3600
            lm = (lap % 3600) // 60
            ls = lap % 60
            print(f"       Lap {idx}: {lh:02}:{lm:02}:{ls:02}")

    cd_h = countdown_seconds // 3600
    cd_m = (countdown_seconds % 3600) // 60
    cd_s
