import socket
import sys
import os
from datetime import datetime

def scanPorts(server, ports):
    ip = socket.gethostbyname(server)
    print('-'*60)
    print ("Please wait. Scanning ", ip)
    print('-'*60)
    time1 = datetime.now()
    try:
        for port in ports:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            res = s.connect_ex((ip, port))
            if(res == 0):
                print("Port {}: Vulnerable".format(port))
            else:
                print("Port {}: Safe".format(port))
                s.close()
    except KeyboardInterrupt:
        print("\nCtrl+C was pressed")
        sys.exit()
    except socket.error:
        print("\nCould not connect to server")
        sys.exit()
    except socket.gaierror:
        print("\nHost could not be resolved. Exiting....")
        sys.exit()
    time2 = datetime.now()
    print("Scanning Completed in: ", (time2-time1))

