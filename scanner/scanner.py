import socket
import os
import sys
import optparse
from datetime import datetime

###main([host], [ports])

def listScan(host, port):
    ip = socket.gethostbyname(host)

    try:
        socket.setdefaulttimeout(20)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = s.connect_ex((ip, port))
        if (res ==   0):
            print("[+]Connection to " + host + " port " + str(port) + " successful!")
            s.send('GET HTTP/1.1 200 OK \r\n')
            banner = s.recv(2048).decode(encoding='UTF-8')
            #print('[+]'+ ip + " on port " + str(port) +  ': ' + '\n' + banner.decode(encoding='UTF-8'))
            return banner
        else:
            print("[-]Connection to " + host + " port " + str(port) + " failed")
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
        
   
def vul_Check(banner, filename):
    print banner
    f = open(filename,'r')
    for line in f.readlines():
        if banner in line.strip('\n'):
            print('[+] Host is vulnerable: ' + line)
        

def main ():
   
    #used for parsing filename hosts and ports               
    parser = optparse.OptionParser('%prog -f vul_banners.txt -t <host(s)> -p <port(s)>')
    parser.add_option('-f', dest='filename', type='string', help='Specify the file. vul_banners.txt ')
    parser.add_option('-t', dest='hosts', type='string', help='Specify the host(s). Separate by commas')
    parser.add_option('-p', dest='ports', type='string', help='Specify the port(s). Separate by commas')
                   
    (options, args) = parser.parse_args()

    #if no hosts or ports are found, error message is shown
    if(options.hosts == None) | (options.ports == None) | (options.filename == None):
        print(parser.usage)
        exit(0)

    filename = str(options.filename)                                  
    hosts = str(options.hosts).split(',')
    ports = str(options.ports).split(',')

    print('-'*60)
    print ("Please wait. Scanning ")
    print('-'*60)

    time1 = datetime.now()

    for host in hosts:
        for port in ports:
            banner = listScan(host, int(port))
            if banner != None:
                vul_Check(banner,filename)
            print ('')
        time2 = datetime.now()
        print("Scanning Completed in: ", (time2-time1))

if __name__ == '__main__':
    main()
