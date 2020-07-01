dias = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos kilometros foram rodados? '))

print('Você deve pagar: R${:.2f}'.format(60*dias+0.15*km))
