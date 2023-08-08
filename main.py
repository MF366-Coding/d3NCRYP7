"""
    d3NCRYP7

Encrypt, decrypt and invert files in lots of ways.
"""

from colorama import Fore, Back, Style # Used for colored text
import os
import json
import requests
from datetime import datetime
import argparse
from simple_webbrowser.simple_webbrowser import Website
import sys

script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)
script_name = os.path.basename(script_path)

VERSION = str("1.0.0")

LATEST_STABLE = False

try:
    gh_data = requests.get("https://api.github.com/repos/MF366-Coding/d3NCRYP7/releases/latest", timeout=3.5)
    data = json.loads(gh_data.text)
    LATEST_STABLE = data['tag_name']
    
except Exception:
    LATEST_STABLE = False

'''
LOGO_PNG = os.path.join(script_dir, "assets/logo.png")
ICON = os.path.join(script_dir, "assets/logo.ico")
'''

qwerty_mode = [
    "Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S", "D", "F", "G",
    "H", "J", "K", "L", "Z", "X", "C", "V", "B", "N", "M",
    # ------------------------------------------------------------------------
    "q", "w", "e", "r", "t", "y", "u", "i", "o", "p", "a", "s", "d", "f", "g",
    "h", "j", "k", "l", "z", "x", "c", "v", "b", "n", "m",
    # ------------------------------------------------------------------------
    "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

start_on_f = [
    "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T",
    "U", "V", "W", "X", "Y", "Z", "A", "B", "C", "D", "E",
    # ------------------------------------------------------------------------
    "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t",
    "u", "v", "w", "x", "y", "z", "a", "b", "c", "d", "e",
    # ------------------------------------------------------------------------
    "6", "7", "8", "9", "0", "1", "2", "3", "4", "5"]

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
print(f"{Back.YELLOW}{Fore.BLACK}{Style.BRIGHT}Welcome to d3NCRYP7 version {VERSION} and thanks for using it!{Fore.RESET}{Style.RESET_ALL}{Back.RESET}{Fore.YELLOW} :){Fore.RESET}")
print(f"{Fore.CYAN}Made by MF366 with {Fore.RED}love <3{Fore.CYAN}!{Fore.RESET}")
newline()

if LATEST_STABLE != VERSION:
    print(f"{Fore.YELLOW}[!] Aplication Version Warning\nYou are either:\n- using an older release of d3NCRYP7 (an update is recommended)\n- using an unstable release of d3NCRYP7\n- offline (with no internet connection) and d3NCRYP7 couldn't reach out to GitHub API\nAnother option is that the connection to GitHub API has timed out.{Fore.RESET}")
    newline()

class CryptFile:
    def __init__(self, file_source: str, new_file: str, _encoding: str = "utf-8", key: str = DEFAULT_KEY, verbose: bool = False):
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
            self.verbose = verbose
            
        except Exception:
            clear()
            print(f"{Fore.RED}[X] An unknown error was raised.{Fore.RESET}")
            quit()

    def encrypt(self, replacements: list):
        """
        encrypt encrypts the file at CryptFile
        """

        try:
            # 1. Opening the source
            f = open(self.file_source, "r", encoding=self.encoding)
            _txt = f.read()
            
            if self.verbose:
                print(Fore.CYAN)
                print(f"\n[i] Opened the file at '{self.file_source}' and stored its contents locally.")

            # 2. Encrypting the data
            replaced_chars = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                            "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                            "S", "T", "U", "V", "W", "X", "Y", "Z",
                            # -----------------------------------------
                            "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s", "t", "u", "v", "w", "x", "y", "z",
                            # -----------------------------------------
                            "0", "1", "2", "3", "4", "5", "6", "7", "8",
                            "9"]

            x = 0

            for i in replaced_chars:
                _txt = _txt.replace(replaced_chars[x], f"{replaced_chars[x]}{self.key}")
                x += 1
                
            if self.verbose:
                print("[i] Started using the key replacement on the locally stored data.")

            x = 0

            for i in replaced_chars:
                _txt = _txt.replace(f"{replaced_chars[x]}{self.key}", replacements[x])
                x += 1
                
            if self.verbose:
                print("[i] Started actually swapping the characters.")

            x = 0

            # 3. Output to a file
            f.close()
            f = open(self.new_file, "w", encoding=self.encoding)
            f.write(str(_txt))
            
            if self.verbose:
                print(f"[i] Stored the data at {self.new_file}.{Fore.RESET}")
                
            f.close()
            
            print(f"{Fore.BLUE}[i] Done.\n{Fore.RESET}")

        except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError):
            clear()
            print(f"{Fore.RED}[X] An encoding error was found while attempting to read the file at {self.file_source}.{Fore.RESET}")
            quit()

        except FileNotFoundError:
            clear()
            print(f"{Fore.RED}[X] The path {self.file_source} is invalid - File Not Found.{Fore.RESET}")
            quit()

        except PermissionError:
            clear()
            print(f"{Fore.RED}[X] Missing permissions for {self.file_source}.{Fore.RESET}")
            quit()

        except Exception:
            clear()
            print(f"{Fore.RED}[X] An unknown error was raised.{Fore.RESET}")
            quit()

    def decrypt(self, replaced_chars: list):
        """
        decrypt decrypts the file at CryptFile
        """

        try:
            # 1. Opening the source
            f = open(self.file_source, "r", encoding=self.encoding)
            _txt = f.read()

            if self.verbose:
                print(Fore.CYAN)
                print(f"\n[i] Opened the file at '{self.file_source}' and stored its contents locally.")

            # 2. Encrypting the data
            replacements = ["A", "B", "C", "D", "E", "F", "G", "H", "I",
                            "J", "K", "L", "M", "N", "O", "P", "Q", "R",
                            "S", "T", "U", "V", "W", "X", "Y", "Z",
                            # -----------------------------------------
                            "a", "b", "c", "d", "e", "f", "g", "h", "i",
                            "j", "k", "l", "m", "n", "o", "p", "q", "r",
                            "s", "t", "u", "v", "w", "x", "y", "z",
                            # -----------------------------------------
                            "0", "1", "2", "3", "4", "5", "6", "7", "8",
                            "9"]

            x = 0

            for i in replaced_chars:
                _txt = _txt.replace(replaced_chars[x], f"{replaced_chars[x]}{self.key}")
                x += 1

            if self.verbose:
                print("[i] Started using the key replacement on the locally stored data.")

            x = 0

            for i in replaced_chars:
                _txt = _txt.replace(f"{replaced_chars[x]}{self.key}", replacements[x])
                x += 1

            if self.verbose:
                print("[i] Started actually swapping the characters.")

            x = 0

            # 3. Output to a file
            f.close()
            f = open(self.new_file, "w", encoding=self.encoding)
            f.write(str(_txt))
            
            if self.verbose:
                print(f"[i] Stored the data at {self.new_file}.{Fore.RESET}")
                
            f.close()
            
            print(f"{Fore.BLUE}[i] Done.\n{Fore.RESET}")


        except (UnicodeDecodeError, UnicodeEncodeError, UnicodeError, UnicodeTranslateError):
            clear()
            print(f"{Fore.RED}[X] An encoding error was found while attempting to read the file at {self.file_source}.{Fore.RESET}")
            quit()

        except FileNotFoundError:
            clear()
            print(f"{Fore.RED}[X] The path {self.file_source} is invalid - File Not Found.{Fore.RESET}")
            quit()

        except PermissionError:
            clear()
            print(f"{Fore.RED}[X] Missing permissions for {self.file_source}.{Fore.RESET}")
            quit()
            
        except Exception:
            clear()
            print(f"{Fore.RED}[X] An unknown error was raised.{Fore.RESET}")
            quit()


