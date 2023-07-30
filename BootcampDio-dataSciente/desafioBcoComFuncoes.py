import textwrap

def menu():
    menu = '''\n
    ====MENU=====
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova Conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair

    =>'''
    return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\t\tR$: {valor:.2f}\n"
        print("=== Depósito realizado com sucesso ===")
    else:
        print("___ Erro! : Valor informado é inválido. ___")
    
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques > limite_saques

    if excedeu_saldo:
        print("____ Você não tem saldo suficiente")
    elif excedeu_limite:
        print("___ Excedeu o valor limite de saque")
    elif excedeu_saques:
        print("___ Excedeu o limite de número de saques")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("=== Saque realizado com sucesso. ===")
    else:
        print("___ Erro! O valor informado é inválido")
    
    return saldo, extrato

def exibir_extrato(saldo, /, *, extrato):
    print("\n=== Extrato: ===")
    print("Não foram realizadas movimentações" if not extrato else extrato)
    print(f"\nSaldo:\t\tR$: {saldo:.2f}")
    print("============")

def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números!): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("! ___ Já existe usuario com CPF informado!")
        return

    nome = input("Informe nome completo: ")
    data_nascimento = input("Informe data de nascimento (dd-mm-aa): ")
    endereco = input("Informe o endereço (logadouro, nro, bairro, cidade, sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("=== Usuario cadastrado com sucesso! ===")

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuario: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("=== Conta criada com sucesso ===")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
    
    print("\n___Usuario não encontrado!, fluxo de criação de conta encerrado!")

    return None

def listar_contas(contas):
    for conta in contas:
        linha = f'''\n
            Agência:\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t{conta['usuario']['nome']}
        '''
        print("=" * 20)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 1
    usuarios = []
    contas = []
    

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor de deposito: "))
            
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor para sacar: "))
            
            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)
        
        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar nosso menu do Banco")
            break

        else:
            print("Opção inválida. Por favor verifique")

main()