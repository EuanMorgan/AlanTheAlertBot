import subprocess
import os
import time
from termcolor import colored
import winsound


def play():
    winsound.PlaySound("alarm", winsound.SND_ASYNC | winsound.SND_ALIAS )
os.system('color')

ips = {"dad":"192.168.1.10","mam":"192.168.1.72","me":"192.168.1.86"}

with open(os.devnull, "wb") as limbo:

            while True:
                os.system('cls')
                for (name,ip) in ips.items():
                    
                
                    result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                            stdout=limbo, stderr=limbo,shell=True).wait()

                    print(result)
                    print("Pinging {}".format(name))
                    if result:
                             
                            print(ip, colored('inactive', 'red'))
                    else:
                            print(ip, colored('active', 'green'))
                            play()
                    time.sleep(0.2)

                time.sleep(1.5)





