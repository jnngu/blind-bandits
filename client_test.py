import socket
import time
#import threaded_voice_recognition as tvr
#import speech_recognition as sr

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("172.26.35.145", 5959))
s.setblocking(0)

#r = sr.Recognizer()
#m = sr.Microphone()
#r.dynamic_energy_threshold = False #Helps increase speed but lowers accuracy
#with m as source: r.adjust_for_ambient_noise(source)      #ambient noise check bad and slow and bad
#stop_listening = r.listen_in_background(m, tvr.callback)
s.send(bytes("I did a thing!", "utf-8"))
while True:
    try:
        msg = s.recv(1024)
        print(msg.decode("utf-8"))
    except:
        pass

    
    print("x")
    time.sleep(1)


#stop_listening()
