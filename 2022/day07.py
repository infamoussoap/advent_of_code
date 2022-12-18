from utils.utils import readlines

FILENAME = 'data/day07.txt'


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size


class Folder:
    def __init__(self, name, previous_folder):
        self.name = name
        self.previous_folder = previous_folder

        self.contents = []

    @property
    def size(self):
        if len(self.contents) == 0:
            return 0
        return sum([file.size for file in self.contents])

    def get(self, name):
        for file in self.contents:
            if file.name == name:
                return file

        raise ValueError(f"{folder_name} is not in the current working directory")

    def add(self, name, is_folder=True, size=None):
        if is_folder:
            self.contents.append(Folder(name, self))
        else:
            self.contents.append(File(name, size))

    def __repr__(self):
        return f"Folder {self.name} : {self.size}"


class CommandLine:
    def __init__(self):
        self.root = Folder('/', None)
        self.current_folder = self.root

    def __call__(self, command_result_list):
        command = command_result_list[0]

        if command[2:4] == 'cd':
            self._parse_cd(command)
        elif command[2:4] == 'ls':
            self._parse_ls(command_result_list[1:])
        else:
            raise ValueError(f"{command} is not understood")

    def _parse_cd(self, command):
        folder_name = command[5:]

        if folder_name == '/':
            self.current_folder = self.root
        elif folder_name == '..':
            self.current_folder = self.current_folder.previous_folder
        else:
            self.current_folder = self.current_folder.get(folder_name)

    def _parse_ls(self, ls_results):
        for line in ls_results:
            if line[:3] == 'dir':
                folder_name = line[4:]
                self.current_folder.add(folder_name, is_folder=True)
            else:
                size, name = line.split(' ')
                self.current_folder.add(name, is_folder=False, size=int(size))


def get_all_subfolders(folder):
    subfolders = [folder]
    for file in folder.contents:
        if isinstance(file, Folder):
            subfolders += get_all_subfolders(file)

    return subfolders


def run_terminal_commands():
    lines = readlines(FILENAME)

    commands = []
    current_command = []

    for line in lines:
        cleaned_line = line.replace('\n', '')

        if cleaned_line[0] == "$":
            commands.append([cleaned_line])
        else:
            commands[-1].append(cleaned_line)

    terminal = CommandLine()

    for command_result_list in commands:
        terminal(command_result_list)

    return terminal


def part1():
    terminal = run_terminal_commands()

    limit = 100000
    folders = get_all_subfolders(terminal.root)

    total = 0
    for folder in folders:
        folder_size = folder.size
        if  folder_size <= limit:
            total += folder_size

    return total


def part2():
    terminal = run_terminal_commands()

    total_disk_space = 70000000
    required_space = 30000000

    total_used_space = terminal.root.size
    unused_space = total_disk_space - total_used_space

    space_to_be_freed = required_space - unused_space

    folders = get_all_subfolders(terminal.root)
    sorted_folders = sorted(folders, key=lambda x: x.size)

    for folder in sorted_folders:
        if folder.size >= space_to_be_freed:
            return folder.size


if __name__ == '__main__':
    print("Advent of Code 2022 Day 07")
    print(f"Part 1: {part1()}")
    print(f"Part 2: {part2()}")
