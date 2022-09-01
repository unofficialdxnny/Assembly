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

f = open(f'config.json')
data = json.load(f)
if data['windows'] == '':
    while True:
        print(Colors.red,f"INSUFFICIENT VALUE IN 'config.json'")
        sleep(5)

else:
    ## Change window title and prints banner
    os.system('cls & title Assembly ~ unofficialdxnny')
    print(Colorate.Horizontal(Colors.red_to_purple, Center.XCenter(banner)))
    
    
    
    def choco_installer():
        choco_path = r'C:/ProgramData/chocolatey'
    
        choco_path_exists = os.path.isdir(choco_path)
        ## print(Colorate.Horizontal(Colors.red_to_purple,f"{choco_path_exists}", 1))
    
        if choco_path_exists == 'False':
            print(Colors.red,f"Chocolatey Not Found. Installing...'")
            choco_install = "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
            os.startfile("powershell.exe")
            sleep(3)
            kb.write(choco_install)
            kb.press('enter')
        else:
            print(Colors.red,f"Chocolatey Installation Found")
            sleep(2)
            print(Colors.green,f"Installing Selected Applications")
            with open('choco.ps1', 'r+') as chocolatey_application_install:
                ## os.startfile("powershell.exe")
                sleep(2)
                line = chocolatey_application_install.readlines()
                for lines in line:
                    os.system(f"choco install {lines} -y --force")
                    print(Colors.red,f"Installation of {lines} completed!'")
    
                    
    
    def aesthetics():
        ## Change mouse to .ani
        print(Colors.green,f"Changing mouse settings...'")
        path = r"HKEY_CURRENT_USER/Control Panel/Cursors"
        cur_loc = r"./Cursors/Normal Select.ani"
        os.system(f"""REG ADD "{path}" /v Default /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
        ctypes.windll.user32.SystemParametersInfoA(0x57)
        print(Colors.green,f"Completed Mouse Changes")
        ## Change WP
        img_data = requests.get("https://hdqwalls.com/badass-deadpool-wallpaper").content
        username = getpass.getuser()
        with open(f'C:/Users/{username}/Pictures/wallpaper.jpg', 'wb') as handler:
            handler.write(img_data)
            os.system(f'reg add "HKEY_CURRENT_USER\Control Panel\Desktop" /v Wallpaper /t REG_SZ /d  C:/Users/{username}/Pictures/wallpaper.jpg')
            os.system('RUNDLL32.EXE user32.dll, UpdatePerUserSystemParameters')
    
        print(Colors.green,f"Wallpaper Set'")
        sleep(3)
    
    
    def spotify():
        print(Colors.green,f"Installing Spotify Premium")
        os.system('SpotXBasic.bat')
        print(Colors.green,f"Completed Successfully")
    
    
    def performance():
            print(Colors.green,f"Enabling best Performance Mode")
            os.system('powercfg -duplicatescheme e9a42b02-d5df-448d-aa00-03f14749eb61')
            ## direct
            os.system('powercfg.exe /setactive a1841308-3541-4fab-bc81-f71556f20b4a')
            ## balanced
            os.system('powercfg.exe /setactive 381b4222-f694-41f0-9685-ff5bb260df2e')
            ## High Performance
            os.system('powercfg.exe /setactive 8c5e7fda-e8bf-4a96-9a85-a6e23a8c635c')
            ## Ultimate performance
            os.system('powercfg /setactive e9a42b02-d5df-448d-aa00-03f14749eb61')
            print('')
            print(Colors.green,f"Best PowerPlan Activated")
            
    ## def win_activate():
    ##     os.system('slmgr/ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
    ##     os.system('slmgr /skms s9.us.to')
    ##     os.system('slmgr /ato')
    
    def win_activate():
        f = open(f'config.json')
        data = json.load(f)
    
        version = platform.release()
        win = data['windows']
        if win == 'Home':
            print(Colors.green,f"Activating Windows {version} Home")
            os.system('slmgr/ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99')
            os.system('slmgr /skms s9.us.to')
            os.system('slmgr /ato')
        elif win == 'Home N':
            print(Colors.green,f"Activating Windows {version} Home N")
            os.system('slmgr/ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM')
            os.system('slmgr /skms s9.us.to')
            os.system('slmgr /ato')
        elif win == 'Home Single Language':
            print(Colors.green,f"Activating Windows {version} Home Single Language")
            os.system('slmgr/ipk 7HNRX-D7KGG-3K4RQ-4WPJ4-YTDFH')
            os.system('slmgr /skms s9.us.to')
            os.system('slmgr /ato')
        elif win == 'Home Country Specific':
            print(Colors.green,f"Activating Windows {version} Home Country Specific")
            os.system('slmgr/ipk PVMJN-6DFY6-9CCP6-7BKTT-D3WVR')
            os.system('slmgr /skms s9.us.to')
            os.system('slmgr /ato')
        elif win == 'Professional':
            print(Colors.green,f"Activating Windows {version} Professional")
            os.system('slmgr/ipk W269N-WFGWX-YVC9B-4J6C9-T83GX')
            os.system('slmgr /skms s9.us.to')
            os.system('slmgr /ato')
        elif win == 'Professional N':
            print(Colors.green,f"Activating Windows {version} Professional N")
            os.system('slmgr/ipk MH37W-N47XK-V7XM9-C7227-GCQG9')
            os.system('slmgr /skms s9.us.to')
            os.system('slmgr /ato')
        elif win == 'Education':
            print(Colors.green,f"Activating Windows {version} Education")
            os.system('slmgr/ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2')
            os.system('slmgr /skms s9.us.to')
            os.system('slmgr /ato')
        elif win == 'Education N':
            print(Colors.green,f"Activating Windows {version} Education N")
            os.system('slmgr/ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWWJ')
            os.system('slmgr /skms s9.us.to')
            os.system('slmgr /ato')
        elif win == 'Enterprise':
            print(Colors.green,f"Activating Windows {version} Enterprise")
            os.system('slmgr/ipk NPPR9-FWDCX-D2C8J-H872K-2YT43')
            os.system('slmgr /skms s9.us.to')
            os.system('slmgr /ato')
        elif win == 'Enterprise N':
            print(Colors.green,f"Activating Windows {version} Enterprise N")
            os.system('slmgr/ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4')
            os.system('slmgr /skms s9.us.to')
            os.system('slmgr /ato')
            f.close()
        else:
            print(Colors.red,f"Windows Version Not Found")
    
    win_activate()
    performance() ## adds best performance
    aesthetics() ## Sets visuals up
    spotify() ## Installs Spotify Premium Patch
    elevate() ## UAC
    choco_installer() ## Installs applications needed
    