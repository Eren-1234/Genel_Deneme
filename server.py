import socket as sc

host ="localhost"
port = 23456

server = sc.socket(sc.AF_INET, sc.SOCK_STREAM)
server.bind((host, port))
server.listen(1)

print("Bağlantı bekleniyor...")

makine,bilgi=server.accept()
print("Bir bağlantı kabul edildi")
mesaj=makine.recv(1024)
print(mesaj)
makine.send("Mesajınız alınmıştır!")
server.close()