import subprocess
from python.speak import talk,talk_p
from python.speak import tspeak as speak
import time

def default_pswd():
    passw = input("pswd")
    with open("python/sudopass.txt", "w") as f:
        f.write(passw)

def passwd():
    with open("python/sudopass.txt", "r") as f:
        passwd = f.read()
        return passwd


def clean(pswd):
    
    
  

    if pswd == "":

        talk("password is needed")
        pswd = input("pswd:")
    subprocess.run(["bash","bsh/commands/clean.sh"],
                    input=pswd + "\n",
                    text=True
                    )



    
import subprocess
from python.speak import talk
from python.speak import tspeak as speak




def healthchk():
    talk_p("heres the report",60)
    bsh = subprocess.run(["bash","bsh/commands/healthchk.sh"],text=True )
    bsh




def internet_test():
    speak("testing internet and internet speed.")


    
    bsh = subprocess.run(["bash","bsh/commands/internet_test.sh"],text=True )
    bsh
    
    

