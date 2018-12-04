## Introdução

A fotossíntese é resultado de uma série de reações químicas que ocorrem no interior das células das plantas.
Portanto, para modelar a fotossíntese, é preciso modelar estas reações \cite{denning1993relating}.

Em uma reação catalizada por uma enzima, ocorre o seguinte:
A enzima (E) se liga aos substratos (S) da reação com uma constante de equilbrio k1, formando um composto intermediário (ES), enquanto este composto se dissocia em enzima e substratos com uma constante k2.
A seguir, este composto intermediário dá origem aos produtos da reação (P), fazendo com que a enzima retorne a seu estado original (E), com uma constante de equilíbrio k3.

Cada uma das etapas desta série de reações apresenta uma constante de equilíbro.
Quando a reação entra em equilíbrio, a variação da concentração de enzima é igual a zero e se dá conforme a Equação:

d[ES]/dt = k1[E][S] - (k2 + k3)[ES] = 0

Neste caso, a concentração de ES segue a Equação:

[ES] = [E][S]/((k_2 + k_3)/(k_1)) = [E][S]/KM

Como o denominador desta equação é formado somente por constantes, é introduzida a KM, chamado de constante de Michaelis.

Isto é, KM = (k2 + k3)/(k1)

Esta constante é utilizada na Equação de Michaelis-Menten para o cálculo da velocidade de uma reação (V) em função de sua velocidade máxima (Vmax) e da concentração de substrato ([S]).

V = Vmax * [S]/([S] + KM)

O efeito de temperatura de uma reação também pode ser modelado utilizando algumas equações.
Entre elas, estão as Equações do Q10:

k = k25 * Q10^((Tk - 298,15)/10)

a equação de Arrhenius

k = k25 * e^(Ea*(T_k - 298,15)/(298,15*R*Tk))

e uma versão da equação de Arrhenius modificada.

k = k_opt * (Hd * e^(Ha * (Tk - T_opt)/(Tk * R * T_opt)))/(Hd - Ha * (1 - e^(Hd * (Tk - T_opt)/(Tk*R*T_opt))))

A Equação do Q10 modela um parâmetro k em função de seu valor a 25ºC, ou 298,15K, (k25), da temperatura atual (Tk), em K, e do parâmetro empírico Q10.
Já a equação de Arrhenius utiliza também, como parâmetros, a energia de ativação da enzima (Ea) e a constante universal dos gases (R = 8,314).
A Equação modificada de Arrhenius utiliza a temperatura ótima da reação (T_opt) e o valor do parâmetro k a esta temperatura (k_opt).
Além disso, utiliza os parâmetros Ha, equivalente à Ea, e Hd, equivalente ao decréscimo da equação depois do ponto ótimo.

## Fotossíntese
### Fase clara

Durante a fase clara, é gerada a energia utilizada na fase escura da fotossíntese.

O início desta fase se dá quando as moléculas de clorofila presentes nos cloroplastos são excitadas por fótons do espectro fotossinteticamente ativo, provindos do Sol.
Estes fótons são absorvidos por moléculas componentes do Complexo Antena dos fotossistemas.
Ao absorver um fóton, estas moléculas transmitem sua energia, até alcançar o chamado Centro de Reação do fotossistema.
A molécula presente no centro de reação absorve esta energia e, em troca, emite um elétron.
Este elétron precisa ser recebido por um aceptor de elétrons próximo ao centro de reação, e deve ser reposto por um doador de elétrons.

A membrana dos tilacoides, nos cloroplastos, apresenta dois fotossistemas: Fotossistema 1 e Fotossistema 2.
No caso do Fotossistema 1, o aceptor final reduz uma molécula de NADP, a transformando em NADPH2.
O doador de elétron para o Fotossistema 1 está no final de uma cadeia de transporte de elétrons, iniciada pelo aceptor de elétrons do Fotossistema 2.
Nesta cadeia de transporte de elétrons, uma molécula de ADP é transformada em ATP, armazenando energia.
Por fim, o doador de elétrons para o Fotossistema 2 são moléculas de H2O fotolisada, gerando H+ e O2.

### Fase escura

Durante a fase escura da fotossíntese, acontece a fixação do carbono proveniente do CO2 atmosférico.
Para isto, inicialmente, uma molécula de ribulose-1,5-bisfosfato (RuBP) é convertida em duas moléculas de 3-fosfoglicerato, pela ação da enzima ribulose-1,5-bisfosfato carboxilase (RuBisCO), processo chamado de carboxilação da RuBisCO.

No entanto, caso a RuBisCO utilize uma molécula de O2 no lugar da molécula de CO2 como substrato, faltará um átomo de carbono para um dos 3-fosfoglicerato, gerando um 2-fosfoglicolato em seu lugar.
Este processo é conhecido como oxigenação da RuBisCO, ou fotorrespiração.

