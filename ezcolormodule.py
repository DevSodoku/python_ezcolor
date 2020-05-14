# -*- coding: utf-8 -*-
#!/usr/bin/env python3

## made by DevSudoku https://github.com/BadMaliciousPyScripts

class ezcolor_class():
    def __init__(self):
        c = ["\033[37m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
        self.c = c

    def red(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[1] + text + self.c[0])
            else:
                print(self.c[1] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def green(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[2] + text + self.c[0])
            else:
                print(self.c[2] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def yellow(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[3] + text + self.c[0])
            else:
                print(self.c[3] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def blue(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[4] + text + self.c[0])
            else:
                print(self.c[4] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def magenta(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[5] + text + self.c[0])
            else:
                print(self.c[5] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def cyan(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[6] + text + self.c[0])
            else:
                print(self.c[6] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()
    def test(self, text):
        print("Without Reset!\n--------------")
        print(self.c[1] + text)
        print("test")
        print(self.c[2] + text)
        print("test")
        print(self.c[3] + text)
        print("test")
        print(self.c[4] + text)
        print("test")
        print(self.c[5] + text)
        print("test")
        print(self.c[6] + text)
        print("test")
        print("\nWith Reset!\n-----------")
        print(self.c[1] + text + self.c[0])
        print("test")
        print(self.c[2] + text + self.c[0])
        print("test")
        print(self.c[3] + text + self.c[0])
        print("test")
        print(self.c[4] + text + self.c[0])
        print("test")
        print(self.c[5] + text + self.c[0])
        print("test")
        print(self.c[6] + text + self.c[0])
        print("test")
