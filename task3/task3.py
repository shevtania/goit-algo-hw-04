from pathlib import Path
from colorama import Fore
import sys

def parse_folder(path):
    path = Path(path)
    try:    
        for element in path.iterdir():
        
            if element.is_dir():
                print(f"{Fore.BLUE} {element} {Fore.RESET}")
                parse_folder(element)
            elif element.is_file():
                print(f"{Fore.YELLOW} {element} {Fore.RESET}")
    except FileNotFoundError:
            print(f"{Fore.MAGENTA}Wrong path{Fore.RESET}")           

if __name__ == "__main__":
    inp_path = 'Wrong input'
    try:
        inp_path = sys.argv[1]
    except IndexError:
        print(f"{Fore.RED}Enter path to your folder as argument of exutable command {Fore.RESET}")    
    except NameError:
        print(f"{Fore.RED}Enter path to your folder as argument of exutable command {Fore.RESET}")     
   

    parse_folder(inp_path)