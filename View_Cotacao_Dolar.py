import datetime
import time
from Controller_Cotacao_Dolar import requisicao

from Service_Cotacao_Dolar import msg

def esta_na_hora(hora, minuto, data_atual):
    if data_atual.hour == hora and data_atual.minute == minuto:
        return True
    return False


def processa_dias_da_semana(dias_da_semana):
    dias_da_semana_int = []
    for dia in dias_da_semana:
        if dia == "seg":
            dias_da_semana_int.append(0)
        if dia == "ter":
            dias_da_semana_int.append(1)
        if dia == "qua":
            dias_da_semana_int.append(2)
        if dia == "qui":
            dias_da_semana_int.append(3)
        if dia == "sex":
            dias_da_semana_int.append(4)
        if dia == "sab":
            dias_da_semana_int.append(5)
        if dia == "dom":
            dias_da_semana_int.append(6)

    return dias_da_semana_int


def esta_no_dia_da_semana(dias_da_semana, data_atual):
    if data_atual.weekday() in dias_da_semana:
        return True

    return False


print("###################################################")

print("PEGANDO COTACAO DO DOLAR VIA API E ENVIANDO POR EMAIL!")

print("###################################################")

hora_string = input("Que horas quer receber a cotacao do Dolar? (hh:mm): ")

dia_da_semana_string = input("Que dias da semana? (seg ter qua qui sex sab dom): ")

hora = int(hora_string.split(':')[0])
minuto = int(hora_string.split(':')[1])

dias_da_semana = dia_da_semana_string.split(' ')
dias_da_semana_int = processa_dias_da_semana(dias_da_semana)

agora = datetime.datetime.now()

while True:
    agora = datetime.datetime.now()
    print(agora)

    if esta_na_hora(hora, minuto, agora) and esta_no_dia_da_semana(dias_da_semana_int, agora):
        requisicao

    time.sleep(60)
