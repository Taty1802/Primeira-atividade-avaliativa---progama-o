from datetime import datetime 


# DADOS PESSOAIS.
sexo = (input('DIGITE O SEU SEXO ( mascilino / feminino ) :'))
dia  = int(input('DIGITE O DIA DO SEU NASCIMENTO :'))
mes  = int(input('DIGITE O MÊS DO SEU NASCIMENTO :'))
ano  = int(input('DIGITE O ANO DO SEU NASCIMENTO :'))
# DADOS DA CONTRIBUIÇÃO INICIO 
c_dia = int(input(' DIA QUE COMEÇOU A CONTRUIBUIR :'))
c_mes = int(input( ' MÊS QUE COMEÇOU A CONTRUIBUIR :'))
c_ano = int(input( ' ANO QUE COMEÇOU A CONTRUIBUIR :'))

data_nascimento     = datetime( ano, mes, dia )
inicio_contribuicao = datetime( c_ano, c_mes, c_dia )

# APOSENTADORIA POR IDADE 

aposentadoria_por_idade = (inicio_contribuicao - data_nascimento).days // 365 

if sexo == 'masculino':
    idade_minima = 65
elif sexo == 'feminino':
    idade_minima = 62
else:
    print ('USE MASCULINO OU FEMININO')

if aposentadoria_por_idade >= idade_minima:
    print(f'VOCÊ JÁ PODE SE APOSENTAR POIS VOCÊ JÁ TEM {inicio_contribuicao} ')
else:
    print (f'A IDADE MINIMA É DE {idade_minima} ANOS, VOCÊ AINDA NÃO PODE  ')

 
# APONSENTADORIA POR TEMPO DE CONTRIBUIÇÃO 

tempo_con = (datetime.now() - inicio_contribuicao).days // 365

if sexo == 'masculino':
    minima_idade = 35 
elif sexo == 'feminino':
    minima_idade = 30

else :
    print (f'IDADE MINIMA NÃO ATINGIDA O TEMPO DE CONTRIBUIÇÃO É DE {tempo_con}')


