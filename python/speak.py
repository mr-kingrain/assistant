import subprocess
import threading

def talk(a):
    with open("voice.txt", "w") as f:
        f.write(a)
    subprocess.run(["bash", "bsh/speak.sh"], check=True)

def talk_p(a,p):
    with open("voice.txt", "w") as f:
        f.write(a)
    subprocess.run(["bash", "bsh/speak.sh",str(p)], check=True)



def tspeak(a):
    t = threading.Thread(target=talk, args=(a,))
    t.start()

    #this make sure that the command is threaded
    #use talk for things where it needs a pause or smth idk


