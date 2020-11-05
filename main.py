'''
Há dois exércitos tentando atacar um castelo no centro de uma planície
O exército azul está ao sul e o exército vermelho está ao norte. 
A única possibilidade de vitória para os dois exércitos sobre o castelo é se eles atacarem ao mesmo tempo, 
para isso eles precisam sincronizar um horário para o ataque.
O exército vermelho comanda o exército azul, então ele deve enviar o primeiro mensageiro definindo a hora do ataque.
O exército vermelho dispõe de um sinalizador, ficou combinado entre os exércitos que quando o exército vermelho recebesse o mensageiro do 
exército azul confirmando o horário esse sinalizador seria disparado confirmando o ataque.
O exército Azul tem 1% de chance de impossibilitar o horário, levando o exército azul a enviar um mensageiro para solicitar um novo horário 
para o exército vermelho (quando o exercito vermelho receber o mensageiro do azul ele ira disparar o sinalizador, então volta pro vermelho denovo).
O mensageiro demora entre 60 ~ 70 minutos (3600 segundos ~ 4200 segundos) para atravessar o campo para enviar a mensagem.
O castelo captura cerca de 45% dos mensageiros.
Se após 210 Minutos e 1 segundo (12601 segundos) do envio do primeiro mensageiro do exército vermelho, o mensageiro do exército azul 
não chegar ao exército vermelho declara-se que o mensageiro enviado anteriormente morreu e é enviado outro. 
IMPORTANTE: Se o mensageiro do exército vermelho não morreu, quer dizer que os últimos 3 mensageiros do exército azul 
morreram, logo se há uma chance de que o quarto mensageiro do exército azul chegue no exército vermelho ao mesmo tempo 
que o do vermelho chegue no azul, se o exército vermelho ainda não tiver disparado o sinalizador quando o novo mensageiro 
chegar o exército azul deve enviar outro mensageiro.
Quando o Sinalizador for disparado não há necessidade de enviar novos mensageiros.
Se após 70 minutos e 1 segundo (4201 segundos) do envio do mensageiro do exército azul não for observado o disparo do sinalizador ou 
não receber um novo mensageiro definindo um novo horário, o exército azul declara que o ultimo mensageiro morreu e deve enviar um novo.
Cada exército só pode enviar um mensageiro por vez.
O exército vermelho dispõe de 5 mensageiros, e o azul dispõe de 10 mensageiros;
Se esgotar o número de mensageiros de um exército antes do sinalizador ter sido disparado o exército perde.

Cada grupo deverá escrever um algoritmo para testar esse problema.
O seu algoritmo deve exibir a timestamp[1] de início da troca de mensagens, e a suposta timestamp de termino da troca de 
mensagens (Adicione os valores da viagem dos mensageiros)
O algoritmo deve exibir quanto tempo demorou a troca de mensagens(hh:mm:ss), quantos mensageiros foram utilizados de 
cada exército e se o exército perdeu a batalha.
Deve-se utilizar um gerador randômico para o tempo de travessia do mensageiro, para a possibilidade de o castelo capturar 
um mensageiro e para a possibilidade do exército azul impossibilitar o horário escolhido pelo exército vermelho
'''

import random
import time
from datetime import datetime

