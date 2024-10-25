from os import remove
from tarfile import TarFile
from application import Application

class Terminal:

    def __init__(self, name, fs_path, file_system: TarFile):
        self.username = name
        self.fs_path = fs_path
        self.filesystem = file_system
        self.path = ""
        self.application = None

    def link(self, app: Application):
        self.application = app

    def command_dispatcher(self, string):
        line = string.split()
        if line[0] == "exit":
            self.application.exit()
        elif line[0] == "ls":
            self.ls(line[1:])
        elif line[0] == "cd":
            temp_dir = self.cd(line[1:])
            if temp_dir is not None:
                self.path = temp_dir
        elif line[0] == "touch":
            self.touch(line[1:])
        elif line[0] == "cat":
            self.cat(line[1:])
        else:
            self.application.print("Работа данной команды не предусмотрена в данном эмуляторе.", "error")

    def ls(self, args):
        work_dir = self.path
        if len(args) > 0:
            work_dir = self.cd(args[-1])
            if work_dir is None:
                self.application.print("", "command")
        items = set()
        for item in self.filesystem.getnames():
            if item.startswith(work_dir):
                ls_name = item[len(work_dir):]
                if "/" in ls_name:
                    ls_name = ls_name[:ls_name.index("/")]
                items.add(ls_name)
        self.application.print('\n'.join(sorted(filter(lambda x: len(x) > 0, items))), "command")

    def cd(self, args):
        if len(args) == 0:
            return ""
        directory = args[-1]
        directory = directory.strip('/')
        directory = directory.split('/')
        new_dir = self.path[:-1].split('/')
        if new_dir == [""]:
            new_dir = []
        for arg in directory:
            if arg == "..":
                if len(new_dir) > 0:
                    new_dir.pop()
                else:
                    self.application.print("Некорректный путь к директории.", "error")
                    return
            else:
                new_dir.append(arg)
        new_path = "/".join(new_dir) + "/"
        if new_path == "/":
            return ""
        for file in self.filesystem.getnames():
            if file.startswith(new_path):
                return new_path
        self.application.print("Директория с таким названием отсутствует.", "error")

    def touch(self, args):
        if len(args) > 0:
            filename = args[-1]
            temp_file = "__temp__" + filename
            try:
                f = open(temp_file, "w")
                f.close()
            except:
                self.application.print("Не удалось создать файл.", "error")
            try:
                self.filesystem.add(temp_file, self.path + filename)
            except:
                self.application.print("Не удалось создать файл.", "error")
            remove(temp_file)
        else:
            self.application.print("Не указано имя файла.", "error")

    def cat(self, params):
        with TarFile(self.fs_path, 'r') as file_system:
            filesystem = file_system
            file = params[-1]
            try:
                file_path = self.path + file
                if file_path in filesystem.getnames():
                    with filesystem.extractfile(file_path) as read_file:
                        self.application.print(read_file.read().decode("UTF-8").replace('\r', ''), "command")
                else:
                    self.application.print("Файл не найден в архиве", "error")
            except:
                self.application.print("Неправильное название файла", "error")
            filesystem.close()