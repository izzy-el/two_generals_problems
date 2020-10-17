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

# print(random.randint(0, 10))
# Duração (60-70) 
# Chance de ser pego no meio - 45%
# Chance do azul impossibilitar ataque - 1%
# Vermelho  => 5 mensageiros
# Azul      => 10 mensageiros

def two_generals():
    sinalizador = 0
    vermelho_mensageiro = 5
    azul_mensageiro = 10
    time_init = datetime.now()
    print("Hora de inicio: "+str(time_init.hour)+':'+str(time_init.minute)+":"+str(time_init.second))

    time_elapsed = []
    
    while(True):
        # Problema em si
        vermelho_mensageiro -= 1
        break


problem = two_generals()

# if problem == 0:
#     # Deu tudo certo
# if problem == 1:
#     # Vermelho sem mensageiros
# if problem == 2:
#     # Azul sem mensageiros
# # ...