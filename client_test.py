import socket
import time
#import threaded_voice_recognition as tvr
import speech_recognition as sr

output_list = []

def check_word_matches(input, phrase_list):
    return input != None and input.lower() in phrase_list

def callback(recognizer, audio):                          # this is called from the background thread
    phrase_list = ["move north", "move east", "move west", "move south",
    "turn left", "turn right", "fire", "echo front", "echo left", "echo right"]
    global output_list
    try:
        phrase = recognizer.recognize_google(audio) #prolly wanna use ibm reocgnizer isntead
        if check_word_matches(phrase, phrase_list):
            print("Correct!")
            output_list += [phrase]
        print("You said " + phrase)  # received audio data, now need to recognize it
    except LookupError:
        print("Oops! Didn't catch that")
    except sr.UnknownValueError:
        print("Couldn't recognize speech")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.26.35.145", 5959))
s.setblocking(0)

r = sr.Recognizer()
m = sr.Microphone()
r.dynamic_energy_threshold = False #Helps increase speed but lowers accuracy
#with m as source: r.adjust_for_ambient_noise(source)      #ambient noise check bad and slow and bad

player_num = None

stop_listening = r.listen_in_background(m, callback)
s.send(bytes("Client Connected", "utf-8"))
try:
    while True:
        try:
            msg = s.recv(1024)
            decodedmsglist = msg.decode("utf-8").split()
            print(msg.decode("utf-8"))
            print(decodedmsglist, player_num == None, len(decodedmsglist) == 3, decodedmsglist[0] == "Set",  decodedmsglist[1] == "Player")
            if player_num == None and decodedmsglist[0] == "Set":
                print("reached", decodedmsglist[2], int(decodedmsglist[2]))
                player_num = int(decodedmsglist[2])
                s.send(bytes("Player {} has Connected".format(player_num), 'utf-8'))
        except:
            pass
        
        for output in output_list:
            s.send(bytes(output, 'utf-8'))
            print("sending")
            output_list.remove(output)
        
        print(player_num)
        time.sleep(1)
except KeyboardInterrupt:
    pass


stop_listening()
