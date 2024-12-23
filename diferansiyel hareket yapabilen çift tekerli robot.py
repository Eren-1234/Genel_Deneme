import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Robot parametreleri
rR = 0.05  # Tekerlek çapı (m)
L = 0.3  # Taban uzunluğu (m)
delta_t = 0.2  # Zaman adımı (s)

# Başlangıç durumu [x, y, theta]
x = 0
y = 0
theta = np.pi / 6  # Radyan cinsinden

# Zaman aralıkları ve hızlar
time_intervals = [(0, 10, 1, 1), (10, 15, 2, 1), (15, 20, 1, -1), (20, 25, 0, 1)]
total_time = 25  # Simülasyon süresi (saniye)

# Robotun pozisyonlarını tutacak listeler
x_positions = [x]
y_positions = [y]
thetas = [theta]

# Simülasyon değişkeni
time = 0

# Grafik oluşturma
fig, ax = plt.subplots(figsize=(10, 10))
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_xlabel("X Position (m)")
ax.set_ylabel("Y Position (m)")
ax.set_title("Robot Konum Grafiği")

# Süre sayacı metni
time_text = ax.text(0.02, 0.95, '', transform=ax.transAxes)

# Robotun pozisyonu ve yönü için çizim elemanları
yön, = ax.plot([], [], 'b-', label="Yön")
robot_imlec = ax.arrow(x, y, 0.1*np.cos(theta), 0.1*np.sin(theta), head_width=0.05)

# Trajektori güncelleme fonksiyonu
def update(frame):
    global x, y, theta, time

    # Zaman aralığına göre vr ve vl değerlerini belirle
    for start_time, end_time, vr, vl in time_intervals:
        if start_time <= time < end_time:
            break
    
    # Ortak hız ve açısal hız hesaplamaları
    w = (vr - vl) / L  # Açısal hız
    
    if vr != vl:
        r = (L / 2) * ((vr + vl) / (vr - vl))
        ICCx = x - r * np.sin(theta)
        ICCy = y + r * np.cos(theta)
        
        
        A1 = np.array([[np.cos(w * delta_t), -np.sin(w * delta_t), 0],
                       [np.sin(w * delta_t),  np.cos(w * delta_t), 0],
                       [0, 0, 1]])
        
        A2 = np.array([[x - ICCx], [y - ICCy], [theta]])
        A3 = np.array([[ICCx], [ICCy], [w * delta_t]])
        
        
        sonuc_matrisi = np.matmul(A1, A2) + A3
        x = sonuc_matrisi[0][0]
        y = sonuc_matrisi[1][0]
        theta = sonuc_matrisi[2][0]
    else:
        # Eğer vr == vl ise düz bir yol boyunca ilerler
        v = vr  # v = vr = vl (çizgisel hız)
        x += v * np.cos(theta) * delta_t
        y += v * np.sin(theta) * delta_t

    # Pozisyonları kaydet
    x_positions.append(x)
    y_positions.append(y)
    thetas.append(theta)
    
    # Grafiği güncelle
    yön.set_data(x_positions, y_positions)
    
    # Robotun yönünü gösteren oku güncelle
    ax.patches.clear()  # Eski oku sil
    ax.arrow(x, y, 0.1*np.cos(theta), 0.1*np.sin(theta), head_width=0.05, color='r')
    
    # Zamanı güncelle
    time_text.set_text(f"Time: {time:.1f} s")
    time += delta_t
    
    return yön, robot_imlec, time_text

# Animasyonu başlatma
ani = FuncAnimation(fig, update, frames=int(total_time/delta_t), interval=100, blit=False, repeat=False)

# Grafiği göster
plt.legend()
plt.grid(True)
plt.axis('equal')
plt.show()
