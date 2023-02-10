# Pintar a Parede 
# Defini a altura da parede 
altura=float(input('Qual a altura da parede em metros? '))
# Defini a largura da parede
largura=float(input('Quala largura da parede em metros? '))
# Descobri a área da parede
area=altura*largura
result=area/2
print('A quantidade de tinta necessária é: {:.0f} litros'.format(result))
# Outro exercicio a baixo
# Tabuada
print('Começou o Jogo da tabuada\n')
print('-'*20)
num=int(input('Digite um número: '))
for i in range(11):
    print('Seu resultado é: {} X {} = {}'.format(num,i,num*i))

# Desconto de compra 
valorSemDesconto=float(input('Digite o valor sem desconto: '))
valorDoDesconto=valorSemDesconto*(5/100)
print('O valor do desconto é : {}'.format(valorDoDesconto))
print('O valor para pagar com desconto é: {} '.format(valorSemDesconto-valorDoDesconto))