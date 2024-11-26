inicio_HORA             = int(input("INICIO DA VIAGEM HORA : "))
inicio_MINUTOS          = int(input("INICIO DA VIAGEM MINUTOS : "))
chegada_HORA            = int(input("CHEGADA DA VIAGEM HORA : "))
chegada_MINUTOS         = int(input("CHEGADA DA VIAGEM MINUTOS: "))
descanço                = int(input("QUANTO TEMPO DE DESCANÇO : "))
litros_de_gasolina      = float(input("GASOLINA USADA : "))
preco_da_gasolina_litro = float(input("PREÇO DA GOSOLINA R$: "))
distancia               = float(input("DISTÂNCIA PERCORRIDA KM: "))

 # a) O tempo da viagem (em segundos) 

inicio_tempo   = (inicio_HORA * 3600)  + (inicio_MINUTOS * 60)
chegada_tempo  = (chegada_HORA * 3600) + (chegada_MINUTOS * 60 )
segundos_tempo = chegada_tempo - inicio_tempo 
tempo_hora     =  segundos_tempo / 3600 
 
 # Tempo do descanço da viagem 
descanço_tempo = descanço / 3600

print(f'O TEMPO DA VIAGEM FOI DE {tempo_hora}')
print(f'O TEMPO DE DESCANÇO FOI DE {descanço_tempo}' )

# b) A velocidade média (Km/h) global e a velocidade média em movimento (Km/h) 

velocidade_global    =  distancia / tempo_hora 
velocidade_movimento =  distancia / ( tempo_hora - descanço_tempo )

print (f' A VELOCIDADE GLOBAL(MÉDIA) KM É DE {velocidade_global}')
print (f' A VELOCIDADE DE MOVIMENTO É DE {velocidade_movimento} ')

# c) O custo da viagem com combustível (em R$) 

gasolina_gasto = litros_de_gasolina * preco_da_gasolina_litro

print (f' FOI GASTO {gasolina_gasto} R$ EM GASOLINA')

# d) O desempenho do carro (em Km/l, l/h e R$/Km)

desempenho_em_km     = gasolina_gasto / distancia
desempenho_em_litros = distancia / litros_de_gasolina

print(f'O DESEMPENHO DO CARRO EM KM FOI DE {desempenho_em_litros} ' )
print(f'O DESENPELHO DO CARRO EM HORAS FOI DE {desempenho_em_km} ')
