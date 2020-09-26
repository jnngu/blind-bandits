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
gameBoard = bg.Board()
playerList = [0]

actionDict = {"move north":lamda p: gameboard.moveNorth(x), "move south":lamda p: gameboard.moveSouth(x), "move east": lamda p: gameboard.moveEast(x), "move west": lamda p: gameboard.moveWest(x), "fire north":lamda p: gameboard.fireNorth(x), "fire south":lamda p: gameboard.fireSouth(x), "fire east": lamda p: gameboard.fireEast(x), "fire west": lamda p: gameboard.fireWest(x), "echo north":lamda p: gameboard.echoNorth(x), "echo south":lamda p: gameboard.echoSouth(x), "echo east": lamda p: gameboard.echoEast(x), "echo west": lamda p: gameboard.echoWest(x)}

def handle_client(conn, addr):
    print(f"New Connection ----> {addr} connected")
    global playerList
    global gameBoard
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
          num, snd = bg.soundList[0]
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