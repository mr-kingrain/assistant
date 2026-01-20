from python.speak import talk
from python.speak import tspeak as speak
import subprocess

def play_music():
    speak("unpausing all music")
    command = "playerctl -a play"
    

    bsh = subprocess.run(command, shell=True, capture_output=True, text=True)
   
def pause_music():
    speak("pausing all music")
    command = "playerctl -a pause"


    bsh = subprocess.run(command, shell=True, capture_output=True, text=True)

