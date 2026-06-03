from socket import *

server = socket(AF_INET, SOCK_STREAM)
server.bind(("localhost", 5003))
server.listen(5)

print("Server2 radi")

while True:
    client, addr = server.accept()

    fajl = open("S2/data.txt", "r")
    podaci = fajl.read()
    fajl.close()

    client.send(podaci.encode())
    client.close()