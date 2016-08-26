#!/usr/bin/python
# -*- coding: utf-8 -*-
# Developed in Python2
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
import urllib
from json import load
from urllib2 import urlopen
import requests
import sys
import commands
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
   colorr = RED
elif color == 2:
   colorr = CYAN
elif color == 3:
   colorr = BLUE
elif color == 4:
   colorr = GREEN

banner = ""+colorr+"""
 █████╗ ███╗   ██╗ ██████╗ ███╗   ██╗██╗  ██╗██╗██████╗ ██████╗ ███████╗███╗   ██╗
██╔══██╗████╗  ██║██╔═══██╗████╗  ██║██║  ██║██║██╔══██╗██╔══██╗██╔════╝████╗  ██║
███████║██╔██╗ ██║██║   ██║██╔██╗ ██║███████║██║██║  ██║██║  ██║█████╗  ██╔██╗ ██║
██╔══██║██║╚██╗██║██║   ██║██║╚██╗██║██╔══██║██║██║  ██║██║  ██║██╔══╝  ██║╚██╗██║
██║  ██║██║ ╚████║╚██████╔╝██║ ╚████║██║  ██║██║██████╔╝██████╔╝███████╗██║ ╚████║
╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝ ╚═╝  ╚═══╝╚═╝  ╚═╝╚═╝╚═════╝ ╚═════╝ ╚══════╝╚═╝  ╚═══╝

Redirect All Traffic From The Machine To The Tor Network
\033[0m"""
os.system("clear")
print(banner)

#/Banner


#ProgBody
def install():
   syst = commands.getstatusoutput("cat /etc/*release | grep 'ID' | cut -d '=' -f 2 | head -1")
   if syst[1] == ("Ubuntu" or "ubuntu" or "Debian" or "debian" or "Parrot" or "Kali" or "kali"):
      os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Install...")
      time.sleep(2)
      os.system("sudo pip install requests")
      os.system("sudo apt-get install tor")
      time.sleep(2)
      print""+colorr+"==> Creating Directory Tor"+RESET+""
      os.system("sudo mkdir -p /etc/tor")
      time.sleep(1.5)
      print""+colorr+"==> Moving Torrc"+RESET+""
      os.system("sudo mv torrc /etc/tor/torrc")
      time.sleep(1.5)
      print""+colorr+"==> Setting Up Permissions"+RESET+""
      os.system("sudo chmod 777 /etc/tor/torrc")
      time.sleep(1.5)
      print""+colorr+"==> Setting NameServer"+RESET+""
      os.system("sudo echo 'nameserver 127.0.0.1' > /etc/resolv.conf")
      ter = ['xterm']
      ter.extend(['-e', 'bash', '-c', 'sudo tor; exec $SHELL' ])
      subprocess.Popen(ter, stdout=subprocess.PIPE)
      time.sleep(1.5)
      print  ""+ colorr + "==> Wait Tor Install\n" + RESET +""
   elif syst[1] == ("Arch" or "arch"):
      os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Install...")
      time.sleep(2)
      os.system("sudo pacman -S python-requests")
      os.system("sudo pacman -S tor")
      time.sleep(2)
      print""+colorr+"==> Creating Directory Tor"+RESET+""
      os.system("sudo mkdir -p /etc/tor")
      time.sleep(1.5)
      print""+colorr+"==> Moving Torrc"+RESET+""
      os.system("sudo mv torrc /etc/tor/torrc")
      time.sleep(1.5)
      print""+colorr+"==> Setting Up Permissions"+RESET+""
      os.system("sudo chmod 777 /etc/tor/torrc")
      time.sleep(1.5)
      print""+colorr+"==> Setting NameServer"+RESET+""
      os.system("sudo echo 'nameserver 127.0.0.1' > /etc/resolv.conf")
      ter = ['xterm']
      ter.extend(['-e', 'bash', '-c', 'sudo tor; exec $SHELL' ])
      subprocess.Popen(ter, stdout=subprocess.PIPE)
      time.sleep(1.5)
      print  ""+ colorr + "==> Wait Tor Install\n" + RESET +""
   elif syst[1] == ("Fedora" or "fedora"):
      os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Install...")
      time.sleep(2)
      os.system("sudo dnf install requests")
      os.system("sudo dnf install tor")
      time.sleep(2)
      print""+colorr+"==> Creating Directory Tor"+RESET+""
      os.system("sudo mkdir -p /etc/tor")
      time.sleep(1.5)
      print""+colorr+"==> Moving Torrc"+RESET+""
      os.system("sudo mv torrc /etc/tor/torrc")
      time.sleep(1.5)
      print""+colorr+"==> Setting Up Permissions"+RESET+""
      os.system("sudo chmod 777 /etc/tor/torrc")
      time.sleep(1.5)
      print""+colorr+"==> Setting NameServer"+RESET+""
      os.system("sudo echo 'nameserver 127.0.0.1' > /etc/resolv.conf")
      ter = ['xterm']
      ter.extend(['-e', 'bash', '-c', 'sudo tor; exec $SHELL' ])
      subprocess.Popen(ter, stdout=subprocess.PIPE)
      time.sleep(1.5)
      print  ""+ colorr + "==> Wait Tor Install\n" + RESET +""
   else:
      os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Install...")
      time.sleep(2)
      os.system("sudo pip install requests")
      os.system("sudo apt-get install tor")
      time.sleep(2)
      print""+colorr+"==> Creating Directory Tor"+RESET+""
      os.system("sudo mkdir -p /etc/tor")
      time.sleep(1.5)
      print""+colorr+"==> Moving Torrc"+RESET+""
      os.system("sudo mv torrc /etc/tor/torrc")
      time.sleep(1.5)
      print""+colorr+"==> Setting Up Permissions"+RESET+""
      os.system("sudo chmod 777 /etc/tor/torrc")
      time.sleep(1.5)
      print""+colorr+"==> Setting NameServer"+RESET+""
      os.system("sudo echo 'nameserver 127.0.0.1' > /etc/resolv.conf")
      ter = ['xterm']
      ter.extend(['-e', 'bash', '-c', 'sudo tor; exec $SHELL' ])
      subprocess.Popen(ter, stdout=subprocess.PIPE)
      time.sleep(1.5)
      print  ""+ colorr + "==> Wait Tor Install\n" + RESET +""

