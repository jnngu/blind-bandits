from pydub import AudioSegment
from pydub.playback import play
import pyaudio


noises = {"bad": AudioSegment.from_wav("sounds/bad.wav"),
          "bump": AudioSegment.from_wav("sounds/bump.wav"),
          "death": AudioSegment.from_wav("sounds/death.wav"),
          "empty": AudioSegment.from_wav("sounds/empty.wav"),
          "flag": AudioSegment.from_wav("sounds/flag.wav"),
          "move": AudioSegment.from_wav("sounds/good.wav"),
          "obs": AudioSegment.from_wav("sounds/obs.wav"),
          "player": AudioSegment.from_wav("sounds/player.wav"),
          "shot": AudioSegment.from_wav("sounds/shot.wav"),
          "win": AudioSegment.from_wav("sounds/win.wav")}

def playSound(noise):
  sound = noises[noise]
  play(sound)