def github_repo():
    Website("https://github.com/MF366-Coding/d3NCRYP7")


def start(_file, process, _new, _enc, _key, _mode, _github, _verb, _json_path, _config_save, *exceptions):
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
        file_used = os.path.abspath(str(_file))
        _file = file_used
        
        new_used = _file.removesuffix(os.path.basename(_file))
        
        if _new != None:
            new_usable = str(new_used + _new)
            _new = new_usable
            
        elif _new == None:
            _new = _file
            
        if _enc == None:
            _enc = "utf-8"
        
        if _key == None:
            _key = DEFAULT_KEY
        
        mode_data = "default (if source code hasn't been edited)"
        mode_name = "QWERTY Mode"
        
        if _mode == None:
            _mode = qwerty_mode
        
        elif _mode.lower() in qwerty_modes:
            _mode = qwerty_mode
            
        elif _mode.lower() in start_on_f_modes:
            _mode = start_on_f
            mode_name = "Starts on F"
        
        else:
            try:
                if _json_path != None:
                    custom_modef = open(_json_path, mode="r", encoding="utf-8")
                    
                    CUSTOM_MODES = json.load(custom_modef)
                    mode_used = CUSTOM_MODES[_mode.lower()]
                    
                    mode_name = _mode.lower()
                    _mode = mode_used
                                        
                    mode_data = 'custom'
                
                else:
                    _json_path = 'none'
                    raise Exception
            
            except Exception:
                _mode = qwerty_mode
        
        f = CryptFile(file_source=_file, new_file=_new, _encoding=_enc, key=_key, verbose=_verb)
        
        _process = "Decryption"
        
        if process == True:
            f.encrypt(_mode)
            _process = "Encryption"
        
        elif process == False:
            f.decrypt(_mode)
            _process = "Decryption"
        
        if _config_save != None:
            file = open(f"{new_used}{str(_config_save)}.d3NCRYP7.config-file", mode="w", encoding="utf-8")
            file.write(f"""d3NCRYP7 config file saved at {str(datetime.now())}
--------------------------------------------------------------------
File: {_file}
Filename given to the output file: {_new}
Directory where the original file was: {new_used}
Encoding: {_enc}
Process: {_process}
Key: {str(_key)}
Mode name: {mode_name}
Mode: {mode_data}
Path to the custom JSON file used (if 'none' then there was no custom JSON): {_json_path}
Mode definition/table (at the time of encryption/decryption): {_mode}
--------------------------------------------------------------------
Recommended actions:
- Save this file near the one you encrypted/decrypted or the original one
- Compare your configurations to the default ones at GitHub                   
""")
         
        if _github == True:
            github_repo()
    
    except Exception:
        clear()
        print(f"{Fore.RED}[X] An unknown error was raised.{Fore.RESET}")
        quit()
        
    
