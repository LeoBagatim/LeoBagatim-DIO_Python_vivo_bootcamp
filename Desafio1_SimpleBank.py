menu = """

Bem-vindo ao banco SimpleBank!

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

"""
continuar = """
sim (S) ou não (N)
"""

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        print("Você escolheu a opção depósito! Gostaria de continuar ou voltar?")
        opcao_deposito = input(continuar)
        if opcao_deposito == "s":
            print ("Quanto você deseja depositar?")
            deposito = float(input())
            saldo += deposito
            print("Processando depósito...")
            print("Seu saldo agora é: "+str(saldo))
            extrato += "Valor depositado: R$"+str(deposito)+"\n""O Saldo mudou para: R$"+str(saldo)+"\n"
            continue
        elif opcao_deposito == "n":
            continue

    elif opcao == "s":
        print("Você escolheu a opção Saque! Gostaria de continuar ou voltar?")
        opcao_saques = input(continuar)
        if opcao_saques == "s":
            numero_saques += 1
            if numero_saques <= LIMITE_SAQUES:
                print ("Quanto você deseja Sacar?")
                saque = float(input())
                if saldo < saque:
                        print("O Valor do seu saldo é inferior ao do saque requerido.")
                        continue
                elif saque <= 500:
                    saldo -= saque
                    print("Processando saque...")                    
                    print("Seu saldo agora é: "+str(saldo))
                    extrato += "Valor Sacado: R$"+str(saque)+"\n""O Saldo mudou para: R$"+str(saldo)+"\n"
                    continue
                else:
                    print("Valor de saque maior que o limite de R$500 tente novamente")
                    continue
            else: 
                print("Você excedeu seu limite de saques diário.")
        elif opcao_saques == "n":
            continue
    elif opcao == "e":
        print("Você escolheu a opção extrato! Gostaria de continuar ou voltar?")
        opcao_extrato = input(continuar)
        if opcao_extrato == "s":
            print (extrato)
            continue
        elif opcao_extrato == "n":
            continue
    elif opcao == "q":
        print("Sair")
        break
    else: 
        print("Operação Inválida, por favor selecione novamente a operação desejada.")