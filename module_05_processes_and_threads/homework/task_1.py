import subprocess, shlex


def run_program():
    with open('test_input.txt', encoding='utf-8') as file:
        lines = file.readlines()
        for input_text in lines:
            res = subprocess.run(['python', 'program_test.py'], input=input_text.encode())
            print(res)


if __name__ == '__main__':
    run_program()





