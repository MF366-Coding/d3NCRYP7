"""
    d3NCRYP7

Encrypt, decrypt and invert files in lots of ways.
"""

from colorama import Fore, Back, Style # Used for colored text
import os
import argparse
from simple_webbrowser.simple_webbrowser import Website
import sys

ICON = os.path.abspath("logo.ico")

qwerty_mode = [
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G",
    "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M",
    # ------------------------------------------------------------------------
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g",
    "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m"]

start_on_f = [
    "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E",
    # ------------------------------------------------------------------------
    "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e"]

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
    def __init__(self, file_source: str, new_file: str, _encoding: str = "utf-8", key: str = DEFAULT_KEY):
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
            self.new_file = new_file
            
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
            f = open(self.new_file, "w", encoding=self.encoding)
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
            f = open(self.new_file, "w", encoding=self.encoding)
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


def start(_file, process, _new, _enc, _key, _mode, _github):
    """
    start starts the encryption/decryption UI
    """
    
    qwerty_modes = [
        "qwerty_mode",
        "qwerty", 
        "mode_qwerty"
    ]
    
    start_on_f_modes = [
        "f_start",
        "f_starts",
        "start_f",
        "starts_f"
    ]
    
    try:
        if _new == None:
            _new = _file
            
        if _enc == None:
            _enc = "utf-8"
        
        if _key == None:
            _key = DEFAULT_KEY
            
        if _mode == None:
            _mode = qwerty_mode
        
        elif _mode.lower() in qwerty_modes:
            _mode = qwerty_mode
            
        elif _mode.lower() in start_on_f_modes:
            _mode = start_on_f
        
        f = CryptFile(file_source=_file, new_file=_new, _encoding=_enc, key=_key)
        
        if process == True:
            f.encrypt(_mode)
        
        elif process == False:
            f.decrypt(_mode)
            
        if _github == True:
            github_repo()
            
    except Exception:
        clear()
        print(f"{Back.RED}An unknown error was raised.{Back.RESET}")
        quit()
        
    
parser = argparse.ArgumentParser(description="d3NCRYP7")

parser.add_argument("filepath", type=str, help="The filepath of the file you'd like to encrypt/decrypt.")
parser.add_argument("-e", "--encrypt", action="store_true", help="If used, this flag will change the process from decryption to encryption.")
parser.add_argument("--new_filename", "-nf", type=str, help="The name of the new file that will result from the encryption/decryption. If not specified, the process will overwrite the existing file.")
parser.add_argument("--encoding", type=str, help="The encoding used to decode the files. If not specified, the encoding will be utf-8 for its large support for many characters.")
parser.add_argument("--key", "-k", type=str, help="The encryption/decryption key used. If not specified, the regular and recommended one will be used.")
parser.add_argument("--mode", "-m", type=str, help="Encryption/decryption mode. See GitHub for all modes available. If not specified, the most basic mode (QWERTY Mode) will be used.")
parser.add_argument("--github", action="store_true", help="If specified, the program will take you to its GitHub repo.")

args = parser.parse_args()

clear()
print(f"{Back.YELLOW}{Style.BRIGHT}Welcome to d3NCRYP7!{Style.RESET_ALL}{Back.RESET}")
print(f"{Fore.CYAN}By: MF366{Fore.RESET}")
newline()

start(args.filepath, args.encrypt, args.new_filename, args.encoding, args.key, args.mode, args.github)
