import os, subprocess
from typing import List

if __name__ == '__main__':
    pidof_process = subprocess.run(['pidof', 'py'], text=True, capture_output=True)
    pid_list: List[int] = list(map(int, pidof_process.stdout.split()))

    for pid in pid_list:
        cmdline = open(f'/proc/{pid}/cmdline').read()
        if 'elect_main.py' in cmdline:
            os.system(f'kill {pid}')
