from python.speak import talk
from python.speak import tspeak as speak
import subprocess

def run():
    speak("What app should I run")
    app = input(">")
    speak("Running app")
    
    try:
        bsh = subprocess.run(app, shell=True, capture_output=True, text=True)
        if bsh.returncode == 0:
            print(bsh.stdout)
        else:
            print(f"Failed to run app. Error:\n{bsh.stderr}")
            speak("Failed to run the app")
    except Exception as e:
        print(f"An exception occurred: {e}")
        speak("Failed to run the app due to an exception")