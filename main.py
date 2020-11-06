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

# Desenvolvido por:
#   Diogo Silveira dos Santos
#   João Vitor Izael Souza
#   João Vitor Oliveira de Melo
#   Luiz Otávio de Oliveira Silva
#   Pedro Henrique Carreto Morais

import random
import time
from datetime import datetime


def two_generals():
    # Obtenção e exibição do horário do início
    time_init = datetime.now()
    print("Hora de inicio: "+str(time_init.hour)+':' + str(time_init.minute)+":"+str(time_init.second))

    # Inicialização de variáveis
    vermelho_mensageiro, azul_mensageiro = 0, 0
    tempoVermelho, tempoAzul, time_elapsed, time_imp = [], [], [], []
    everReached, capt = 0, 1

    while(True):
        # Verifica se existem mensageiros restantes
        if (verMensageiro(vermelho_mensageiro, azul_mensageiro) != 0):
            return verMensageiro(vermelho_mensageiro, azul_mensageiro), time_elapsed

        if (tempoVermelho == []):
            # Envia um mensageiro vermelho e verifica se foi capturado
            time_elapsed, vermelho_mensageiro, tempoVermelho = enviaVermelho(time_elapsed, vermelho_mensageiro, tempoVermelho)
            capturou, time_elapsed, tempoVermelho, tempoAzul = tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul, 0)

            if (capturou == 0):
                # Chega no Azul
                imp, time_elapsed, azul_mensageiro = chegaNoAzul(time_elapsed, azul_mensageiro)
                if (imp == 0):
                    everReached = 1
                else:
                    while (sum(time_imp) < 12600):
                        time_elapsed, azul_mensageiro, tempoAzul = enviaAzul(time_elapsed, azul_mensageiro, tempoAzul)
                        voltou, time_elapsed, tempoVermelho, tempoAzul = tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul, 1)
                        if (voltou == 0):
                            # Não foi capturado no retorno da impossibilitação
                            time_imp.append(12600)
                            print("Sinalizador disparado da impossibilitação")
                        else:
                            time_imp.append(random.randint(3600, 4201))
                    time_imp = []

        if (everReached == 1):
            if (tempoAzul == []):
                # Envia um mensageiro azul e verifica se foi capturado
                time_elapsed, azul_mensageiro, tempoAzul = enviaAzul(time_elapsed, azul_mensageiro, tempoAzul)
                capt, time_elapsed, tempoVermelho, tempoAzul = tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul, 1)
            if (capt == 0):
                # Não foi capturado, logo o sinalizador foi disparado
                return 0, time_elapsed
            if (capt == 1 or sum(tempoAzul) > 4200):
                tempoAzul = []

        if (sum(tempoVermelho) > 12600 or everReached == 0):
            tempoVermelho = []


# Verifica a existência de mensageiros
def verMensageiro(vermelho_mensageiro, azul_mensageiro):
    if (vermelho_mensageiro == 5):
        return 1

    if (azul_mensageiro == 10):
        return 2

    return 0


# Envia um mensageiro vermelho
def enviaVermelho(time_elapsed, vermelho_mensageiro, tempoVermelho):
    if (vermelho_mensageiro == 5):
        return time_elapsed, vermelho_mensageiro, tempoVermelho

    vermelho_mensageiro += 1
    time_elapsed.append(random.randint(3600, 4201))

    print("Enviando mensageiro vermelho", 5-vermelho_mensageiro, "restantes")
    return time_elapsed, vermelho_mensageiro, tempoVermelho


# Realiza a verificação randômica de captura de travessia
def tentativaCaptura(time_elapsed, tempoVermelho, tempoAzul, azul):
    tentativa = random.randint(1, 101)
    tempoDecorrido = random.randint(3600, 4201)
    tempoVermelho.append(tempoDecorrido)

    if (azul == 1):
        tempoAzul.append(tempoDecorrido)

    if (tentativa <= 45):
        print("Castelo Capturou!")
        time_elapsed.append(12600 + 1)
        return 1, time_elapsed, tempoVermelho, tempoAzul
    else:
        print("Castelo nao Capturou!")
        return 0, time_elapsed, tempoVermelho, tempoAzul


# Verifica se o azul aceita o horário proposto
def chegaNoAzul(time_elapsed, azul_mensageiro):
    negar = random.randint(1, 101)

    if(negar == 1):
        print("Exercito azul impossibilitou o horário!")
        return 1, time_elapsed, azul_mensageiro
    else:
        print("Exercito azul aceita o horário!")
        return 0, time_elapsed, azul_mensageiro


# Envia um mensageiro azul
def enviaAzul(time_elapsed, azul_mensageiro, tempoAzul):
    azul_mensageiro += 1
    time_elapsed.append(random.randint(3600, 4201))

    print("Enviando mensageiro azul", 10-azul_mensageiro, "restantes")
    return time_elapsed, azul_mensageiro, tempoAzul


# Transforma segundos para horas, minutos e segundos
def seg_toDateTime(s):
    s = s % (24 * 3600 * 60)
    s %= 216000
    hour = s // 3600
    s %= 3600
    minutes = s // 60
    s %= 60
    return hour, minutes, s


# Inicia o problema
problem, time_elapsed = two_generals()

# Verifica as saidas obtidas
if problem == 0:
    print("\nSinalizador disparado")

if problem == 1:
    print("\nVermelho sem mensageiros")

if problem == 2:
    print("\nAzul sem mensageiros")

# Elimina contagens de tempo inválidas
for i in range(0, len(time_elapsed)):
    try:
        if (time_elapsed[i+1] == 12600):
            time_elapsed[i] = 0
    except:
        None

# Define e exibe os timestamps
time_stamp_inicial = time.time()
time_stamp_final = time_stamp_inicial + sum(time_elapsed)

hour, minutes, s = seg_toDateTime(sum(time_elapsed))

print("Tempo decorrido: %02d:%02d:%02d" % (hour, minutes, s))
print("\nTimestamp Inicial: %.0f" % (time_stamp_inicial))
print("Timestamp Final: %.0f" % (time_stamp_final))
