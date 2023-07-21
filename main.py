"""
    d3NCRYP7

Encrypt, decrypt and invert files in lots of ways.
"""

from colorama import Fore # Used for colored text and menus
import os
import sys

e = (ValueError, TypeError, NameError)

UNIX_OS = [
    "darwin", # Stands for MacOS
    "linux" # Stands for all Linux distros
]

def clear():
    if sys.platform == "win32":
        os.system("cls")
    elif sys.platform in UNIX_OS:
        os.system("clear")

def newline():
    print("\n")

class Encryption:
    def __init__(self, replacements: list, file_source: str, file_encrypted: str):
        """
        __init__ initializes Encryption

        Encryption is the general encryption system for this piece of software
        
        Args:
            replacements (list): List of chars that will replace the old ones
            file_source (str): The path to the file that will be encrypted
            file_encrypted (str): The path to where d3NCRYP7 will save the encrypted version of your file
        """
        self.replacements = replacements
        self.file_source = file_source
        if file_encrypted == "":
            self.file_encrypted = file_source
        else:
            self.file_encrypted = file_encrypted
    
    def encrypt(self):
        # 1. Opening the source
        f = open(self.file_source, "r", encoding="utf-8")
        _f = f.read()
        _txt = _f.upper()
        
        # 2. Encrypting the data
        replaced_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                          "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
                          "S", "T", "U", "V", "W", "X", "Y", "Z", "1",
                          "2", "3", "4", "5", "6", "7", "8", "9", "0"]
        
        A_text = _txt.replace("A", "z")
        Z_text = A_text.replace("Z", "a")
        
        # 3. Output to a file
        print(A_text)
        print(f"{Fore.RED}{Z_text}{Fore.RESET}")
        f.close()
        f = open(self.file_encrypted, "w", encoding="utf-8")
        f.write(str(Z_text))
        f.close()
        

class MainMenu:
    def __init__(self, properties: dict):
        """
        __init__ initializes MainMenu class

        Args:
            properties (dict): The properties for the MainMenu
        """
        self.titles = properties["titles"]
        self.desc = properties["descriptions"]
        self.fg = properties["foreground_colors"]
        self.commands = properties["commands"]
        self.header = properties["header"]
    
    def pack(self):
        """
        pack packs the menu on the commandline
        """
        clear()
        print(f"{Fore.RESET}{str(self.header)}")
        print("="*len(str(self.header)))
        newline()
        x = 0
        for i in self.titles:
            print(f"{self.fg[x]}{str(x+1)}. {self.titles[x]}\n\t{self.desc[x]}{Fore.RESET}")
            x += 1
            newline()
        print("-"*len(str(self.header)))
        print("<- d3NCRYP7 by MF366 ->")
        print("-"*len(str(self.header)))
        newline()
        try:
            y_command = int(input("Insert the command number: "))
        except e:
            try:
                y_command = int(input("Please insert a correct command: "))
            except e:
                y_command = int(input("Last chance before an exception is raised - Please insert a correct command: "))  

class Tests:
    # Check the tests dir at GitHub         
    a = {
        "titles": ["Hello!", "World!", "This is Python"],
        "descriptions": ["random stuff", ":)", "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaamazzzzing!!!!"],
        "foreground_colors": [Fore.GREEN, Fore.RED, Fore.RESET],
        "commands": [newline, clear],
        "header": "By MF366: Test # 1"
    }

    b = ["a", "B", "C", "D", "E", "F", "G", "H", "I",
        "J", "K", "L", "M", "N", "O", "P", "Q", "R", 
        "S", "T", "U", "V", "W", "X", "Y", "a", "1",
        "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    c = 'C:\Users\some_name\Coding\Python\d3NCRYP7\tests\test-001.txt'
    d = 'Good, everybody knows my name now'

    bob = Encryption(replacements=b, file_source=c, file_encrypted=d)
    bob2 = MainMenu(properties=a)