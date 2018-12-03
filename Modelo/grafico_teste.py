import time
import matplotlib.pyplot as plt
import numpy as np
import math
import farquhar

tempo_inicial = float(time.strftime("%S")) + float(time.strftime("%M"))*60 + float(time.strftime("%H"))*3600

plt.style.use("ggplot")

plt.ion()

time.sleep(1)

x = []
y = []

plt.ylabel("CO2")
plt.xlabel("tempo")
plt.ylim(0, 50)

while True:
    tempo = (float(time.strftime("%S")) + float(time.strftime("%M"))*60 + float(time.strftime("%H"))*3600) - tempo_inicial
    y.append(farquhar.farquhar())
    x.append(tempo)

    plt.scatter(x, y, color = "black")
    plt.plot(x, y, color = "black")
    #print(x, y)

    plt.pause(1)

