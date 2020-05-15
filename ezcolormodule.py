# -*- coding: utf-8 -*-
#!/usr/bin/env python3

## made by DevSodoku/BadMaliciousPyScripts https://github.com/DevSodoku/https://github.com/BadMaliciousPyScripts

class main():
    def __init__(self):
        c = ["\033[37m", "\033[31m", "\033[32m", "\033[33m", "\033[34m", "\033[35m", "\033[36m"]
        self.c = c

    def print_red(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[1] + text + self.c[0])
            else:
                print(self.c[1] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def red(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                test = self.c[1] + text + self.c[0]
                return test
            else:
                test = self.c[1] + text
                return test
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def print_green(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[2] + text + self.c[0])
            else:
                print(self.c[2] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def green(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                test = self.c[2] + text + self.c[0]
                return test
            else:
                test = self.c[2] + text
                return test
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def print_yellow(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[3] + text + self.c[0])
            else:
                print(self.c[3] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def yellow(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                test = self.c[3] + text + self.c[0]
                return test
            else:
                test = self.c[3] + text
                return test
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def print_blue(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[4] + text + self.c[0])
            else:
                print(self.c[4] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def blue(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                test = self.c[4] + text + self.c[0]
                return test
            else:
                test = self.c[4] + text
                return test
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def print_magenta(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[5] + text + self.c[0])
            else:
                print(self.c[5] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def magenta(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                test = self.c[5] + text + self.c[0]
                return test
            else:
                test = self.c[5] + text
                return test
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def print_cyan(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                print(self.c[6] + text + self.c[0])
            else:
                print(self.c[6] + text)
        else:
            print("EZcolor ValueError: The second Value has to be y,Y,n or N.")
            exit()

    def cyan(self, text, reset):
        if reset in {"y", "n", "Y", "N"}:
            if reset in {"y", "Y"}:
                test = self.c[6] + text + self.c[0]
                return test
            else:
                test = self.c[6] + text
                return test
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

    def help(self, option):
        if option in {"color", "import", "var"}:
            if option is "color":
                print("Coming soon...")
            else:
                if option is "import":
                    print("Coming soon...")
                else:
                    print("Coming soon...")
        else:
            print("Help options are color for help with the colors, import for help with importing everything and var for help with defineing variables.")
