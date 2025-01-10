import platform

RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
BLUE = "\033[34m"
MAGENTA = "\033[35m"
CYAN = "\033[36m"
WHITE = "\033[37m"
RESET = "\033[0m"

BOLD = "\033[1m"
UNDERLINE = "\033[4m"

def get_os():
    os_name = platform.system()
    print(f"{MAGENTA}Operating System: {os_name}{RESET}\n")

def get_software():
    uninstall_choice = input(f"{YELLOW}What do you want to uninstall?{RESET}\r\n{RED}[1]{RESET} Web Server\r\n{RED}[2]{RESET} Programming Languages\r\n{RED}[3]{RESET} Databases\r\n{RED}[4]{RESET} Exit\r\n")

    if uninstall_choice == "1":
        exit()
    elif uninstall_choice == "2":
        exit()
    elif uninstall_choice == "3":
        exit()
    elif uninstall_choice == "4":
        exit()
    else:
        print(f"{RED}Invalid choice!{RESET}")

def header():
    print("""

 .d8888b.                             888       888 d8b      888                    
d88P  Y88b                            888   o   888 Y8P      888                    
Y88b.                                 888  d8b  888          888                    
 "Y888b.   888  888 88888b.   .d8888b 888 d888b 888 888  .d88888  .d88b.            
    "Y88b. 888  888 888 "88b d88P"    888d88888b888 888 d88" 888 d8P  Y8b           
      "888 888  888 888  888 888      88888P Y88888 888 888  888 88888888           
Y88b  d88P Y88b 888 888  888 Y88b.    8888P   Y8888 888 Y88b 888 Y8b.               
 "Y8888P"   "Y88888 888  888  "Y8888P 888P     Y888 888  "Y88888  "Y8888            
                888                                                                 
           Y8b d88P                                                                 
            "Y88P"                                                                  
888     888          d8b                   888             888 888                  
888     888          Y8P                   888             888 888                  
888     888                                888             888 888                  
888     888 88888b.  888 88888b.  .d8888b  888888  8888b.  888 888  .d88b.  888d888 
888     888 888 "88b 888 888 "88b 88K      888        "88b 888 888 d8P  Y8b 888P"   
888     888 888  888 888 888  888 "Y8888b. 888    .d888888 888 888 88888888 888     
Y88b. .d88P 888  888 888 888  888      X88 Y88b.  888  888 888 888 Y8b.     888     
 "Y88888P"  888  888 888 888  888  88888P'  "Y888 "Y888888 888 888  "Y8888  888                                                                                                                                                                                                                                                       

""")
    
if __name__ == "__main__":
    header()
    get_os()
    get_software()