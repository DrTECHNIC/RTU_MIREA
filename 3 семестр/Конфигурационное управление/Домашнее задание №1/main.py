from sys import argv
from tarfile import TarFile
from application import Application
from terminal import Terminal
import json

def main():
    if len(argv) > 1:
        config_file = argv[1]
        try:
            with open(config_file, "r", encoding="UTF-8") as file:
                data = json.load(file)
                username = data.get("username")
                filesystem_path = data.get("filesystem_path")
                with TarFile(filesystem_path, 'a') as file_system:
                    Application(Terminal(username, filesystem_path, file_system)).run()
        except FileNotFoundError:
            print(f"Файл {config_file} не найден.")
    else:
        print("Аргументы не были переданы.")

if __name__ == "__main__":
    main()