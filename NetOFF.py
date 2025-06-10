import colorama
import time
import random
import os
from colorama import Fore, Style
rd = Fore.RED
rs = Fore.RESET
ok = "[  " + Fore.GREEN + "OK" + Fore.RESET + "  ] "

b = f"""{rd}
 /$$   /$$             /$$      /$$$$$$  /$$$$$$$$ /$$$$$$$$
| $$$ | $$            | $$     /$$__  $$| $$_____/| $$_____/
| $$$$| $$  /$$$$$$  /$$$$$$  | $$  \\ $$| $$      | $$      
| $$ $$ $$ /$$__  $$|_  $$_/  | $$  | $$| $$$$$   | $$$$$   
| $$  $$$$| $$$$$$$$  | $$    | $$  | $$| $$__/   | $$__/   
| $$\\  $$$| $$_____/  | $$ /$$| $$  | $$| $$      | $$      
| $$ \\  $$|  $$$$$$$  |  $$$$/|  $$$$$$/| $$      | $$      
|__/  \\__/ \\_______/   \\___/   \\______/ |__/      |__/      
{rs}                                           
[ made by supremehacker69 | python really fast ddos tool ]
"""
print(b)

ip = input("[$] Target IP: ")
input("[$] Target Port (leave empty for auto): ")
print("Setting up botnets and DDoS")
time.sleep(3)
print("Setting up DDoS attacks")
time.sleep(2)
pts = ["HTTP/UDP/SYN/PING", "HTTP/UDP/PING"]

for _ in range(1200):
    pt = random.choice(pts)
    print(f"{ok} Sent 199 Packets ({pt})")

print(f"DDOS COMPLETE | {ip} IS DOWN!")
