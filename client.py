import socket 
client = socket.socket()
host="localhost" 
port=9000 # bağlanacağımız kapı
client.connect((host,port)) # bağlantı yapılıyor
print("Bağlantı yapıldı")
client.send("Nude at xd") # mesaj gönderiyoruz
mesaj=client.recv(1024) # geri gelen mesajı okuyoruz
print(mesaj)
client.close() # bağlantıyı  kapatıyoruz
