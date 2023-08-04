"""
    d3NCRYP7

Encrypt, decrypt and invert files in lots of ways.
"""

from colorama import Fore, Back, Style # Used for colored text
import os
from simple_webbrowser.simple_webbrowser import Website
import sys
import customtkinter as ctk

ICON = os.path.abspath("logo.ico")

qwerty_mode = [
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G",
    "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M",
    # ------------------------------------------------------------------------
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g",
    "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

DEFAULT_KEY = "_-|]>/=!^%#*:.'\";+@<[?()&,`$*&<($|>^]!\\?_%)+@[(/.~[:;~][!&<|/)=^>~%+_`;:\"](@?,.$*'/#;(|@?&],!_>~[%+\"#$%#/(=%&/&$/%$&#$&%)=&%&&/%$=?(?=?»(«>>>><<<<--,.,_;_º+º+~ª*ª;_;_))"

e = (ValueError, TypeError, NameError)

UNIX_OS = [
    "darwin", # Stands for MacOS
    "linux" # Stands for all Linux distros
]

def clear():
    """
    clear clears the screen

    Either uses cls or clear, based on your OS
    """
    if sys.platform == "win32":
        os.system("cls")
    elif sys.platform in UNIX_OS:
        os.system("clear")

def newline():
    """
    newline simply prints a break line
    """
    print("\n")

clear()

class CryptFile:
    def __init__(self, file_source: str, _encoding: str = "utf-8", key: str = DEFAULT_KEY):
        """
        __init__ _summary_

        _extended_summary_

        Args:
            file_source (str): the file to encrypt/decrypt
            _encoding (str, optional): the encoding of the file. Defaults to "utf-8".
            key (str, optional): the key for encryption/decryption. Defaults to DEFAULT_KEY.
        """
        
        try:
            self.file_source = file_source
            self.encoding = _encoding
            self.key = key
            
        except Exception:
            clear()
            print(f"{Back.RED}An unknown error was raised.{Back.RESET}")
            quit()

    def encrypt(self, replacements: list):
        """
        encrypt encrypts the file at CryptFile
        """

        try:
            # 1. Opening the source
            f = open(self.file_source, "r", encoding=self.encoding)
            _txt = f.read()

            # 2. Encrypting the data
            replaced_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                            "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                            "S", "T", "U", "V", "W", "X", "Y", "Z",
                            # -----------------------------------------
                            "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s", "t", "u", "v", "w", "x", "y", "z"]

            x = 0

            for i in replaced_chars:
                _txt = _txt.replace(replaced_chars[x], f"{replaced_chars[x]}{self.key}")
                x += 1

            x = 0

            for i in replaced_chars:
                _txt = _txt.replace(f"{replaced_chars[x]}{self.key}", replacements[x])
                x += 1

            x = 0

            # 3. Output to a file
            f.close()
            f = open(f"{self.file_source}.d3NCRYP7.encrypted", "w", encoding=self.encoding)
            f.write(str(_txt))
            f.close()

        except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError):
            clear()
            print(f"{Back.RED}An encoding error was found while attempting to read the file at {self.file_source}.{Back.RESET}")
            quit()

        except FileNotFoundError:
            clear()
            print(f"{Back.RED}The path {self.file_source} is invalid - File Not Found.{Back.RESET}")
            quit()

        except PermissionError:
            clear()
            print(f"{Back.RED}Missing permissions for {self.file_source}.{Back.RESET}")
            quit()

        except Exception:
            clear()
            print(f"{Back.RED}An unknown error was raised.{Back.RESET}")
            quit()

    def decrypt(self, replaced_chars: list):
        """
        decrypt decrypts the file at CryptFile
        """

        try:
            # 1. Opening the source
            f = open(self.file_source, "r", encoding=self.encoding)
            _txt = f.read()

            # 2. Encrypting the data
            replacements = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                            "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                            "S", "T", "U", "V", "W", "X", "Y", "Z",
                            # -----------------------------------------
                            "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s", "t", "u", "v", "w", "x", "y", "z"]

            x = 0

            for i in replaced_chars:
                _txt = _txt.replace(replaced_chars[x], f"{replaced_chars[x]}{self.key}")
                x += 1

            x = 0

            for i in replaced_chars:
                _txt = _txt.replace(f"{replaced_chars[x]}{self.key}", replacements[x])
                x += 1

            x = 0

            # 3. Output to a file
            f.close()
            f = open(f"{self.file_source}.d3NCRYP7.decrypted", "w", encoding=self.encoding)
            f.write(str(_txt))
            f.close()

        except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError):
            clear()
            print(f"{Back.RED}An encoding error was found while attempting to read the file at {self.file_source}.{Back.RESET}")
            quit()

        except FileNotFoundError:
            clear()
            print(f"{Back.RED}The path {self.file_source} is invalid - File Not Found.{Back.RESET}")
            quit()

        except PermissionError:
            clear()
            print(f"{Back.RED}Missing permissions for {self.file_source}.{Back.RESET}")
            quit()
            
        except Exception:
            clear()
            print(f"{Back.RED}An unknown error was raised.{Back.RESET}")
            quit()


def github_repo():
    Website("https://github.com/MF366-Coding/d3NCRYP7")

def encrypt_ui() -> None:
    pass

def decrypt_ui() -> None:
    pass
    
def start() -> None:
    """
    start starts the encryption/decryption UI
    """

    ROOT = ctk.CTk()
    ROOT.title("d3NCRYP7 - Encrypt and Decrypt Files")
    ROOT.geometry("325x150")
    ROOT.resizable(False, False)
    if sys.platform == "win32":
        ROOT.iconbitmap(ICON)
    
    frame_1 = ctk.CTkFrame(ROOT)
    
    label_1 = ctk.CTkLabel(ROOT, text_color="yellow", font=("JetBrains Mono Bold", 16), text="Welcome to d3NCRYP7 by MF366!")
    label_2 = ctk.CTkLabel(ROOT, text="", font=("JetBrains Mono", 10))
    
    butt_1 = ctk.CTkButton(frame_1, corner_radius=6, fg_color="#49C4E0", text_color="black", font=("JetBrains Mono", 13), text="Encrypt", command=encrypt_ui)
    butt_2 = ctk.CTkButton(frame_1, corner_radius=6, fg_color="#8A8ADA", text_color="black", font=("JetBrains Mono", 13), text="Decrypt", command=decrypt_ui)
    butt_3 = ctk.CTkButton(ROOT, corner_radius=6, fg_color="#DDE8EA", text_color="black", font=("JetBrains Mono", 12), text="At GitHub", command=github_repo)
    
    label_clone_1 = label_2
    
    # in progress
    
    label_1.pack()
    label_2.pack()
    frame_1.pack()
    butt_1.pack()
    butt_2.pack()
    butt_3.pack()
    
    ROOT.mainloop()

if __name__ == "__main__":
    try:
        clear()
        print(f"{Back.YELLOW}{Style.BRIGHT}Welcome to d3NCRYP7!{Style.RESET_ALL}{Back.RESET}")
        print(f"{Fore.CYAN}By: MF366{Fore.RESET}")
        newline()
        
        start()
        
    except Exception:
        pass
