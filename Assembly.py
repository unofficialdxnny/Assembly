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
from colorama import *
import time
import json
import platform
import pyautogui as pag



banner = '''

 █████╗ ███████╗███████╗███████╗███╗   ███╗██████╗ ██╗  ██╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔════╝████╗ ████║██╔══██╗██║  ╚██╗ ██╔╝
███████║███████╗███████╗█████╗  ██╔████╔██║██████╔╝██║   ╚████╔╝ 
██╔══██║╚════██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══██╗██║    ╚██╔╝  
██║  ██║███████║███████║███████╗██║ ╚═╝ ██║██████╔╝███████╗██║   
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝   
            Windows Setup script by  unofficialdxnny                                                
                                                                 
'''

banner1 = '''
        INSUFFICIENT FIELD IN CONFIG.JSON
 █████╗ ███████╗███████╗███████╗███╗   ███╗██████╗ ██╗  ██╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔════╝████╗ ████║██╔══██╗██║  ╚██╗ ██╔╝
███████║███████╗███████╗█████╗  ██╔████╔██║██████╔╝██║   ╚████╔╝ 
██╔══██║╚════██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══██╗██║    ╚██╔╝  
██║  ██║███████║███████║███████╗██║ ╚═╝ ██║██████╔╝███████╗██║   
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝   
            Windows Setup script by  unofficialdxnny                                                
                                                                 
'''


elevate()


f = open(f'config.json')
data = json.load(f)
if data['windows'] == '':
    while True:
        os.system('cls & title Assembly ~ unofficialdxnny')
        print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(banner1)))
        sleep(1000)
else:
    ## Change window title and prints banner
    os.system('cls & title Assembly ~ unofficialdxnny')
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(banner)))
    
    def choco_install():
        print(Colorate.Color(Colors.green, 'Installinbg Chocolatey PKG Manager', True))
        with open(f'chocolatey.ps1', 'r+') as chocinstaller:
            lines = chocinstaller.readlines()
            for line in lines:
                os.system(f'powershell -command {line}')
                print(Colorate.Color(Colors.green, 'Installed Chocolatey Package Manager.', True))



    def spotify():
        print(Colorate.Color(Colors.green, 'Installing Spotify Premium Patch', True))
        os.system('SpotXBasic.bat')
        print(Colorate.Color(Colors.green, 'Installed Spotify Premium Patch.', True))

    def updates():
        print(Colorate.Color(Colors.green, 'Checking For Updates', True))
        os.system('UsoClient StartScan')        
        print(Colorate.Color(Colors.green, 'Downloading Updates', True))
        os.system('UsoClient StartDownload')
        print(Colorate.Color(Colors.green, 'Installing Updates', True))
        os.system('UsoClient StartInstall ')
        print(Colorate.Color(Colors.green, 'Restarting Device', True))
        sleep(10)
        os.system('UsoClient RestartDevice')

    def activate():
        URL = f'https://github.com/unofficialdxnny/Assembly/{data["windows"]}'
        response = requests.get(URL)
        open(f"{data['windows']}.txt", "wb").write(response.content)
        with open(f"{data["windows_key"]}.txt") as windows_key:
            lines = windows_key.readlines()
            for line in lines:
                os.system(f'slmgr/ipk {windows_key}')

    activate() ## Activate windows 10
    choco_install() ## Installs chocolatey pkg manager
    spotify() ## Installs Spotify Premium Patch