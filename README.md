![image](https://github.com/coolpancakes/Deauthor/assets/73265375/3ac4e02c-d87c-4955-90e1-8388895c976e)








# Deauthor
This tool can remove any wireless device on your local area network with ease, if you came seeking a tool that will give you more power over your network without any administrative rights to your routers interface then this is the tool for you. 

# Setup and usage 
pip3 install -r requirements.txt
python deauthor.py
use numbers to navigate the menu. 

# Please NOTE: 
1. This tool requires administrative privileges in order to access layer 3 to send and receive packets on your network. 
2. This only works on devices that are wirelessly connected to your network. 

# How does it work (for nerds)
Deauthor uses the Layer 2 ARP protocol alongside that, the Dot11 protocol. Address Resolution Protocol is used to discover the hosts on your network. After all hosts have been scanned by simply selecting the number associated with the string "Scan Network" the programs output is as follows: 

IP Address: 172.20.10.1 MAC Address: f6:0e:01:21:d0:64
IP Address: exampleip MAC Address: ff:ff:ff:ff:ff:ff 
IP Address: exampleip MAC Address: ff:ff:ff:ff:ff:ff

It gives you the IP and MAC Address of every node connected to your LAN. And when entered and Deauthing has commenced the Target node will be disonnected from the network within a matter of seconds, **Please NOTE** that this only works on devices that are WIRELESSLY connected to your LAN. 

# What operating systems does Deauthor run on? 

POSIX, Windows you name it, we support it.  


