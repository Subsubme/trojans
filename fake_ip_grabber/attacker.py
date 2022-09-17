import socket, os

host = "127.0.0.1"
port = 6930

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((host,port))
    s.listen(2)
    s, addr = s.accept()
    print(f"connected to {addr} the idiot succesfuly took the bait")
    data = s.recv(1200).decode("utf-8")
    with open("hello.txt","w") as f:
        f.write(f"the victims ip is {data}")
        f.close()
    s.close()