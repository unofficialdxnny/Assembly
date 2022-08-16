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
        
    ##    def exe_install():
    ##        filesize = os.path.getsize("exe.txt")
    ##        if filesize == 0:
    ##             print("0 executables need to be installed: " + str(filesize))
    ##        else:
    ##            Write.Print(f"Installing Your executables!", Colors.blue_to_green, interval=0.05)
    ##            print('')
    ##            with open(f'exe.t', 'r') as b:
    ##                lines = b.readlines()
    ##                for line in lines:
    ##                    url = line
    ##                    r = requests.get(url, allow_redirects=True)
    ##                    t = urlparse(url).netloc
    ##                    print ('.'.join(t.split('.')[-2:]))
    ##                    open(f'{t}.exe', 'wb').write(r.content)
    ##                    print('')
    ##                    sleep(100)
    ##
    ##    exe_install()
        choco_install()
    
        sleep(5)
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)



    