def two_generals():
    time_init = datetime.now()
    print("Hora de inicio: "+str(time_init.hour)+':'+str(time_init.minute)+":"+str(time_init.second))
    vermelho_mensageiro = 0
    azul_mensageiro = 0
    time_elapsed = []
    tempoVermelho = []
    tempoAzul = []
    everReached = 0
    while(True):
        if (verMensageiro(vermelho_mensageiro, azul_mensageiro) != 0):
            return verMensageiro(vermelho_mensageiro, azul_mensageiro), time_elapsed
        if (tempoVermelho == []):
            # Envia um mensageiro vermelho e verifica se foi capturado
            time_elapsed, vermelho_mensageiro, tempoVermelho = enviaVermelho(time_elapsed, vermelho_mensageiro, tempoVermelho)
            capturou, time_elapsed, tempoVermelho, tempoAzul = tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul, 0)
        if (capturou == 0 and everReached != 1):
            # Chega no Azul
            imp, time_elapsed, azul_mensageiro = chegaNoAzul(time_elapsed, azul_mensageiro)
            if (imp == 0):
                everReached = 1
        if (everReached == 1):
            if (tempoAzul == []):
                # Envia um mensageiro azul e verifica se foi capturado
                time_elapsed, azul_mensageiro, tempoAzul = enviaAzul(time_elapsed, azul_mensageiro, tempoAzul)
                capt, time_elapsed, tempoVermelho, tempoAzul = tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul, 1)
            if (capt == 0):
                return 0, time_elapsed
            if (capt == 1 or tempoAzul == [70,70]):
                tempoAzul = []

        if (capturou == 1 or tempoVermelho == [70,70,70]):
            tempoVermelho = []
        if (vermelho_mensageiro == 5 and azul_mensageiro == 0):
            return 1, time_elapsed


def verMensageiro(vermelho_mensageiro, azul_mensageiro):
    if (azul_mensageiro == 10):
        return 2
    return 0


def enviaVermelho(time_elapsed, vermelho_mensageiro, tempoVermelho):
    # Enviando o vermelho
    if (vermelho_mensageiro == 5):
        return time_elapsed, vermelho_mensageiro, tempoVermelho
    vermelho_mensageiro += 1
    time_elapsed.append(random.randint(3600, 4201))
    print("Enviando mensageiro vermelho", 5-vermelho_mensageiro,"restantes")
    return time_elapsed, vermelho_mensageiro, tempoVermelho


def tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul ,azul):
    tentativa = random.randint(1, 101)
    tempoDecorrido = random.randint(60, 71)
    tempoVermelho.append(tempoDecorrido)
    if (azul == 1):
        tempoDecorrido = random.randint(60, 71)
        tempoAzul.append(tempoDecorrido)
    if (tentativa <= 45):
        print("Castelo Capturou!")
        time_elapsed.append(210 * 60 + 1)
        return 1, time_elapsed, tempoVermelho, tempoAzul
    else:
        print("Castelo nao Capturou!")
        return 0, time_elapsed, tempoVermelho, tempoAzul


def chegaNoAzul(time_elapsed, azul_mensageiro):
    negar = random.randint(1, 101)
    if(negar == 1):
        print("Exercito azul impossibilitou o horário!")
        return 1, time_elapsed, azul_mensageiro
    else:
        print("Exercito azul aceita o horário!")
        return 0, time_elapsed, azul_mensageiro


def enviaAzul(time_elapsed, azul_mensageiro, tempoAzul):
    # Enviando o azul
    azul_mensageiro += 1
    time_elapsed.append(random.randint(3600, 4201))
    print("Enviando mensageiro azul", 10-azul_mensageiro,"restantes")
    return time_elapsed, azul_mensageiro, tempoAzul
            

def seg_toDateTime(s):
    s = s % (24 * 3600 * 60)
    s %= 216000
    hour = s // 3600
    s %= 3600
    minutes = s // 60
    s %= 60
    return hour, minutes, s


problem, time_elapsed = two_generals()
if problem == 0:
    print("\nSinalizador disparado")
if problem == 1:
    print("\nVermelho sem mensageiros")
if problem == 2:
    print("\nAzul sem mensageiros")

for i in range(0, len(time_elapsed)):
    try:
        if (time_elapsed[i+1] == 12600):
                time_elapsed[i] = 0
    except:
        None

time_stamp_inicial = time.time()
time_stamp_final = time_stamp_inicial + sum(time_elapsed)

hour, minutes, s = seg_toDateTime(sum(time_elapsed))

print("Tempo decorrido: %02d:%02d:%02d"%(hour, minutes, s))
print("\nTimestamp Inicial: %.0f"%(time_stamp_inicial))
print("Timestamp Final: %.0f"%(time_stamp_final))