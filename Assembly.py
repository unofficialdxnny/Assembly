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
import winreg, ctypes, win32con




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
                ## os.system('cmd')


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
        sleep(10)


    def activate():
        print(Colorate.Color(Colors.green, 'Activating Windows', True))
        name = data["windows_key"]
        with open(f"{name}.txt", "r+") as windows_key:
            lines = windows_key.readlines()
            for line in lines:
                os.system(f'slmgr/ipk {line}')
                os.system('slmgr /skms s9.us.to')
                os.system('slmgr /ato')
                print(Colorate.Color(Colors.green, f'Activated Windows {name}', True))

    def powerplan():
        print(Colorate.Color(Colors.green, 'Setting Best Power Plan', True))
        os.system('powercfg.exe /setactive 381b4222-f694-41f0-9685-ff5bb260df2e')
        os.system('powercfg.exe /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c')
        os.system('powercfg.exe /setactive a1841308-3541-4fab-bc81-f71556f20b4a')
        os.system('powercfg.exe /setactive f996c0c1-3756-4d6b-9467-5510c2776be3')
        print(Colorate.Color(Colors.green, 'Best PowerPlan Set', True))


    def aesthetics():
        print(Colorate.Color(Colors.green, 'Setting Aesthetics', True))
        path = r"HKEY_CURRENT_USER\Control Panel\Cursors"
        cursor = r"./Cursors/Normal Select.ani"
        os.system(f"""REG ADD "{path}" /v Arrow /t REG_EXPAND_SZ /d "{cursor}" /f""")
        ctypes.windll.user32.SystemParametersInfoA(0x57)

    ## method from stackoverflow
    def setWallpaper(path):
        FILL,FIT,STRETCH,TILE,CENTER,SPAN = 0,1,2,3,4,5
        MODES = (0,10),(0,6),(0,2),(1,0),(0,0),(0,22)
        value1,value2 = MODES[FILL] # choose mode here

        key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Control Panel\Desktop", 0, winreg.KEY_WRITE)
        winreg.SetValueEx(key, "TileWallpaper", 0, winreg.REG_SZ, str(value1))
        winreg.SetValueEx(key, "WallpaperStyle", 0, winreg.REG_SZ, str(value2))
        winreg.CloseKey(key)
        changed = win32con.SPIF_UPDATEINIFILE | win32con.SPIF_SENDCHANGE
        ctypes.windll.user32.SystemParametersInfoW(win32con.SPI_SETDESKWALLPAPER,0,path,changed)

    setWallpaper("G:\Projects\Assembly\Wallpaper.jfif")



    def choco_install_apps():
        ## paevate()
        ## pag.keyDown('win')
        ## pag.keyDown('r')
        ## pag.keyUp('win')
        ## pag.keyUp('r')
        ## pag.typewrite('cmd')
        ## pag.keyDown('enter')
        ## pag.keyUp('enter')
        ## paeep(2)
        ## pag.typewrite('cd G:\Projects\Assembly')
        ## pag.keyDown('enter')
        ## pag.keyUp('enter')        
        ## pag.typewrite('python G:\Projects\Assembly\choco.py')
        ## pag.keyDown('enter')
        ## pag.keyUp('enter')
        with open(f'choco.ps1', 'r+') as choco_install_apps:
            lines = choco_install_apps.readlines()
            for line in lines:
                os.system(line)
        









    
    
    
    powerplan() ## Sets best powerplan
    choco_install() ## Installs chocolatey pkg manager
    spotify() ## Installs Spotify Premium Patch
    choco_install_apps() ## installs applications needed
    Aesthetics() ## change windows aesthetics
    setwallpaper() ## Sets windows wallpaper
    activate() ## Activate windows 10
    updates() ## Check for updates
    print(Colorate.Color(Colors.green, 'Windows Setup Complete', True))