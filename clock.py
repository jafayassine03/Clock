import time
import os

day = True 

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
    second = time.strftime("%S", now)

    colon = ":" 

    time_display = f"{hour}{colon}{minute}:{second}"
    date_display = time.strftime("%A, %d %B %Y", now)


    print("       TERMINAL DIGITAL CLOCK")
    print("      ========================")
    print("\n")
    print(f"          {time_display}")
    print("\n")
    print(f"     {date_display}")

    time.sleep(1)