Ao fim da fase escura, o carbono da atmosfera deve ser transferido a uma molécula de açúcar e a molécula de RuBP deve ser recomposta.
Isto ocorre através do Ciclo de Calvin-Benson.

## Modelo

Foi utilizado principalmente o modelo de Farquhar, com algumas modificações para o efeito da temperatura, propostas por Collatz (1991), Bernacchi (2001) e Medlyn (2002).

Por este modelo, a assimilação líquida de carbono (An) é dada pela Equação:

An = min(wc, wj, ws) - Rd

Em que wc é a taxa de fotossíntese limitada pela RuBisCO, wj é a taxa de fotossíntese limitada pela cadeia de transporte de elétrons, ws é a taxa de fotossíntese limitada pela síntese do produto final (açúcar) e Rd representa o carbono perdido pela respiração.
A dependência do Ciclo de Calvin em wc, wj e ws pode ser observada na Figura 5, enquanto a diferença entre o mínimo destes valores e Rd vem do fato que se deseja calcular a fotossíntese líquida, isto é, a fotossíntese bruta menos a respiração.

Segundo Farquhar, wc pode ser dado pela equação abaixo, a qual, por sua vez, vem da equação de Michaelis-Menten.

wc = Vc_max * C/(C + Kc * (1 + O/Ko))

Em que Vc_max é a velocidade máxima da carboxilação da RuBisCO, Kc é a constante de Michaelis para a carboxilação e Ko é a constante de Michaelis para a oxigenação da RuBisCO, C é a concentração de carbono e O é a concentração de oxigênio.

Já wj, segundo Medlyn (2002), é obtido pela Equação abaixo, em que J é a taxa de transporte de elétrons e Gamma* é o ponto de compensação de gás carbônico, desconsiderando-se Rd.

wj = (J/4) * (C - Gamma*)/(C + 2*Gamma*)

Também segundo Medlyn (2002), J pode ser obtido em função de J_max, a taxa máxima de transporte de elétrons, e de APAR, a radiação fotossinteticamente ativa absorvida, encontrando-se as raízes da Equação abaixo.

theta * J^2 - (alpha * APAR + J_max)*J + alpha * APAR * J_max = 0

Em que alpha e theta são parâmetros empíricos.

Também, Collatz (1991) afirmam que ws = V_max/2 é uma boa estimativa de ws.

Farquhar também apresenta a equação abaixo como forma de calcular Gamma*, em que Vo_max é a velocidade máxima da oxigenação da RuBisCO.

Gamma* = (K_c * Vo_max * O)/(2 * Ko * Vc_max)

Por fim, Collatz (1991) apresentaram as Equações abaixo, como uma forma de ajustar Vc_max e Rd à temperatura (Tk, em Kelvin).
Neste modelo, Vc_max_o representa a Vc_max original calculada pelo modelo de Farquhar. Também de acordo com Farquhar, Rd_o = 0,015 * Vc_max.
Além disso, a e b são constantes empíricas, oferecidas por Collatz (1991).

Vc_max = Vc_max_o/(1 + e^((-a+b*(Tk))/(R * Tk))

Rd = (Rd_o)/(1 + e^(1,3*(Tk - 328,15)))

## Circuito

Para compor o circuito, utilizou-se um Raspberry Pi 3, um leitor de temperatura LM35, um leitor de luminosidade LDR GL5528 e um conversor analógico/digital MCP3008.

### Leitura de temperatura

Para a leitura da temperatura, foi utilizado um sensor LM35.
Considerou-se, conforme a documentação, uma variação de 10mV/ºC.
A acurácia deste sensor é de +- 0,5 ºC.

### Leitura de luminosidade

A leitura de luminosidade foi feita com o sensor LDR GL5528.
Foi feita uma calibração da leitura obtida por este sensor com os dados do INMET, durante um dia.
Com estes dados, obteve-se a equação abaixo:

Y = -12954,9 + 12932,99 * e^(1/X)

Para esta curva, obteve-se um R^2 de 0,7435 e uma raiz do erro quadrático médio (RMSE) igual a 84,34 W/m^2.

### Conversão do sinal analógico para digital

Por fim, foi feita a conversão do sinal analógico para digital utilizando o conversor MCP3008.
Este componente utiliza o protocolo de comunicação serial SPI para se comunicar com o Raspberry Pi.
Por este protocolo, o Raspberry Pi envia um sinal de ``relógio'' (CLK) para o MCP3008, que marca os bits enviados entre ambos.
O Raspberry Pi controla de qual canal do MCP3008 deseja obter os dados através do pino MOSI (do inglês, Master-Out, Slave-In), enquanto o MCP3008 devolve os dados pelo pino MISO (do inglês, Master-In, Slave-Out).
É necessário um divisor de tensão para reduzir a tensão no pino MISO de 5V para 3,3V, tensão máxima suportada pelo Raspberry Pi.

O código foi escrito utilizando a linguagem Python e foi dividido em três arquivos.
