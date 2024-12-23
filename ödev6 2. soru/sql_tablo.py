import sqlite3

# Veritabanı bağlantısı oluşturma
conn = sqlite3.connect("personel_veritabani.db")
cursor = conn.cursor()

# 1. Personel tablosunu oluşturma
cursor.execute('''
CREATE TABLE IF NOT EXISTS Personel (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ad TEXT NOT NULL,
    soyad TEXT NOT NULL,
    departman TEXT NOT NULL,
    maas INTEGER NOT NULL
)
''')
conn.commit()
print("Tablo oluşturuldu.")

# 2. Tabloya örnek veriler ekleme
personel_verileri = [
    ('Ahmet', 'Yılmaz', 'Muhasebe', 5000),
    ('Ayşe', 'Kara', 'IT', 7000),
    ('Mehmet', 'Çelik', 'Muhasebe', 5500),
    ('Fatma', 'Demir', 'IT', 8000),
    ('Ali', 'Can', 'Pazarlama', 4500)
]

cursor.executemany("INSERT INTO Personel (ad, soyad, departman, maas) VALUES (?, ?, ?, ?)", personel_verileri)
conn.commit()
print("Örnek veriler eklendi.")

# 3. Ekleme İşlemi
cursor.execute("INSERT INTO Personel (ad, soyad, departman, maas) VALUES (?, ?, ?, ?)", ('Zeynep', 'Güneş', 'Pazarlama', 4800))
conn.commit()
print("Yeni personel eklendi.")

# 4. Silme İşlemi (id = 3 olan personeli sil)
cursor.execute("DELETE FROM Personel WHERE id = ?", (3,))
conn.commit()
print("id=3 olan personel silindi.")

# 5. Güncelleme İşlemi (id = 2 olan personelin maaşını güncelle)
cursor.execute("UPDATE Personel SET maas = ? WHERE id = ?", (7500, 2))
conn.commit()
print("id=2 olan personelin maaşı güncellendi.")

# 6. Gruplama İşlemi (departmanlara göre ortalama maaş)
cursor.execute("SELECT departman, AVG(maas) AS ortalama_maas FROM Personel GROUP BY departman")
grup_verileri = cursor.fetchall()

print("Departmanlara göre ortalama maaşlar:")
for departman, ortalama_maas in grup_verileri:
    print(f"{departman}: {ortalama_maas}")

# 7. Tablodaki Tüm Verileri Görüntüleme
cursor.execute("SELECT * FROM Personel")
tum_veriler = cursor.fetchall()
print("\nTablodaki tüm veriler:")
for veri in tum_veriler:
    print(veri)

# Bağlantıyı kapatma
conn.close()
