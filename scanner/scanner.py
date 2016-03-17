import socket
import os
import sys
import optparse
from datetime import datetime



def listScan(host, port):
    ip = socket.gethostbyname(host)

    try:
        socket.setdefaulttimeout(20)
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        res = s.connect_ex((ip, port))
        if (res == 0):
            print("[+]Connection to " + host + " port " + str(port) + " successful!")
            if port == 80:
                s.connect_ex((ip,port))
                banner = s.recv(1024)
                print('[+]'+ ip + ': ' + '\n' + banner.decode(encoding='UTF-8'))
            else:
                s.connect_ex((ip,port))
                banner = s.recv(1024)
                print('[+]'+ ip + ': ' + '\n' + banner.decode(encoding='UTF-8'))
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
    f = open(filename,'r')
    for line in f.readlines():
        if line.strip('\n') in banner:
            print('[+] Server is vulnerable: ' + banner.strip('\n'))



def main (filename, hosts, ports):
   
    #used for parsing filename hosts and ports               
#    parser = optparse.OptionParser('%prog -f vul_banners.txt -t <host(s)> -p <port(s)>')
#    parser.add_option('-f', dest='filename', type='string', help='Specify the file. vul_banners.txt ')
#    parser.add_option('-t', dest='hosts', type='string', help='Specify the host(s). Separate by commas')
#    parser.add_option('-p', dest='ports', type='string', help='Specify the port(s). Separate by commas')
                   
#    (options, args) = parser.parse_args()

    #if no hosts or ports are found, error message is shown
#    if(options.hosts == None) | (options.ports == None) | (options.filename == None):
#        print(parser.usage)
#        exit(0)

#    filename = str(options.filename)                                  
#    hosts = str(options.hosts).split(',')
#    ports = str(options.ports).split(',')

    print('-'*60)
    print ("Please wait. Scanning ")
    print('-'*60)

    time1 = datetime.now()

    for host in hosts:
        for port in ports:
            listScan(host, int(port))
            print ('')
        time2 = datetime.now()
        print("Scanning Completed in: ", (time2-time1))

#if __name__ == '__main__':
#    main()
    



    


    

