import socket
import threading


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serv = socket.gethostbyname(socket.gethostname())
serv = '0.0.0.0'
port = 5959
addr = (serv, 5959)
s.bind(addr)

player_count = 1

def handle_client(conn, addr):
    print(f"New Connection ----> {addr} connected")
    
    connected = True
    conn.send(bytes("YeeeHAw I'm The Blind Bandit and I'm gonna eat you","utf-8"))
    while connected:
        msg = conn.recv(1024).decode("utf-8")
        if msg == "Client Connected":
            conn.send(bytes("Set Player {}".format(player_count)))
            player_count += 1
        print(msg)
        
    
    conn.close()
    
def start():
    s.listen()
    print(f"Listening on {serv}")
    while True:
        conn, addr = s.accept()
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        print(f"Active Connections ----> {threading.activeCount() - 4}")

print ("Server Starting.......")
start()
    








#2 players 
s.listen(2) 

while True:
    clientsocket, address = s.accept()
    print(f"Connection from {address} successful.")
    clientsocket.send(bytes("James smells weird!", "utf-8"))