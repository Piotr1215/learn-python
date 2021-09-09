#!/usr/bin/env python3

import os

# List the only files and their size in the home directory and all subdirectories
def main():
    print("This is the os-fun.py file.")
    systemData = [os.name, os.getcwd(), os.getgid(), os.getuid(), os.getpid(), os.getppid(), os.getlogin()]

    # Convert the systemData list to a dictionary
    systemDict = dict(zip(['name', 'cwd', 'gid', 'uid', 'pid', 'ppid', 'login'], systemData))

    # Print the dictionary item on new line
    for k, v in systemDict.items():
        print(k, ':\t', v)

main()