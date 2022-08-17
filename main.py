from ast import excepthandler
from ftplib import all_errors
import os, getpass, requests
from traceback import format_exception
from pystyle import *
import urllib.request
import ctypes
import sys
from urllib.parse import urlparse

banner = '''

 █████╗ ███████╗███████╗███████╗███╗   ███╗██████╗ ██╗  ██╗   ██╗
██╔══██╗██╔════╝██╔════╝██╔════╝████╗ ████║██╔══██╗██║  ╚██╗ ██╔╝
███████║███████╗███████╗█████╗  ██╔████╔██║██████╔╝██║   ╚████╔╝ 
██╔══██║╚════██║╚════██║██╔══╝  ██║╚██╔╝██║██╔══██╗██║    ╚██╔╝  
██║  ██║███████║███████║███████╗██║ ╚═╝ ██║██████╔╝███████╗██║   
╚═╝  ╚═╝╚══════╝╚══════╝╚══════╝╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝   
            Windows Setup script by  unofficialdxnny                                                
                                                                 
'''

granted = '''

 ▄▄▄       ▄████▄   ▄████▄  ▓█████   ██████   ██████      ▄████  ██▀███   ▄▄▄       ███▄    █ ▄▄▄█████▓▓█████ ▓█████▄ 
▒████▄    ▒██▀ ▀█  ▒██▀ ▀█  ▓█   ▀ ▒██    ▒ ▒██    ▒     ██▒ ▀█▒▓██ ▒ ██▒▒████▄     ██ ▀█   █ ▓  ██▒ ▓▒▓█   ▀ ▒██▀ ██▌
▒██  ▀█▄  ▒▓█    ▄ ▒▓█    ▄ ▒███   ░ ▓██▄   ░ ▓██▄      ▒██░▄▄▄░▓██ ░▄█ ▒▒██  ▀█▄  ▓██  ▀█ ██▒▒ ▓██░ ▒░▒███   ░██   █▌
░██▄▄▄▄██ ▒▓▓▄ ▄██▒▒▓▓▄ ▄██▒▒▓█  ▄   ▒   ██▒  ▒   ██▒   ░▓█  ██▓▒██▀▀█▄  ░██▄▄▄▄██ ▓██▒  ▐▌██▒░ ▓██▓ ░ ▒▓█  ▄ ░▓█▄   ▌
 ▓█   ▓██▒▒ ▓███▀ ░▒ ▓███▀ ░░▒████▒▒██████▒▒▒██████▒▒   ░▒▓███▀▒░██▓ ▒██▒ ▓█   ▓██▒▒██░   ▓██░  ▒██▒ ░ ░▒████▒░▒████▓ 
 ▒▒   ▓▒█░░ ░▒ ▒  ░░ ░▒ ▒  ░░░ ▒░ ░▒ ▒▓▒ ▒ ░▒ ▒▓▒ ▒ ░    ░▒   ▒ ░ ▒▓ ░▒▓░ ▒▒   ▓▒█░░ ▒░   ▒ ▒   ▒ ░░   ░░ ▒░ ░ ▒▒▓  ▒ 
  ▒   ▒▒ ░  ░  ▒     ░  ▒    ░ ░  ░░ ░▒  ░ ░░ ░▒  ░ ░     ░   ░   ░▒ ░ ▒░  ▒   ▒▒ ░░ ░░   ░ ▒░    ░     ░ ░  ░ ░ ▒  ▒ 
  ░   ▒   ░        ░           ░   ░  ░  ░  ░  ░  ░     ░ ░   ░   ░░   ░   ░   ▒      ░   ░ ░   ░         ░    ░ ░  ░ 
      ░  ░░ ░      ░ ░         ░  ░      ░        ░           ░    ░           ░  ░         ░             ░  ░   ░    
          ░        ░                                                                                           ░      


'''

os.system('cls')
print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(banner)))
username = getpass.getuser()
name = Write.Input("What is your username", Colors.red_to_black, interval=0.0025)
if name == username:
    Write.Print(f"{granted}", Colors.red_to_black, interval=0.001)
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
            ## os.system("powershell -command Set-ExecutionPolicy Bypass -Scope Process -Force; [System.Net.Servic
            with open(f'choco.txt', 'r+') as choco:
                line = choco.readlines()
                for lines in line:
                    os.system(f'choco install {lines} -y --force')
                print(Colors.green + f'Application {lines} installed')
        
        def cursors():
            with open(f'cur-loc.txt', 'r+') as cursors:
                line = cursors.readlines()
                for lines in line:
                    path = r"HKEY_CURRENT_USER\Control Panel\Cursors"
                    cur_loc = f"./Cursors/{cursors}.ani"
            
            with open('type.txt', 'r+') as cur_type:
                line = cur_type.readlines()
                for lines in line:
                    type = line


            os.system(f"""REG ADD "{path}" /v {type} /t REG_EXPAND_SZ /d "{cur_loc}" /f""")

            ctypes.windll.user32.SystemParametersInfoA(0x57)
        
        cursors()
        ##choco_install()
    
        sleep(5)
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)



    

