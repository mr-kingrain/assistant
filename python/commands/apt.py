import subprocess
from python.speak import talk


def default_pswd():
    passw = input("pswd")
    with open("python/sudopass.txt", "w") as f:
        f.write(passw)

def passwd():
    with open("python/sudopass.txt", "r") as f:
        passwd = f.read()
        return passwd


def apt(a,pswd):
    
    
    if a == 1:

        if pswd == "":

            talk("password is needed")
            pswd = input("pswd:")
        else:
            talk("running")
        subprocess.run(["bash","bsh/commands/apt.sh"],
                       input=pswd + "\n",
                       text=True
                       )

        pass
        

    
