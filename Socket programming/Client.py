import socket
import time 


targetIP="127.0.0.1"
targetPort=9999

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #   ip v4 using ,udp
    
    print("Socket object s got created..")
    
    #binding my ip and port
except:
    print("please check your socket..")
    
while 3>2:
    msg=input("enter your message : ")
    new_msg=msg.encode('ascii')
    s.sendto(new_msg,(targetIP,targetPort))
    print("data send ...")
    print("waiting for responce : ")
    time.sleep(1)
    print(s.recvfrom(100))
    