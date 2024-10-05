


from datetime import date

from models import Conta, Deposito, PessoaFisica, Historico, Saque


clientes = []

while True:
    print("Menu")
    print("1 - Criar conta")
    print("2 - Realizar saque")
    print("3 - Realizar um depósito")
    print("-1 - Sair")
    opcao = int(input("Digite a opção"))

    if opcao == 1:
        cpf = input("Digite o número do CPF")
        nome = input("Digite o nome do cliente")
        dia = int(input("Digite o dia de nascimento"))
        mes = int(input("Digite o mês de nascimento"))
        ano = int(input("Digite o ano de nascimento"))
        data_nascimento = date(ano, mes, dia)
        endereco = input("Digite o endereço")

        pessoa = PessoaFisica(cpf, nome, data_nascimento, endereco)

        historico = Historico()
        valor = float(input("Digite o valor inicial da conta"))
        numero = 0

        conta = Conta(valor, numero, "0001", pessoa, historico)
        pessoa.adicionar_conta(conta)
        clientes.append(pessoa)
        numero+= 1

    elif opcao == 2:

        pessoa = None
        cpf = input("Digite o CPF do cliente")
        for cliente in clientes:
            if cliente.cpf == cpf:
                pessoa = cliente

        saque = float(input("Digite o valor a ser sacado"))
        transacao = Saque(saque)

        pessoa.realizar_transacao(transacao)

    elif opcao ==3:
         cpf = input("Digite o CPF do cliente")
         for cliente in clientes:
            if cliente.cpf == cpf:
                pessoa = cliente

         valor = float(input("Digite o valor a ser depositado"))
         transacao = Deposito(valor)

         pessoa.realizar_transacao(transacao)

    elif opcao == -1:
        print("Saindo")
        break

    else:
        print("Operação inválida")


