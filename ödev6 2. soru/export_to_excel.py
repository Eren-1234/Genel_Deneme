import sqlite3
import pandas as pd

# Veritabanına bağlanma
conn = sqlite3.connect("personel_veritabani.db")

# SQL sorgusuyla Personel tablosundaki tüm verileri çekme
df = pd.read_sql_query("SELECT * FROM Personel", conn)

# Verileri bir Excel dosyasına yazma
df.to_excel("Personel_Tablosu.xlsx", index=False)

# Bağlantıyı kapatma
conn.close()

print("Veritabanı tablosu Excel dosyasına aktarıldı.")
