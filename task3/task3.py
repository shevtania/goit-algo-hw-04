from pathlib import Path
from colorama import Fore
import sys

def parse_folder(path):
    path = Path(path)

# open file with exception hendler and iterate with help method iterdir()
    try:    
        for element in path.iterdir():
        
            if element.is_dir():  # if element is dir -> print it name  in blue
                print(f"{Fore.BLUE} {element} {Fore.RESET}")
                parse_folder(element)
            elif element.is_file():   # if element is file -> print it name  in yellow
                print(f"{Fore.YELLOW} {element} {Fore.RESET}")
    except FileNotFoundError:
            print(f"{Fore.MAGENTA}Wrong path{Fore.RESET}")           

if __name__ == "__main__":
    inp_path = 'Wrong input'

# save parameters of command line with help sys.argv    
    try:
        inp_path = sys.argv[1]
    except IndexError:
        print(f"{Fore.RED}Enter path to your folder as argument of exutable command {Fore.RESET}")    
    except NameError:
        print(f"{Fore.RED}Enter path to your folder as argument of exutable command {Fore.RESET}")     
   

    parse_folder(inp_path)