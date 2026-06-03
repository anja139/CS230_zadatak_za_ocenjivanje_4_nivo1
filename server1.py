#1. Napisati dva servera. Server1 čuva data.txt i na svakih 30 sekundi proverava da li se
# datoteka na Server2 razlikuje. Ako se razlikuje, Server1 napravi kopiju data.txt sa novim imenom
# data_backup_TIMESTAMP.txt u svom folderu S1. Server2 samo šalje svoju verziju fajla na zahtev.

from socket import *
import time
import os
import shutil

def procitaj_lokalni_fajl():
    fajl = open("S1/data.txt", "r")
    podaci = fajl.read()
    fajl.close()
    return podaci

def uzmi_fajl_sa_servera2():
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(("localhost", 5003))

    podaci = client.recv(4096).decode()

    client.close()
    return podaci

os.makedirs("S1", exist_ok=True)
os.makedirs("S2", exist_ok=True)

print("Server1 radi")

while True:
    lokalni_fajl = procitaj_lokalni_fajl()
    server2_fajl = uzmi_fajl_sa_servera2()

    if lokalni_fajl != server2_fajl:
        timestamp = str(int(time.time()))
        novo_ime = "S1/data_backup_" + timestamp + ".txt"
        shutil.copy("S1/data.txt", novo_ime)
        print("Napravljena kopija:", novo_ime)
    else:
        print("Fajlovi su isti.")

    time.sleep(30)