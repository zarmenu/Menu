import os,sys
import time
from colorama import Fore
import pystyle
import subprocess

def pprint(s):
    for c in s + '\n':
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.8 / 100)

key = input(f"{Fore.BLUE}Press Enter{Fore.RESET}: ")
if key != "":
    pprint(f"{Fore.RED}Invalid key. Try Free Key...{Fore.RESET}")
    pprint(f"{Fore.WHITE}Exiting... GoodBye 👋{Fore.RESET}")
    time.sleep(3)
    exit()



class menu:
    def __init__(self):
        pass

    def main(self):
        subprocess.run("cls", shell=True) # Clears the command line

        print(f'{Fore.LIGHTMAGENTA_EX}Menu v0.1 Free ^| YouTube: zarmenu{Fore.RESET}')
        pystyle.Write.Print("""


███████╗░█████╗░██████╗░  ███╗░░░███╗███████╗███╗░░██╗██╗░░░██╗
╚════██║██╔══██╗██╔══██╗  ████╗░████║██╔════╝████╗░██║██║░░░██║
░░███╔═╝███████║██████╔╝  ██╔████╔██║█████╗░░██╔██╗██║██║░░░██║
██╔══╝░░██╔══██║██╔══██╗  ██║╚██╔╝██║██╔══╝░░██║╚████║██║░░░██║
███████╗██║░░██║██║░░██║  ██║░╚═╝░██║███████╗██║░╚███║╚██████╔╝
╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚═╝░░░░░╚═╝╚══════╝╚═╝░░╚══╝░╚═════╝░v0.1 menu""", pystyle.Colors.purple_to_blue, interval=0)
        
        print("")
        print("")

        print(f'                                     {Fore.GREEN}[{Fore.RESET} {Fore.MAGENTA}Made By{Fore.RESET} {Fore.GREEN}]{Fore.RESET}{Fore.GREEN} [{Fore.RESET}{Fore.YELLOW}@ultve{Fore.RESET}{Fore.GREEN}]{Fore.RESET}')


        print("")
        print("")
        print("")

x = menu()
x.main()

import os
from colorama import Fore

folders = ["free", "vip", "vip_plus"]

while True:
    print(f"{Fore.RED}Select a folder{Fore.RESET}: ")
    for i, folder in enumerate(folders):
        print(f"{i+1}. {folder}")
    choice = input()
    if choice.isdigit() and int(choice) <= len(folders):
        assets = [file for file in os.listdir(f"assets/{folders[int(choice)-1]}") if file.endswith(".py")]
        while True:
            print(f"{Fore.RED}Select a file{Fore.RESET}: ")
            for i in range(0, len(assets), 20):
                for j in range(i, min(i+20, len(assets))):
                    print(f"{j+1}. {assets[j]}")
                file_choice = input()
                if file_choice.isdigit() and int(file_choice) <= len(assets):
                    os.system(f"python assets/{folders[int(choice)-1]}/{assets[int(file_choice)-1]}")
                elif file_choice == "0":
                    break
                else:
                    print(f"{Fore.RED}Invalid choice. Please try again.{Fore.RESET}")
            if file_choice == "99":
                break
    elif choice == "99":
        break
print(f"{Fore.RED}Exiting...{Fore.RESET}")


