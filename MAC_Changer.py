CEZARY SAWICKI  
import subprocess
import optparse
import re

def get_args(): # gets arguments from user and handles missing options.
    parser = optparse.OptionParser() # calls parser object

    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC address") #adds option to parser
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    (options, arguments) = parser.parse_args() #gets options and arguments from parser
    
    if not options.interface:
        parser.error("[-]Please input correct interface name, use --help for more info")
    elif not options.new_mac:
        parser.error("[-]Please input correct MAC address, use --help for more info")
    return options

def change_mac(interface, new_mac): # changes mac address for specified interface
    print("[+] Changing MAC address for " + interface + " to " + new_mac)

    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])

def get_current_mac (interface): # gets current mac address for specified interface
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        print(mac_address_search_result.group(0))
    else:
        print("Couldn't find any MAC address")

options = get_args()
change_mac(options.interface,options.new_mac)
current_mac=get_current_mac(options.interface)
if current_mac == options.new_mac:
    print("[+] MAC address was successfully changed to " + current_mac)
else:
    print("[-] MAC address did not get changed")
