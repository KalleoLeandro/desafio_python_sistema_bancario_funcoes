menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[nu] Novo usuário
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3
clientes = []
contas = []
AGENCIA = "0001"

def depositar(valor, saldo, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("\nDepósito realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")
    return saldo, extrato


def sacar(valor, saldo, extrato, limite, numero_saques, limite_saques):
    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\nOperação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("\nOperação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("\nOperação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("\nSaque realizado com sucesso!")
    else:
        print("\nOperação falhou! O valor informado é inválido.")

    return saldo, extrato, numero_saques


def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def cadastrar_cliente(nome, cpf, data_nascimento, endereco):    
    cliente = next((c for c in clientes if c["cpf"] == cpf), None)
    if cliente:
        print("\nJá existe cliente com esse CPF!")
        return

    clientes.append({
        "nome": nome,
        "cpf": cpf,
        "data_nascimento": data_nascimento,
        "endereco": endereco
    })
    print("\nCliente cadastrado com sucesso!")


def cadastrar_conta(cpf):
    cliente = next((c for c in clientes if c["cpf"] == cpf), None)
    if not cliente:
        print("\nCliente não encontrado! Cadastre o cliente primeiro.")
        return

    numero_conta = len(contas) + 1
    contas.append({
        "agencia": AGENCIA,
        "numero_conta": numero_conta,
        "cliente": cliente
    })
    print(f"\nConta criada com sucesso! Agência: {AGENCIA} Conta: {numero_conta}")



while True:
    opcao = input(menu)

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: "))
        saldo, extrato = depositar(valor, saldo, extrato)

    elif opcao == "s":
        valor = float(input("Informe o valor do saque: "))
        saldo, extrato, numero_saques = sacar(
            valor, saldo, extrato, limite, numero_saques, LIMITE_SAQUES
        )

    elif opcao == "e":
        exibir_extrato(saldo, extrato)

    elif opcao == "nu":
        nome = input("Informe o nome completo: ")
        cpf = input("Informe o CPF (somente números): ")
        data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
        endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")
        cadastrar_cliente(nome, cpf, data_nascimento, endereco)

    elif opcao == "nc":
        cpf = input("Informe o CPF do cliente: ")
        cadastrar_conta(cpf)

    elif opcao == "q":
        break

    else:
        print("Operação inválida, por favor selecione novamente a operação desejada.")
