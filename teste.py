#Número interno par ou impar verificando se é inteiro
while True:
    numero_recebido = input('Digite um teste: ')
    if numero_recebido.isnumeric() == True:
        print('É inteiro!')
        numero_recebido = int(numero_recebido)
        if numero_recebido%2 !=0:
            print('É impar!')
        else:
            print('É par!')
    else:
        print('Não é inteiro ou não é numérico!')