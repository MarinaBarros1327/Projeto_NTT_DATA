menu = """
[1]Depositar
[2]Sacar
[3]Extrato
[0]Sair
"""

saldo = 0
limite=500
extrato =""
qtd_saques=0
limite_saques =3

while True:
    opcao=input(menu)

    if opcao =="1":
        valor= float(input("informe o valor do deposito"))
        
        if valor >0:
         saldo += valor
         extrato== f"deposito: R$(valor:.2f)\n"

        else:
            print("Operação falhou: O valor informado é invalido")

    
    elif opcao =="2":
        valor= float(input("informe o valor do saque"))

        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saque = qtd_saques >=limite_saques

        if excedeu_saldo:
            print("Erro na operação! Você não tem saldo suficiente.")

        elif excedeu_limite:
            print("Erro na operação! Valor do saque excede o limite.")

        elif excedeu_saque:
            print("Erro na operação! Numero maximo de saque")
        
        elif valor >0:
            saldo += valor
            extrato== f"Saque: R$(valor:.2f)\n"
            qtd_saques+= 1

        else:
             print("Operação falhou: O valor informado é invalido:")

    elif opcao =="3":
        print("\n============extrato===========")
        print("Não foram realizados movimentações."if not extrato else extrato)
        print(f"\n Saldo: R$ {saldo:.2f}")
        print("==============fim===============")

    elif opcao=="0":
        break

    else:
        print("Operação invalida, por favor selecione novamente a operação desejada!")
