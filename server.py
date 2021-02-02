import socket
import threading
ip= "192.168.43.22"   # server ip
port=9090
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((ip,port))

server.listen()
clients=[]
clientsname=[]


#broadcast
def broadcast(user,message):
    for client in clients:
        message=user+"-->"+message
        client.send(message.encode())


#receive
def receive():
    while True:
        client,address=server.accept()
        print(f"connected with {str(address)}")

        # client.send("N".encode())
        cli_name=client.recv(1024)
        clientname=cli_name.decode()
        clientsname.append(clientname)
        clients.append(client)

        print(f"Name of client is {cli_name.decode()}")
        broadcast(clientname,f"{clientname} conected to server !")
        client.send("conected to the server".encode())

        t1=threading.Thread(target=handle, args=(client,))
        t1.start()

#handle
def handle(client):
    while True:
        try:
            message=client.recv(1024)
            user=clientsname[clients.index(client)]
            msg=message.decode()
            print(f"{clientsname[clients.index(client)]}-->{msg}")
            broadcast(user,msg)

        except:
            index=clients.index(client)
            clients.remove(client)
            client.close()
            cliname=clientsname[index]
            clientsname.remove(cliname)

if __name__=='__main__':
    print("server is running")
    receive()

