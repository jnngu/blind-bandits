import speech_recognition as sr

def check_word_matches(input, phrase_list):
    return input != None and input.lower() in phrase_list


def callback(recognizer, audio):                          # this is called from the background thread
    phrase_list = ["move north", "move east", "move west", "move south",
    "turn left", "turn right", "fire", "echo front", "echo left", "echo right"]
    try:
        phrase = recognizer.recognize_google(audio) #prolly wanna use ibm reocgnizer isntead
        if check_word_matches(phrase, phrase_list):
            print("Correct!")
        print("You said " + phrase)  # received audio data, now need to recognize it
    except LookupError:
        print("Oops! Didn't catch that")
    except sr.UnknownValueError:
        print("Couldn't recognize speech")

r = sr.Recognizer()
m = sr.Microphone()
r.dynamic_energy_threshold = False #Helps increase speed but lowers accuracy
#with m as source: r.adjust_for_ambient_noise(source)      #ambient noise check bad and slow and bad
stop_listening = r.listen_in_background(m, callback)

import time
x = 1
try:
    while True:
        #Do things here
        print(x)
        time.sleep(1)
        x = x + 1
except KeyboardInterrupt:
    pass

stop_listening()                                          # call the stop function to stop the background thread
