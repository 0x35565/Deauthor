 ![image](https://github.com/coolpancakes/Deauthor/assets/73265375/3ac4e02c-d87c-4955-90e1-8388895c976e)








# Deauthor
With this simple and effective tool you can easily remove ANY wireless device to your network in an instant without any administrative rights to your routers interface. Please read below for more information.  

# Setup and usage 
pip3 install -r requirements.txt
python deauthor.py
use numbers to navigate the menu. 

# Please NOTE: 

1. The tool requires administrative privileges in order to access layer 3 to send and receive packets on your network. 
2. This only works on devices that are wirelessly connected to your network. 

# The innerworkings of the tool (for nerds)
Deauthor uses the Layer 2 ARP protocol alongside that, the Dot11 protocol. Address Resolution Protocol is used to discover the hosts on your network. After all hosts have been scanned by simply selecting the number associated with "Scan Network" the programs output is as follows: 

IP Address: 172.20.10.1 MAC Address: f6:0e:01:21:d0:64
IP Address: exampleip MAC Address: ff:ff:ff:ff:ff:ff 
IP Address: exampleip MAC Address: ff:ff:ff:ff:ff:ff

It gives you the IP and MAC Address of every node connected to your LAN. And when entered and Deauthing has commenced the Target node will be disonnected from the network within a matter of seconds, **Please NOTE** that this only works on devices that are WIRELESSLY connected to your LAN. 

Now, how does Deauthing actually work? So using scapy which is a packet manipulation module the frame looks similar to this: RadioTap()/Ether()/Dot11(subtype=1100)

**Breaking the packet down.**

RadioTap() to add addional essential information to the frame, without radiotap the frame does not send properly over the wire and results in a malformed packet.. 
Ether() to automatically retrieve the source mac address of the interface we're sending from because we're super lazy. NOTE: Ether is not essential for this to work, it's convenience.
Dot11() This part of the packet is the Dot11 protocol itself, the subtype argument sets it to the subtype 1100 which is Deauthentication. It's a management frame used by the router on end devices that are in the process of disconnecting themselves from the network. 

If you want a more in depth explanation of the Dot11 protocol, i encourage you to visit: https://en.wikipedia.org/wiki/802.11_frame_types which gives you a full list of the available subtypes and lots of other juicy information. 

# What operating systems does Deauthor run on? 

POSIX, Windows


