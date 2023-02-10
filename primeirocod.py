# Pintar a Parede 
# Defini a altura da parede 
altura=float(input('Qual a altura da parede em metros? '))
# Defini a largura da parede
largura=float(input('Quala largura da parede em metros? '))
area=altura*largura
result=area/2
print('A quantidade de tinta necessária é: {:.0f} litros'.format(result))