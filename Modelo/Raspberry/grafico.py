import time
import matplotlib.pyplot as plt
import numpy as np
import math
import farquhar
import leitura_dados

tempo_inicial = float(time.strftime("%S")) + float(time.strftime("%M"))*60 +
float(time.strftime("%H"))*3600

plt.style.use("ggplot")

plt.ion()

time.sleep(1)

x = []
y = []

plt.ylabel(r'Fotossíntese líquida ($\mu mol \; CO_2 \; m^{-2} \; s^{-1}
$)')
plt.xlabel(r'Tempo ($s$)')
ymax=15
plt.ylim(-5, ymax)

while True:
    try:
        tempo = (float(time.strftime("%S")) + float(time.strftime("
%M"))*60 + float(time.strftime("%H"))*3600) - tempo_inicial
        r,t = leitura_dados.read()
        y.append(farquhar.farquhar(t, r))
        x.append(tempo)

        txt = plt.text(x[0], ymax*0.8, "Temperatura: {} $^o$C
\nIrradiância: {} $\mu$mol fóton".format(t, r) + r' m$^{-2}$ s$^{-1}$')

        plt.hlines(0,xmin = x[0], xmax = x[-1], linestyles = "dashed",
 colors = "#fc9272")
        if y[-1] > ymax:
            ymax = y[-1] + 1

        plt.ylim(-5, ymax)

        plt.scatter(x, y, color = "black", marker = "")
        plt.plot(x, y, color = "black", marker = "")
        

        plt.pause(1)
        txt.remove()
    except KeyboardInterrupt:
        plt.close()
        break

