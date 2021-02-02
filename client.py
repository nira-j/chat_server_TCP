import socket
import threading
import time

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)

def receivemsg(s):
    while True:
        message=s.recv(1024)
        print(f"{message.decode()}")
        print()

def sendmsg(s):
    while True:
        x=input("Enter msg: ")
        s.send(x.encode())
        if "close" in x:
            s.close()
            break

if __name__=='__main__':
    # ip=input("Enter ip of server: ")
    # port=int(input("Enter port no: "))
    s.connect(("192.168.43.226",9090))
    nname=input("Enter your nikename:")
    s.send(nname.encode())
    t1=threading.Thread(target=sendmsg, args=(s,))
    t1.start()
    t2=threading.Thread(target=receivemsg, args=(s,))
    t2.start()
        
    
