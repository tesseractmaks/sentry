import shlex, subprocess
import os


def process_count():
    """ Получает к-во процессов, запущенных из-под текущего пользователя """

    file_name = os.path.abspath('size')
    with open(file_name, 'w') as file:
        username = f"whoami"
        result = subprocess.run(username, capture_output=True)
        stdout_username = result.stdout.decode()
        command_str = f"ps -Fu {stdout_username}"
        command = shlex.split(command_str)
        print(f"User: {stdout_username}\n".strip())
        popen = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)
        stdout = popen.stdout.read()
        file.write(str(stdout))
        command_str = f"awk 'NR>1{{print $6}}' {file_name}"
        comman = shlex.split(command_str)
        popen = subprocess.Popen(comman, stdout=subprocess.PIPE, universal_newlines=True)
        std = popen.stdout.read().strip()
        memory = std.strip().split('\n')
        print(len(memory), 'процессов')
    os.remove(file_name)
    return memory


def total_memory_usage(root_memory):
    """Получает Cуммарное потребление памяти древа процессов"""

    memory_sum = sum(map(int, root_memory))
    print(f'Cуммарное потребление памяти древа процессов: {(memory_sum / 1024 / 1024).__round__(2)} гигабайт')


def test_process_count():
    """ Проверяет к-во процессов, запущенных из-под текущего пользователя"""

    file_name = os.path.abspath('size_test')
    with open(file_name, 'w') as file:
        username = f"whoami"
        result = subprocess.run(username, capture_output=True)
        stdout_username = result.stdout.decode()
        command_str = f"ps -Fu {stdout_username}"
        command = shlex.split(command_str)
        popen = subprocess.Popen(command, stdout=subprocess.PIPE, universal_newlines=True)
        stdout = popen.stdout.read()
        file.write(str(stdout))
        command_str = f"awk '{{print NR,$0}}' {file_name}"
        comman = shlex.split(command_str)
        popen = subprocess.Popen(comman, stdout=subprocess.PIPE, universal_newlines=True)
        std = popen.stdout.read().strip()
        memory = std.strip()
    os.remove(file_name)
    with open('check_result.txt', 'w') as file:
        file.write(str(memory))


if __name__ == "__main__":
    root_memory = process_count()
    total_memory_usage(root_memory)
    # test_process_count()
