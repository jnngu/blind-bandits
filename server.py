import socket
import threading
import board_game as bg


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#serv = socket.gethostbyname(socket.gethostname())
serv = '0.0.0.0'
port = 5959
addr = (serv, 5959)
s.bind(addr)

player_count = 1
gameboard = bg.Board()
playerList = [0]

actionDict = {"move north": lambda x: gameboard.moveNorth(x),"move south":lambda p: gameboard.moveSouth(p), "move east": lambda p: gameboard.moveEast(p), "move west": lambda p: gameboard.moveWest(p), "fire north":lambda p: gameboard.fireNorth(p), "fire south":lambda p: gameboard.fireSouth(p), "fire east": lambda p: gameboard.fireEast(p), "fire west": lambda p: gameboard.fireWest(p), "echo north":lambda p: gameboard.echoNorth(p), "echo south":lambda p: gameboard.echoSouth(p), "echo east": lambda p: gameboard.echoEast(p), "echo west": lambda p: gameboard.echoWest(p)}


def handle_client(conn, addr):
    print(f"New Connection ----> {addr} connected")
    global playerList
    global gameboard
    connected = True
    conn.send(bytes("YeeeHAw I'm The Blind Bandit and I'm gonna eat you","utf-8"))
    playerNum = None
    while connected:
        msg = conn.recv(1024).decode("utf-8")
        msgList = msg.split()
        
        if msg == "Client Connected":
            conn.send(bytes("Set Player {}".format(player_count)))
            playerList += bg.Player(player_count)
            playerNum = player_count
            player_count += 1
        elif msgList[0] == "0":
            actionDict[msg[2:0]](playerList[0])
        elif msgList[0] == "1":
            actionDict[msg[2:0]](playerList[1])
        
        if len(bg.soundList) != 0:
          num, snd = gameboard.soundList[0]
          if num == playerNum:
            msg = str(playernum) + " " + snd
            conn.send(bytes(msg, "utf-8"))
            bg.soundList.pop(0)


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