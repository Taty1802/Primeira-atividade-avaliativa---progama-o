valor = float(input(" DIGA O VALOR DO SAQUE: R$ "))

nota_100 = valor // 100
valor %= 100

nota_de_50 = valor // 50
valor %= 50

nota_de_20 = valor // 20
valor %= 20

nota_de_10 = valor // 10
valor %= 10

nota_de_5 = valor // 5
valor %= 5

nota_de_2 = valor // 2
valor %= 2

print(f'NOTAS DE R$ 100,00: {nota_100}')
print(f'NOTAS DE R$ 50,00: {nota_de_50}')
print(f'NOTAS DE R$ 20,00: {nota_de_20}')
print(f'NOTAS DE R$ 10,00: {nota_de_10}')
print(f'NOTAS DE R$ 5,00: {nota_de_5}')
print(f'NOTAS DE R$ 2,00: {nota_de_2}')

moeda_de_1_real = valor // 1
valor %= 1

moeda_de_cinquenta_centavos = valor // 0.50
valor %= 0.50

moeda_de_vinte_cinco_centavos = valor // 0.25
valor %= 0.25

moeda_de_dez_centavos = valor // 0.10
valor %= 0.10

moeda_de_cinco_centavos = valor // 0.05
valor %= 0.05

moeda_de_um_centavo = valor // 0.01
valor %= 0.01

print(f'MOEDAS DE R$ 1,00: {moeda_de_1_real}')
print(f'MOEDAS DE R$ 0,50: {moeda_de_cinquenta_centavos}')
print(f'MOEDAS DE R$ 0,25: {moeda_de_vinte_cinco_centavos}')
print(f'MOEDAS DE R$ 0,10: {moeda_de_dez_centavos}')
print(f'MOEDAS DE R$ 0,05: {moeda_de_cinco_centavos}')
print(f'MOEDAS DE R$ 0,01: {moeda_de_um_centavo}')
