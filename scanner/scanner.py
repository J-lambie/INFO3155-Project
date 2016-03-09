import socket

ip = socket.gethostbyname(raw_input("Enter target host IP: "))
print "Scanning", ip
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

def scanPort(ip, port):
    res = s.connect_ex((ip, port))
    if(res == 0):
        return True
    else:
        return False

for port in range(0,2000):
    value = scanPort(ip, port)
    if value == False:
        print("Secure: " + str(port))
    else:
        print("I can get in!: " + str(port))
        break
#raw_input()
s.close()

