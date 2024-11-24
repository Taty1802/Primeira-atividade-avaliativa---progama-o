from datetime import datetime

dia_inicial = int(input("DATA INICIO (dia): "))
mes_inicial = int(input("MÊS INICIO: "))
dia_final   = int(input("DATA FINAL (dia): "))
mes_final   = int(input("MÊS FINAL: "))

ano = 2024 # TIVE QUE COLOCAR O ANO, POIS ESTAVA DANDO ERRO SEM ELE. 

data_inicial = datetime(ano,mes_inicial, dia_inicial)
data_final   = datetime(ano,mes_final, dia_final)


if data_inicial > data_final:
    print("ERRO DIGITE PRIMEIRO A DATA INICIAL :")
else:
    diferenca = (data_final - data_inicial).day
    print(f'FORAM {diferenca} DIAS DE DIFERENÇA')
