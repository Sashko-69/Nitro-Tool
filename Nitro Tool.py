###############################################
######  Направено от Сашко прашкоﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞ#0001 ########
###############################################

import random, string
import os
import webbrowser
import time
import requests
import colorama
import ctypes
from colorama import Fore
from time import gmtime, sleep, strftime

def Home():
    os.system("cls")
    os.system("mode 85,21")
    colorama.init()
    ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Tool | Зареждане...")
    time.sleep(3)
    ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Tool | Главно меню")
    print(f'''
    {Fore.LIGHTCYAN_EX}[40;31m███╗   ██╗██╗████████╗██████╗  ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
    {Fore.LIGHTCYAN_EX}[40;32m████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    {Fore.LIGHTCYAN_EX}[40;33m██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║       ██║   ██║   ██║██║   ██║██║
    {Fore.LIGHTCYAN_EX}[40;34m██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║       ██║   ██║   ██║██║   ██║██║     
    {Fore.LIGHTCYAN_EX}[40;35m██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
    {Fore.LIGHTCYAN_EX}[40;36m╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

 {Fore.LIGHTCYAN_EX}   ╔══════════════════════╗
 {Fore.LIGHTCYAN_EX}   ║     Nitro  Tool      ║
 {Fore.LIGHTCYAN_EX}   ║══════════════════════║
 {Fore.LIGHTCYAN_EX}   ║ {Fore.YELLOW}[1] {Fore.LIGHTCYAN_EX}Nitro generator  ║
 {Fore.LIGHTCYAN_EX}   ║ {Fore.YELLOW}[2] {Fore.LIGHTCYAN_EX}Nitro Checker    ║
 {Fore.LIGHTCYAN_EX}   ║ {Fore.YELLOW}[E] {Fore.LIGHTCYAN_EX}Изход            ║
 {Fore.LIGHTCYAN_EX}   ╚══════════════════════╝
                                                                                                    
 {Fore.LIGHTCYAN_EX}   Направено от Сашко прашко#0491
 {Fore.LIGHTCYAN_EX}   https://discord.gg/EYuhmzRAnZ
''')


    answer = input(f"{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}NITRO TOOL{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX}> ")

    if answer == '1':
        Generator()

    elif answer == '2':
        Checker()

def Generator():
    os.system("cls")
    ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Tool | Nitro Generator")
    generated = 0

    print(f'''


    {Fore.LIGHTCYAN_EX}[40;31m███╗   ██╗██╗████████╗██████╗  ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
    {Fore.LIGHTCYAN_EX}[40;32m████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    {Fore.LIGHTCYAN_EX}[40;33m██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║       ██║   ██║   ██║██║   ██║██║
    {Fore.LIGHTCYAN_EX}[40;34m██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║       ██║   ██║   ██║██║   ██║██║     
    {Fore.LIGHTCYAN_EX}[40;35m██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
    {Fore.LIGHTCYAN_EX}[40;36m╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                           
                                                                                                                                                   
{Fore.LIGHTBLACK_EX}Направено от Сашко#0001  | Нитро код генератор
    ''')

    num=input(f"[{Fore.LIGHTCYAN_EX}Въведете количеството кодове за генериране{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX}> ")

    f=open("Nitro Codes.txt","r+", encoding='utf-8')
        
    for kele in range(int(num)):
        nitro = ''.join(random.choice(string.ascii_uppercase + string.digits + string.ascii_lowercase) for _ in range(16))
        print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTCYAN_EX}generated{Fore.LIGHTBLACK_EX}] {Fore.LIGHTCYAN_EX}https://discord.gift/{nitro}')
        ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Tool  | Generilani: %s" % generated)
        generated += 1
        f.write('https://discord.gift/')
        f.write(nitro)
        f.write("\n")

    f.close()
    input("\n\nГотови генериращи кодове. Натиснете Enter, за да се върнете в главното меню.")

    if input == input:
        Home()

def Checker():
    os.system("cls")
    colorama.init()
    checked = 0

    print(f'''


    {Fore.LIGHTCYAN_EX}[40;31m███╗   ██╗██╗████████╗██████╗  ██████╗     ████████╗ ██████╗  ██████╗ ██╗     
    {Fore.LIGHTCYAN_EX}[40;32m████╗  ██║██║╚══██╔══╝██╔══██╗██╔═══██╗    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
    {Fore.LIGHTCYAN_EX}[40;33m██╔██╗ ██║██║   ██║   ██████╔╝██║   ██║       ██║   ██║   ██║██║   ██║██║
    {Fore.LIGHTCYAN_EX}[40;34m██║╚██╗██║██║   ██║   ██╔══██╗██║   ██║       ██║   ██║   ██║██║   ██║██║     
    {Fore.LIGHTCYAN_EX}[40;35m██║ ╚████║██║   ██║   ██║  ██║╚██████╔╝       ██║   ╚██████╔╝╚██████╔╝███████╗
    {Fore.LIGHTCYAN_EX}[40;36m╚═╝  ╚═══╝╚═╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝        ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝
                                                                                                                           
  
{Fore.LIGHTBLACK_EX}Направено от Сашко#0001| Nitro Cheker
    ''')

    num=input(f"[{Fore.LIGHTCYAN_EX}Натиснете Enter, за да започнете проверка на кодовете{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX}> ")

    f=open("Nitro Codes.txt","r+", encoding='utf-8')

    for line in f:
        nitro = line.strip("\n")

        url = "https://discordapp.com/api/v6/entitlements/gift-codes/" + nitro + "?with_application=false&with_subscription_plan=true"

        r = requests.get(url)

        if r.status_code == 200:
            print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTGREEN_EX}VALID{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} {nitro}')
            break
            ctypes.windll.kernel32.SetConsoleTitleW(f"Nitro Tool | Checked: %s" % checked)
            checked += 1
        else:
            print(f'{Fore.LIGHTBLACK_EX}[{Fore.LIGHTRED_EX}INVALID{Fore.LIGHTBLACK_EX}]{Fore.LIGHTCYAN_EX} {nitro}')
            ctypes.windll.kernel32.SetConsoleTitleW(f"[Sashko Nitro Tool] от Сашко прашкоﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞﱞ#0001 | Checked: %s" % checked)
            checked += 1

    f.close()
    input("\n\nЗавършена проверка на кодовете. Натиснете Enter, за да се върнете в главното меню.")
    Home()

Home()