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


os.system('cls')
print(Colorate.Horizontal(Colors.red_to_black, Center.XCenter(banner)))
username = getpass.getuser()
name = Write.Input("What is your username : ", Colors.red_to_black, interval=0.0025)
if name == username:
    ## Write.Print(f"{granted}", Colors.red_to_black, interval=0.001)
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
            ## while x < 7:
            ##     with open(f'cur-loc.txt', 'r+') as cursors:
            ##         line = cursors.readlines()
            ##         for lines in line:
            path = r"HKEY_CURRENT_USER\Control Panel\Cursors"
            ## cur_loc = f"./Cursors/{lines}.ani"
            
            type = ['Arrow', 'AppStarting', 'Crosshair', 'Hand', 'Help', 'No', 'NWPen', 'Wait', 'UpArrow', 'SizeAll', '']
            x = 0


            os.system(f"""REG ADD "{path}" /v {type[x]} /t REG_EXPAND_SZ /d "./Cursors/Normal Select.ani" /f""")
            x = +1
            os.system(f"""REG ADD "{path}" /v {type[x]} /t REG_EXPAND_SZ /d "./Cursors/Working in Background.ani" /f""")
            x = +1
            os.system(f"""REG ADD "{path}" /v {type[x]} /t REG_EXPAND_SZ /d "./Cursors/Precission Select.ani" /f""")
            x = +1
            os.system(f"""REG ADD "{path}" /v {type[x]} /t REG_EXPAND_SZ /d "./Cursors/Link Select.ani" /f""")
            x = +1
            os.system(f"""REG ADD "{path}" /v {type[x]} /t REG_EXPAND_SZ /d "./Cursors/Help Select.ani" /f""")
            x = +1
            os.system(f"""REG ADD "{path}" /v {type[x]} /t REG_EXPAND_SZ /d "./Cursors/Unavailable.ani" /f""")
            x = +1
            os.system(f"""REG ADD "{path}" /v {type[x]} /t REG_EXPAND_SZ /d "./Cursors/Handwritting.ani" /f""")
            x = +1
            os.system(f"""REG ADD "{path}" /v {type[x]} /t REG_EXPAND_SZ /d "./Cursors/Busy.ani" /f""")
            x = +1
            os.system(f"""REG ADD "{path}" /v {type[x]} /t REG_EXPAND_SZ /d "./Cursors/Alternative Select.ani" /f""")
            x = +1
            os.system(f"""REG ADD "{path}" /v {type[x]} /t REG_EXPAND_SZ /d "./Cursors/Move.ani" /f""")
            ctypes.windll.user32.SystemParametersInfoA(0x57)
                    

        cursors()
        ##choco_install()
    
        
    else:
        # Re-run the program with admin rights
        ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)



    