def check():
    os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden 'Check IP'")
    print""+colorr+"==> Check IP"+RESET+"\n"
    ip = load(urlopen('https://api.ipify.org/?format=json'))['ip']
    tor = urllib.urlopen('https://check.torproject.org/exit-addresses')
    for ip_tor in tor.readlines():
        ip_tor = ip_tor.replace("\n","")
        if "ExitAddress" in ip_tor:
            ip_tor = ip_tor.split(" ")[1]
            if ip == ip_tor:
                success = 1
                break
            else:
                success = 0
    if success == 1:
        print "\033[92m==> Success IP:" + ip + " |OK|\033[1;00m \n"
    else:
        print "\033[91m==> Failure IP:" + ip + " |Fail|\033[1;00m \n"


def start():
   os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Starting...")
   time.sleep(5)
   print  ""+ colorr + "==> Killing Applications" + RESET +""
   os.system("sudo killall -q chrome dropbox iceweasel skype icedove thbird firefox chromium xchat transmission")
   print  ""+ colorr + "==> Killing Cache" + RESET +""
   os.system("sudo bleachbit -c adobe_reader.cache chromium.cache chromium.current_session chromium.history elinks.history emesene.cache epiphany.cache firefox.url_history flash.cache flash.cookies google_chrome.cache google_chrome.history  links2.history opera.cache opera.search_history opera.url_history &> /dev/null")
   non_tor = "192.168.1.0/24 192.168.0.0/24"
   tor = "127.0.0.0/9" , "127.128.0.0/10"
   tor2 = "127.0.0.0/8"
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
   print""+colorr+"==> Starting TOR"+RESET+""
   time.sleep(8)
   check()

def stop():
   os.system("/usr/bin/notify-send -i " + os.getcwd() + "/hidden.png AnonHidden Stop...")
   os.system ("sudo iptables -t nat -F OUTPUT")
   os.system ("sudo iptables -t filter -F OUTPUT")
   print(""+BOLD+""+RED+"==> Stop TOR"+RESET+"")
   time.sleep(8)
   check()
   print""+colorr+"==> Thank You...Goodbye :)\n"+RESET+""

def about():
    time.sleep(1)
    print""+colorr+"==> AnonHidden Redirect all traffic from the machine to the Tor network."+RESET+""
    time.sleep(1)
    print""+colorr+"==> Version: 3.0.0"+RESET+""
    time.sleep(1)
    print""+colorr+"==> Create By: Julian Pedro F. Braga"+RESET+""
    time.sleep(1)
    print""+colorr+"==> Github: Github.com/JulianPedro"+RESET+""
    time.sleep(1)
    print""+colorr+"==> Thank You :)\n"+RESET+""

if sys.argv[1:] == []:
    print("")
    print(""+colorr+"Usage: sudo python3 AnonHidden.py [OPTIONS]")
    print(""+colorr+"""
    --install       Install Tor And Conf
    --start         Start AnonHidden
    --check         Check IP
    --stop          Stop AnonHidden
    --about         About AnonHidden
        \033[0m""")
else:
    if sys.argv[1] == "--install":
        install()
    elif sys.argv[1] == "--start":
        start()
    elif sys.argv[1] == "--check":
        check()
    elif sys.argv[1] == "--stop":
        stop()
    elif sys.argv[1] == "--about":
        about()
    else:
        print""+colorr+"==> Enter A Valid Argument!"+RESET+"\n"
#/ProgBody
