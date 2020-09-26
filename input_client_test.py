from socket import*
import sys
import select

HOST = '172.26.35.145'
PORT = 5959
s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))
s.setblocking(False)
while True:
    socket_list = [sys.stdin, s]

    # Get the list sockets which are readable
    read_sockets, write_sockets, error_sockets = select.select(
        socket_list, [], [])

    for sock in read_sockets:
        #incoming message from remote server
        if sock == s:
            data = sock.recv(1024)
            if not data:
                print('\nDisconnected from server')
                break
            else:
                #print data
                sys.stdout.write("{}\n".format(data.decode('utf-8')))
                # prints the message received
                print("New message: " + repr(data))
                #prompt()
        #user entered a message
        else:
            msg = sys.stdin.readline()
            s.send(bytes(msg,'utf-8'))
            #prompt()