parser = argparse.ArgumentParser(description="d3NCRYP7")

parser.add_argument("filepath", 
                    type=str, help="The filepath of the file you'd like to encrypt/decrypt.")

parser.add_argument("--encrypt", "-e",
                    action="store_true", help="If used, this flag will change the process from decryption to encryption.")

parser.add_argument("--output-name", "--output", "-o",
                    type=str, help="The name of the new file that will result from the encryption/decryption. If not specified, the process will overwrite the existing file.")

parser.add_argument("--verbose", "-v",
                    action="store_true", help="If used, more information about what is happening will be given.")

parser.add_argument("--json-load", "-j",
                    type=str, help="If you have a JSON file where you saved custom encryption/decryption modes, make sure to indicate the path to that file using this flag. It's also a good idea to use this flag together with the --mode flag.")

parser.add_argument("--encoding",
                    type=str, help="The encoding used to decode the files. If not specified, the encoding will be utf-8 for its large support for many characters.")

parser.add_argument("--key", "-k",
                    type=str, help="The encryption/decryption key used. If not specified, the regular and recommended one will be used.")

parser.add_argument("--mode", "-m",
                    type=str, help="Encryption/decryption mode. See GitHub for all modes available. If not specified, the most basic mode (QWERTY Mode) will be used.")

parser.add_argument("--save-configs", "-s",
                    type=str, help="If specified, a config file with the arguments used will be saved under the name you selected.\nNOTE: This is only the basename! Please don't isnert an extension or a file path.")

parser.add_argument("--github",
                    action="store_true", help="If specified, the program will take you to its GitHub repo.")

try:
    args = parser.parse_args()
    start(args.filepath, args.encrypt, args.output_name, args.encoding, args.key, args.mode, args.github, args.verbose, args.json_load, args.save_configs)
    
except:
    print(f"\n{Fore.BLUE}[i] Information and tips about the given arguments.{Fore.RESET}\n{Fore.GREEN}- Please consider using the '--help' or '-h' flag if you need help.\n- Please use double quotes in the start and end of the path you inserted in case it conatins spaces\n- If you still need help, please consider visiting GitHub\n{Fore.RESET}")
    quit()
