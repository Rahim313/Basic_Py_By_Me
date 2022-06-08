import socket
import time 


myIP="127.0.0.1"
myPort=9999

try:
    s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #   ip v4 using ,udp
    
    print("Socket object s got created..")
    
    #binding my ip and port
    
    s.bind((myIP,myPort))
    print("ASocket got binded..")
    
except:
    print("Please check your socket")
    
    
    
    
# to recive data

while 4>2:
    data=s.recvfrom(100)
    time.sleep(2)
    print(data)
    # giving reply
    reply=input("enter your responce : ")
    reply_new=reply.encode("ascii")
    s.sendto(reply_new,data[1])
    print("____________________________")
s.close()
    