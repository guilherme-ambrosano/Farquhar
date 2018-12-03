import math
import numpy as np
import leitura_dados

#R = constante universal dos gases (J/(mol*K))
R = 8.314

def medlyn(kopt, Ha, Hd, Topt, Tk):
    #kopt = valor do parametro na condicao de temperatura otima
    #Ha = energia de ativacao (taxa de ascencao antes do ponto otimo)
    #Hd = taxa de decrescimo depois do ponto otimo
    #Topt = temperatura ótima da enzima
    e1 = np.exp(Ha*(Tk - Topt)/(Tk*R*Topt))
    e2 = np.exp(Hd*(Tk - Topt)/(Tk*R*Topt))
    peak = kopt*Hd*e1/(Hd - Ha*(1 - e2))
    return(peak)

def arrhenius(k25, Ha, Tk):
    #k25 = valor a 25 graus
    #Ha = energia de ativacao
    #Tk = temperatura atual
    return(k25*np.exp((Ha*(Tk-298.15))/(298.15*R*Tk)))

def collatz(vmax, temp):
    a = 220
    b = 703
    return(vmax*pow((1 + np.exp(-a+b*(temp)/(R*temp))), -1))

def Q10(k25, q10, temp):
    #Q10 = sensibilidade da reacao a uma mudança de 10 graus celsius
    return(k25*pow(q10, (temp-298.15)/10))

def farquhar(temp=25.0,APAR=500.0):
    #temperatura em kelvin
    temp += 273.15

    #jmax = taxa maxima de fotossintese limitada pelo transporte de eletrons
    #Medlyn (soja)
    kopt_jmax = 328.57
    Ha_jmax = 88820
    Hd_jmax = 113770
    Topt_jmax = 38.17+273.15
    jmax = medlyn(kopt_jmax, Ha_jmax, Hd_jmax, Topt_jmax, temp)

    #farquhar
    q10_vmax = 2.21
    k25_vmax = 98
    vmax = Q10(k25_vmax, q10_vmax, temp)

    #Collatz (1991)
    vmax = collatz(vmax, temp)

    #psfc = pressao atmosferica na superficie
    psfc = 95000
    #ci = pressao parcial de co2 (Pa)
    ci = 30
    #oi = pressao parcial de o2 (Pa)
    oi = 0.209*psfc

    #gammac = ponto de compensacao de co2 sem Rd corrigido p temperatura
    # Bernacchi et al. (2001) / tabaco
    k25_gammac = 3.1
    Ha_gammac = 37830
    gammac = arrhenius(k25_gammac, Ha_gammac, temp)

    #kc = constante de Michaelis-Menten para carboxilacao
    #ko = constante de Michaelis-Menten para oxidacao
    k25_kc = 46
    Ha_kc = 59356
    kc = arrhenius(k25_kc, Ha_kc, temp)
    k25_ko = 33000
    Ha_ko = 35948
    ko = arrhenius(k25_ko, Ha_ko, temp)

    #respiracao - fase escura
    Rd_o = 0.015*vmax
    #corrigido por Collatz (1991)
    Rd = Rd_o/(1 + np.exp(1.3*(temp-(55+273.15))))

    #gamma = ponto de compensacao de co2 com Rd
    gamma = (gammac + kc*(1+oi/ko)*Rd/vmax)/(1 - Rd/vmax)

    #solucao da equacao quadratica por Bonan (2008)
    alfa = 0.3
    theta = 0.9
    a = theta
    b = -(jmax + alfa*APAR)
    c = alfa*jmax*APAR
    j1 = (-b + np.sqrt(pow(b, 2) - 4*a*c))/(2*a)
    j2 = (-b - np.sqrt(pow(b, 2) - 4*a*c))/(2*a)
    j = min(j1, j2)

    #taxa de fotossintese limitada pela rubisco
    wc = vmax*(ci - gammac)/(ci+kc*(1+oi/ko))
     
    #taxa de fotossintese limitada pela luz
    wj = j*(ci - gammac)/(4*(ci+2*gammac))

    #taxa de fotossíntese limitada pelo produto final
    ws = vmax/2

    #assimilacao
    An = min(wc, wj, ws) - Rd

    return An
