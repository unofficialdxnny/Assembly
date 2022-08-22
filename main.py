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



def choco_installer():
    choco_path = r'C:/ProgramData/chocolatey'

    choco_path_exists = os.path.isdir(choco_path)
    ## print(Colorate.Horizontal(Colors.red_to_purple, f"{choco_path_exists}", 1))

    if choco_path_exists == 'False':
        print(Colors.red, f"Chocolatey Not Found. Installing...'")
        choco_install = "Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))"
        os.startfile("powershell.exe")
        sleep(3)
        kb.write(choco_install)
        kb.press('enter')
    else:
        print(Colors.red, f"Chocolatey Installation Found")
        sleep(2)
        print(Colors.green, f"Installing Selected Applications")
        with open('choco.ps1', 'r+') as chocolatey_application_install:
            ## os.startfile("powershell.exe")
            sleep(2)
            line = chocolatey_application_install.readlines()
            for lines in line:
                os.system(f"choco install {lines} -y --force")
                print(Colors.red, f"Installation of {lines} completed!'")

                

def aesthetics():
    ## Change mouse to .ani
    print(Colors.red, f"Changing mouse settings...'")
    path = r"HKEY_CURRENT_USER\Control Panel\Cursors"
    cur_loc = r"./Cursors/Normal Select.ani"
    os.system(f"""REG ADD "{path}" /v Default /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v AppStarting /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v Arrow /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v Crosshair /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v Hand /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v Help /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v IBeam /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v No /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v NWPen /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v Person /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v Pin /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v SizeAll /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v SizeNESW /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v SizeNS /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v SizeNWSE /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v SizeWE /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v UpArrow /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    os.system(f"""REG ADD "{path}" /v Wait /t REG_EXPAND_SZ /d "{cur_loc}" /f""")
    ctypes.windll.user32.SystemParametersInfoA(0x57)
    print(Colors.red, f"Completed...'")

    


aesthetics()
## choco_installer()