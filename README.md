# Deauthor
Deauthor, this tool can remove any wireless device on your local area network with ease, if you came seeking a tool that will give you more power over your network without any administrative rights to your routers interface then this is the tool for you. 

**Requirements**
to use this tool you require scapy to be installed, to install scapy run the following within the cloned directory. pip3 install -r requirements.txt and that will install scapy for you. 

**How does it work?**
Deauthor uses the Layer 2 ARP protocol alongside that Dot11 Deauthentication frames but more on that later. Address Resolution Protocol is used to discover the hosts on your network. After all hosts have been scanned by simply selecting "Scan Network" via typing 1 and clicking enter within the Deauthor tool devices will be displayed as follows in the programs output: 

IP Address: 172.20.10.1 MAC Address: f6:0e:01:21:d0:64

It gives you the IP and MAC Address of EACH node on the network. And when entered and Deauthing has commenced the Target node will be disonnected from the network within a matter of seconds. NOTE: This only works on wireless devices as mentioned at the beginning. 

**Is this tool powerful?**
This tool is powerful, simple and easy to navigate. 

**What operating systems have support?**
Look, at the current time of writing this only Linux. Windows support can easily be added 

**Basic Usage**
Here I've compiled an overly simplified set of procedures to use the tool with a summarised explanation and dot points. 

To list all devices on the network simply type 1 and select your enter key to get a list of devices that are on your LAN. Followed by that you're going to want to find the private IP of the wireless device you want removed then you're going to copy the MAC address of the device asociated with that IP listed on your screen then you'll be prompted to re-run a scan, input n and click enter, this will take you back to the home screen. When you're back into the main menu select 2, input the MAC address you have in your clipboard and launch the attack. by inputing 2 and clicking enter to start the attack and click y

1. List all devices by clicking 1, copy mac address associated with IP you want kicked off the network
2. type n on your keyboard to decline and go back to menu
3. type 2 on your keyboard to select Deauth Attack
4. type 1 on your keyboard to enter mac address (paste copied mac address in clipboard)
5. type 2 to start the Deauth Attack!

**Summary**
Yeah this is my first big tool apart from the port scanner, the difference is i made this by myself with no help and I feel really acomplished to deliver such a product to the world and I hope everyone enjoys it. Any feedback on the code would be greatly appreciated. 


