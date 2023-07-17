import term
import sys
import os
import time
import termcolor as tc

def clr():
    os.system('cls')
    
def load():
    term.writeLine('Loading.')
    time.sleep(0.5)
    clr()
    term.writeLine('Loading..')
    time.sleep(0.5)
    clr()
    term.writeLine('Loading...')
    time.sleep(0.5)
    clr()
    term.writeLine('Loading.')
    time.sleep(0.5)
    clr()
    term.writeLine('Loading..')
    
def print(s):
    term.writeLine(s)
    
clr()
load()
clr()
while True:
    try:
        s = input('User> ').split(' *')
        c = s[0].lower()
        if c == 'echo':
            term.writeLine(s[1])
        if c == 'echo pos':
            term.saveCursor()
            term.pos(int(s[2]), int(s[3]))
            term.write(s[1])
            term.restoreCursor()
        if c == 'clr':
            clr()
        if c == 'cmd':
            print(f'Running {s[1]}')
            os.system(s[1])
        if c == 'info':
            print('Build#: 5302')
            print('Version: 1.0.0a')
        if c == 'gui':
            os.system('python gui/gui.py')
        if c == 'app':
            os.system(f'python apps/{s[1]}/{s[1]}.py')
    except:
        print(tc.colored(f'{c}: Error while running', 'red'))
