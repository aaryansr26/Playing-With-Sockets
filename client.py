import pickle
import socket

HEADERSIZE = 10

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), 1234))


while True:
    full_msg = b""
    new_msg = True
    
    while True:
        msg = s.recv(16)
        
        if new_msg:
            msglen = msg[:HEADERSIZE].decode()
            print(f"new message length: {msglen}")
            msglen = int(msg[:HEADERSIZE])
            new_msg = False
             
        full_msg+= msg
        
        if len(full_msg) - HEADERSIZE == msglen:
            print("Full message recvd!")
            print(full_msg[HEADERSIZE:])
            
            d = pickle.loads(full_msg[HEADERSIZE:])
            print(d)
            new_msg = True
            full_msg = b"" 