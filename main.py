from ast import excepthandler
from ftplib import all_errors
import os, getpass, requests
from traceback import format_exception
from pystyle import *
import urllib.request
import ctypes
import sys

banner = '''

 █████╗ ███████╗███████╗███████╗███╗   ███╗██████╗ ██╗  ██╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔════╝████╗ ████║██╔══██╗██║  ╚██╗ ██╔╝
███████║███████╗███████╗█████╗  ██╔████╔██║██████╔╝██║   ╚████╔╝ 
██╔══██║╚════██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══██╗██║    ╚██╔╝  
██║  ██║███████║███████║███████╗██║ ╚═╝ ██║██████╔╝███████╗██║   
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝   
                 Windows Setup for unofficialdxnny                                                
                                                                 
'''

def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False
if is_admin():
    os.system('cls & title Windows Setup ~ unofficialdxnny')
    print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(banner)))

    ## install chocolatey files
    def choco_install():
        print(Colors.green + 'Installing chocolatey applications')
        ## os.system("powershell -command Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.ServicePointManager]::SecurityProtocol = [System.Net.ServicePointManager]::SecurityProtocol -bor 3072; iex ((New-Object System.Net.WebClient).DownloadString('https://community.chocolatey.org/install.ps1'))")
        with open(f'choco.txt', 'r+') as choco:
            line = choco.readlines()
            for lines in line:
                os.system(f'choco install {lines} -y --force')
            print(Colors.green + f'Application {lines} installed')

    choco_install()
    sleep(5)
else:
    # Re-run the program with admin rights
    ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)



