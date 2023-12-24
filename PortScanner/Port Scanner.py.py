import socket
from pyfiglet import Figlet
from colorama import Fore, Style

f = Figlet(font='slant')
print(Fore.GREEN + f.renderText('Port Scan'))
print(Fore.MAGENTA + "https://pxrsoftware.com")
print(Fore.GREEN + "---------------------------------")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(5)

print("EX: example.com")
host = input(Fore.MAGENTA + "Enter IP or Hostname: ")
print("--" * 10)
print("EX: 80")
port = int(input(Fore.MAGENTA + "Enter the Port you want to scan: "))

def portScanner(port):
    if s.connect_ex((host, port)):
        print()
        print("Port is closed")
    else:
        print()
        print("Port is open")

portScanner(port)