from time import sleep
menu = '''
Selecione a opção desejada:
[1] DEPÓSITO
[2] SAQUE
[3] VISUALIZAR EXTRATO
[0] SAIR

=> '''

saldo = 0
limite = 500
extrato =""
numero_saques = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)

    if opcao == "1":
        print("DEPÓSITO")
        print("Neste terminal NÃO é aceito o depósito de MOEDAS")
        valor_deposito = float(input("Digite o valor que deseja depositar: R$ "))
        if valor_deposito <= 0:
            print("Digite um valor válido!")

        elif valor_deposito % 1 > 0:
            print("""Opção INVÁLIDA!
        Este terminal NÃO aceita o depósito de MOEDAS""")

        else:
                print("Insira as cédulas no local indicado.")
                sleep(2.5)
                print("\nProcessando...")
                sleep(2)
                print(f"\nDepósito realizado com SUCESSO! \nO valor de "
                      f"R$ {valor_deposito:.2f} já está disponível em sua conta!")
                saldo += valor_deposito
                extrato += f"Depósito: + R$ {valor_deposito:.2f}\n"



    elif opcao == "2":
        print("SAQUE")
        if numero_saques < LIMITE_SAQUES:
            valor_saque = int(input("Digite o valor que deseja SACAR: R$ "))
            if valor_saque <= saldo and valor_saque <= limite and valor_saque > 0:
                saldo -= valor_saque
                numero_saques += 1
                extrato += f"Saque: + R$ {valor_saque:.2f}\n"
                print("\nProcessando...")
                sleep(3)
                print("\nSaque realizado com SUCESSO!")
                print("Retire as cédulas no local indicado.")
            elif valor_saque > saldo:
                print("SALDO INSUFICIENTE! Não foi possível realizar esta operação.")
            elif valor_saque > limite:
                print("Não foi possível realizar esta operação. O valor informado excede o LIMITE de saque.")
        else:
            print("Você excedeu o limite diário de SAQUES! Por favor, retorne outro dia para realizar esta operação.")


    elif opcao == "3":
        print("="*27)
        print("Extrato".center(20))
        print("Não foram realizadas transações!" if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}".center(25))
        print("="*27)

    elif opcao == "0":
        break

    else:
        print("Opção INVÁLIDA!")