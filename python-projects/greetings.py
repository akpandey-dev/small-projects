import random, keyboard, time, colorama
import sys

colorama.init()
thislist = ["Hello","Hi","What's up?","How are you?","Good day!","Greetings!","Salutations!","Howdy!","Hey there!"]

for name in thislist:
    for char in name:
        print(colorama.Fore.GREEN + char, end="", flush=True)
        time.sleep(0.15)  # typewriter effect
    # Blinking cursor effect
    for _ in range(3):
        print(colorama.Fore.GREEN + "|", end="", flush=True)
        time.sleep(0.2)
        print("\b \b", end="", flush=True)  # Erase cursor
        time.sleep(0.2)
    print()  # Move to nl after each word