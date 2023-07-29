menu = '''

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=>
'''

saldo = 0
limite = 500
extrato = ""
numero_saques = 1
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor de deposito: "))
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
        else:
            print("Erro! : Valor informado é inválido.")

    elif opcao == "s":
        valor = float(input("Informe o valor para sacar: "))
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques > LIMITE_SAQUES

        if excedeu_saldo:
            print("Você não tem saldo suficiente")
        elif excedeu_limite:
            print("Excedeu o valor limite de saque")
        elif excedeu_saques:
            print("Excedeu o limite de número de saques")
        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Erro! O valor informado é inválido")


    elif opcao == "e":
        print("\n-------Extrato-------")
        print("Não foram realizadas movimentações" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("------------------------")

    elif opcao == "q":
        print("Obrigado por usar nosso menu do Banco")
        break

    else:
        print("Opção inválida. Por favor verifique")


