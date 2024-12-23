import matplotlib.pyplot as plt

boy = [170, 150, 180 , 165, 175,190,173.3,140,182,168]
kilo = [65.5, 40, 85.3, 60.2, 90.1,80,55,30,70,59]

sıra_boy = boy.sort()
sıra_kilo = kilo.sort()

plt.xlabel("Boy")
plt.ylabel("Kilo")
plt.title("Boy-Kilo Grafiği")
plt.scatter(boy, kilo)
plt.show()
