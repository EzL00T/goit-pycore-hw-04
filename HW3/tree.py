import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True) # Налаштувати colorama для кольору

def show_tree(path, indent=""): # Функція для показу дерева файлів
    for p in path.iterdir():
        if p.is_dir():
            print(indent + Fore.BLUE + p.name + Style.RESET_ALL)  # Вивести ім'я папки з кольором
            show_tree(p, indent + "  ") 
        else:
            print(indent + Fore.GREEN + p.name) 
if __name__ == "__main__": 
    if len(sys.argv) < 2: 
        print("Укажи шлях до папки!")
        sys.exit(1)
    folder = Path(sys.argv[1]) # Перевірка наявності аргументу
    if not folder.exists() or not folder.is_dir(): 
        print("Шлях не існує або це не папка!")
        sys.exit(1) 
    show_tree(folder)
