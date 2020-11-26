import subprocess
import os
import time
from termcolor import colored
import winsound
import smtplib

def play():
    winsound.PlaySound("alarm", winsound.SND_ASYNC | winsound.SND_ALIAS )
os.system('color')

def sendMail(name):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    password = ""
    server.login('euanmorgan48@gmail.com', password)

    subject = "ALERT!! ALERT!!!!"

    body = f"{name} is outside!!!"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "euanmorgan48@gmail.com",
        msg
    )
    print("Sent email")

    server.quit()


a = input("Mam, dad or both?")

if a.lower() == "mam":
    ips = {"mam":"192.168.1.42"}
elif a.lower() == "dad":
    ips = {"dad":"192.168.1.10"}
else:
    ips = {"mam":"192.168.1.42","dad":"192.168.1.10"}
    
x = True

with open(os.devnull, "wb") as limbo:

            while x:
                os.system('cls')
                for (name,ip) in ips.items():
                    
                
                    result=subprocess.Popen(["ping", "-n", "1", "-w", "200", ip],
                            stdout=limbo, stderr=limbo,shell=True).wait()

                    
                    print("Pinging {}".format(name))
                    if result:
                            print(ip, colored('inactive', 'red'))
                            
                            
                    else:
                            
                            print(ip, colored('active', 'green'))
                            play()
                            sendMail(name)
                            time.sleep(4)
                            x = False
                            break
                    time.sleep(0.2)

                time.sleep(1.5)





