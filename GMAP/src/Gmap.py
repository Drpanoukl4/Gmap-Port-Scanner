import socket
import sys
import pyfiglet
import cowsay
import signal
from rich.console import Console
from rich import print
from datetime import datetime

#xD贾奎

undep = "tcp"

def sig_handler(sig, frame):
    print("\n\n[green][+][/green] [red]Exiting Gmap[/red], [blue]Thank you for use...[blue]\n")
    sys.exit(0)


signal.signal(signal.SIGINT, sig_handler)

gmap_banner = pyfiglet.figlet_format("Gmap Port Scanner")
print(gmap_banner)
cowsay.cow("By: Gabriel Perez")

print("-*-" * 25)
print("\nPlease Ip: ")

host = input("\n\n-*-* [!] Enter target [!] -*-*: " )


print("-*-" * 25)
print("\n")
print("Scanning target: ", host)
print("Starting Gmap 9.92 ( https://Gmap.org ) at: " + str(datetime.now()))
print("\n")
print("-*-" * 25)

try:
    for port in range(1, 65535): #All ports Can edit
    
        scket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)#IPV4 AND TCP protocols...
        socket.setdefaulttimeout(1)

        result = scket.connect_ex((host, port))

        if result == 0:
            try:

                res = socket.getservbyport(port, undep)

                print("host {}: Port {} is open, Service: {}".format(host, port, res))

            except socket.error:

                 print("host {}: Port {} is open, Service: Not Found".format(host, port))

            
        scket.close()
        
except KeyboardInterrupt:
    print("\n[!] Exiting Gmap")
    sys.exit()
except socket.gaierror:
    print("\n[!]Can't resolved Hostname")
    sys.exit()




#Gmap parody to Nmap