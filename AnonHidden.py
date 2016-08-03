#!/usr/bin/python
# -*- coding: utf-8 -*-
# Developed in Python3
"""
+-------------------------------------------------------+
| Create BY: Julian Pedro F. Braga                      |
|                                                       |
| [*] AUTOR:        Julian Pedro F. Braga               |
| [*] GITHUB:       https://github.com/JulianPedro      |
+-------------------------------------------------------+
"""
#Imports
import os
import os.path
import time
import requests
import sys
import subprocess
import random
#/Imports

#Colors
PURPLE = '\033[95m'
CYAN = '\033[96m'
DARKCYAN = '\033[36m'
BLUE = '\033[94m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
BOLD = '\033[1m'
UNDERLINE = '\033[4m'
END = '\033[0m'
RESET='\033[1;00m'
#/Colors

#Banner
color = random.randrange(1,5)
if color == 1:
   colorr = PURPLE
elif color == 2:
   colorr = CYAN
elif color == 3:
   colorr = BLUE
elif color == 4:
   colorr = GREEN

banner = ""+colorr+"""
 @@@@@@   @@@  @@@   @@@@@@   @@@  @@@  @@@  @@@  @@@  @@@@@@@   @@@@@@@   @@@@@@@@  @@@  @@@
@@@@@@@@  @@@@ @@@  @@@@@@@@  @@@@ @@@  @@@  @@@  @@@  @@@@@@@@  @@@@@@@@  @@@@@@@@  @@@@ @@@
@@!  @@@  @@!@!@@@  @@!  @@@  @@!@!@@@  @@!  @@@  @@!  @@!  @@@  @@!  @@@  @@!       @@!@!@@@
!@!  @!@  !@!!@!@!  !@!  @!@  !@!!@!@!  !@!  @!@  !@!  !@!  @!@  !@!  @!@  !@!       !@!!@!@!
@!@!@!@!  @!@ !!@!  @!@  !@!  @!@ !!@!  @!@!@!@!  !!@  @!@  !@!  @!@  !@!  @!!!:!    @!@ !!@!
!!!@!!!!  !@!  !!!  !@!  !!!  !@!  !!!  !!!@!!!!  !!!  !@!  !!!  !@!  !!!  !!!!!:    !@!  !!!
!!:  !!!  !!:  !!!  !!:  !!!  !!:  !!!  !!:  !!!  !!:  !!:  !!!  !!:  !!!  !!:       !!:  !!!
:!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  !:!  :!:  :!:  !:!  :!:  !:!  :!:       :!:  !:!
::   :::   ::   ::  ::::: ::   ::   ::  ::   :::   ::   :::: ::   :::: ::   :: ::::   ::   ::
 :   : :  ::    :    : :  :   ::    :    :   : :  :    :: :  :   :: :  :   : :: ::   ::    :

Redirect All Traffic From The Machine To The Tor Network
\033[0m"""
os.system("clear")
print(banner)
#/Banner

#ProgBody
def install():
   syst = subprocess.getstatusoutput("cat /etc/*release | grep 'ID' | cut -d '=' -f 2 | head -1")
   if syst[1] == ("Ubuntu" or "ubuntu" or "Debian" or "debian" or "Parrot" or "Kali" or "kali"):
      os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Install...")
      time.sleep(2)
      os.system("sudo apt-get install tor")
      os.system("sudo mkdir -p /etc/tor")
      os.system("sudo mv torrc /etc/tor/torrc")
      os.system("sudo chmod 777 /etc/tor/torrc")
      os.system("sudo echo 'nameserver 127.0.0.1' > /etc/resolv.conf")
      os.system("sudo tor")
      time.sleep(15)
      print("+--------------------------+")
      print("|" + GREEN + "     Install Tor Sucess   " + RESET + "|" + RESET + "")
      print("+--------------------------+")
   elif syst[1] == ("Arch" or "arch"):
      os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Install...")
      time.sleep(2)
      os.system("sudo pacman -S tor")
      os.system("sudo mkdir -p /etc/tor")
      os.system("sudo mv torrc /etc/tor/torrc")
      os.system("sudo chmod 777 /etc/tor/torrc")
      os.system("sudo echo 'nameserver 127.0.0.1' > /etc/resolv.conf")
      os.system("sudo tor")
      time.sleep(15)
      print("+--------------------------+")
      print("|" + GREEN + "     Install Tor Sucess   " + RESET + "|" + RESET + "")
      print("+--------------------------+")
   elif syst[1] == ("Fedora" or "fedora"):
      os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Install...")
      time.sleep(2)
      os.system ("sudo dnf install tor")
      os.system("sudo mkdir -p /etc/tor")
      os.system("sudo mv torrc /etc/tor/torrc")
      os.system("sudo chmod 777 /etc/tor/torrc")
      os.system("sudo echo 'nameserver 127.0.0.1' > /etc/resolv.conf")
      os.system("sudo tor")
      time.sleep(15)
      print("+--------------------------+")
      print("|" + GREEN + "     Install Tor Sucess   " + RESET + "|" + RESET + "")
      print("+--------------------------+")
   else:
      os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Install...")
      time.sleep(2)
      os.system("sudo apt-get install tor")
      os.system("sudo mkdir -p /etc/tor")
      os.system("sudo mv torrc /etc/tor/torrc")
      os.system("sudo chmod 777 /etc/tor/torrc")
      os.system("sudo echo 'nameserver 127.0.0.1' > /etc/resolv.conf")
      os.system("sudo tor")
      time.sleep(15)
      print("+--------------------------+")
      print("|" + GREEN + "     Install Tor Sucess   " + RESET + "|" + RESET + "")
      print("+--------------------------+")

