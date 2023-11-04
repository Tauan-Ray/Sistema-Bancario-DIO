saldo = 0
limite_saques = 0
extrato = []

while True:
    print('1.Depósito')
    print('2.Saque')
    print('3.Extrato')
    print('4.Sair')

    op = int(input('Escolha uma opção[1/2/3/4]: '))

    if op == 1:
        valor = float(input('Quanto você deseja depositar? '))
        if valor < 0:
            print('Você não pode depositar um valor negativo')

        else:
            saldo += valor
            print('Valor depositado com sucesso!')
            extrato.append(f'Depósito: R${valor}')

    elif op == 2:
        if limite_saques >= 3:
            print('Você ja fez o limite diário de saques')
        
        else:
            quantidade_saque = float(input(('Quanto você deseja sacar? ')))
            if quantidade_saque > 500:
                print('O valor limite para saques é R$500')

            elif quantidade_saque > saldo:
                print('Você não possui saldo suficiente')

            elif quantidade_saque < saldo:
                saldo -= quantidade_saque
                print('Dinheiro sacado com sucesso')
                limite_saques += 1
                extrato.append(f'Saque: R${quantidade_saque}')

    elif op == 3:
        print('Extrato bancário'.center(50))
        for operacao in extrato:
            print(operacao)
        
        print(f'Saldo: R${saldo}')
        print('')

    elif op == 4:
        break

    else:
        print('Escolha uma opção existente')