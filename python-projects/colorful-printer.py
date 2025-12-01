import colorama, random, time
from colorama import Fore, Back, Style
colorama.init()

s = ""
colors = ["RED","BLUE","GREEN","YELLOW","CYAN","WHITE","MAGENTA","LIGHTRED_EX","LIGHTBLUE_EX","LIGHTGREEN_EX","LIGHTYELLOW_EX","LIGHTCYAN_EX","LIGHTWHITE_EX","LIGHTMAGENTA_EX"]
noted = []


input("Press Enter to start...")
user_input = input("Type the word...")
if user_input.__len__() == 0:
    s = "An error has occurred because you haven't typed any word!"
else:
    s = user_input

for i in s:
    col = random.choice(colors)
    noted.append(col)
    if noted.__len__() > 2 and noted[-1] == noted[-2] and noted[-1] == noted[-3]:
        while col == noted[-1]:
            col = random.choice(colors)
        noted[-1] = col
    print(Fore.__getattribute__(col) + i, end="", flush=True)
    time.sleep(0.1)