def check():
   os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden 'Check IP'")
   try:
      os.system("firefox https://check.torproject.org/?lang=pt_BR &")
   except:
      os.system("iceweasel https://check.torproject.org/?lang=pt_BR &")
   r = requests.get('http://icanhazip.com/')
   time.sleep(2)
   print(""+colorr+"You IP Public is :"+ r.content.decode('ascii')+RESET)

def start():
   os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Starting...")
   non_tor = "192.168.1.0/24 192.168.0.0/24"
   tor = ("127.0.0.0/9" , "127.128.0.0/10")
   tor2 = ("127.0.0.0/8")
   torid= "109"
   transport = "9040"
   os.system("sudo iptables -F ")
   os.system("sudo iptables -t nat -F ")
   os.system("sudo iptables -t nat -A OUTPUT -m owner --uid-owner "+torid+" -j RETURN")
   os.system("sudo iptables -t nat -A OUTPUT -p udp --dport 53 -j REDIRECT --to-ports 53 ")
   for net in tor:
      os.system("sudo iptables -t nat -A OUTPUT -d "+net+" -j RETURN")
   os.system("sudo iptables -t nat -A OUTPUT -p tcp --syn -j REDIRECT --to-ports "+transport+"")
   os.system("sudo iptables -A OUTPUT -m state --state ESTABLISHED,RELATED -j ACCEPT")
   os.system("sudo iptables -A OUTPUT -d "+tor2+" -j ACCEPT")
   os.system("sudo iptables -A OUTPUT -m owner --uid-owner "+torid+" -j ACCEPT")
   os.system("sudo iptables -A OUTPUT -j REJECT")
   print(""+colorr+"Starting TOR..."+RESET+"")
   time.sleep(8)
   r = requests.get('http://icanhazip.com/')
   print("" + colorr + "You IP Public is :" + r.content.decode('ascii') + RESET)

def stop():
   os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Stop...")
   os.system ("sudo iptables -t nat -F OUTPUT")
   os.system ("sudo iptables -t filter -F OUTPUT")
   print(""+BOLD+""+RED+"Stop TOR..."+RESET+"")
   time.sleep(8)
   r = requests.get('http://icanhazip.com/')
   print("" + colorr + "You IP Public is :" + r.content.decode('ascii') + RESET)
   print(""+BOLD,colorr+"Thank You...Goodbye :)"+RESET+"")

if sys.argv[1:] == []:
    print("")
    print(""+colorr+"Usage: sudo python3 AnonHidden.py [OPTIONS]")
    print(""+colorr+"""
    --install       Install Tor And Conf
    --start         Start AnonHidden
    --check         Check IP
    --stop          Stop AnonHidden
        \033[0m""")
else:
   if sys.argv[1] == "--install":
      install()
   if sys.argv[1] == "--start":
      start()
   if sys.argv[1] == "--check":
      check()
   if sys.argv[1] == "--stop":
      stop()
   else:
      pass
#/ProgBody