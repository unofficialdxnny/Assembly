import os
import getpass
import requests
import os.path
import subprocess
import sys
import ctypes
import keyboard as kb
from pystyle import *
from time import sleep
from elevate import elevate



elevate()
banner = '''

 █████╗ ███████╗███████╗███████╗███╗   ███╗██████╗ ██╗  ██╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔════╝████╗ ████║██╔══██╗██║  ╚██╗ ██╔╝
███████║███████╗███████╗█████╗  ██╔████╔██║██████╔╝██║   ╚████╔╝ 
██╔══██║╚════██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══██╗██║    ╚██╔╝  
██║  ██║███████║███████║███████╗██║ ╚═╝ ██║██████╔╝███████╗██║   
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝   
            Windows Setup script by  unofficialdxnny                                                
                                                                 
'''


## Change window title and prints banner
os.system('cls & title Assembly ~ unofficialdxnny')
print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(banner)))
print(Colorate.Horizontal(Colors.red_to_purple, "Getting things ready", 1))


choco_path = r'C:/ProgramData/chocolatey'

choco_path_exists = os.path.isdir(choco_path)
## print(Colorate.Horizontal(Colors.red_to_purple, f"{choco_path_exists}", 1))

if choco_path_exists == 'False':
    choco_install = "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
    os.startfile("powershell.exe")
    sleep(3)
    kb.write(choco_install)
    kb.press('enter')
    print(Colorate.Horizontal(Colors.red_to_purple, f"Chocolatey Not Found. Please run 'install.ps1'", 1))



else:
    print(Colorate.Horizontal(Colors.red_to_purple, f"Chocolatey is already Installed", 1))
    sleep(2)
    print(Colorate.Horizontal(Colors.red_to_purple, f"Installing Selected Applications", 1))
    with open('choco.ps1', 'r+') as chocolatey_application_install:
        os.startfile("powershell.exe")
        sleep(2)
        line = chocolatey_application_install.readlines()
        for lines in line:
            kb.write(lines)
            kb.press('enter')

    sleep(2)
