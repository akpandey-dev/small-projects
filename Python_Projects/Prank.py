import random
import time
import keyboard
from colorama import Fore, Style, Back, init
init(autoreset=True)

time.sleep(3)
print(Fore.BLUE + Style.BRIGHT + "WELCOME......" )
time.sleep(0.30)
print(Fore.GREEN + Style.BRIGHT + "Starting Program...." )
time.sleep(3)
print(Fore.BLUE + Style.BRIGHT + "Initiating.....Please wait" )

time.sleep(0.80)


# listKey = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','shift','enter','backspace','alt','fn','caps lock',1,2,3,4,5,6,7,8,9,0]
#     recorded = keyboard.read_event()
#     for x in listKey:
#        if(x == recorded):
#           print("THERE IS A KEY TO STOP THIS CHAOS")
# The above function was for giving user a hint but it didn't worked


x = True
while x:
    print(Fore.RED + Style.BRIGHT + Back.WHITE + "HACKER404")
    time.sleep(0.06)
    inp = ('s')
    if (keyboard.is_pressed('s')):
        print('\a')
        print(Fore.GREEN + Style.BRIGHT + "Analysing Software...")
        time.sleep(0.30)
        print(Fore.GREEN + Style.BRIGHT + "Vulnerability found...")
        time.sleep(0.35)
        print(Fore.GREEN + Style.BRIGHT + "Injecting malware Payload...")
        time.sleep(0.34)
        print(Fore.GREEN + Style.BRIGHT + "Access Denied...")
        time.sleep(0.27)
        print(Fore.GREEN + Style.BRIGHT + "Injecting Trozen Scripts...")
        time.sleep(0.100)
        print(Fore.GREEN + Style.BRIGHT + "Root Unavailable at that moment...")
        time.sleep(0.10)
        print(Fore.GREEN + Style.BRIGHT + "program Failed...")
        break
    
    
    
