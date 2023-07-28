menu = """

[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair

=> """

saldo = 0
limite = 500
extrato = """
########## EXTRATO ##########
"""
numero_saque = 0
LIMITE_SAQUES = 3

while True:
    opcao = input(menu)
    
    # DEPOSITAR
    if opcao == "1":
        
        print("Informe o valor a ser depositado")
        valor = float(input("Valor: "))
        
        if valor > 0:
            extrato += f"""
            Saldo: R$ {saldo}"""
            
            saldo += valor
            extrato += f""" 
            Deposito: R$ {valor}

Saldo: {saldo}
            """
            print(extrato)
            print(f"Saldo: R$ {saldo}")
            
        else:
            print("Impossivel depositar este valor")
        
    # SACAR
    
    elif opcao == "2":
        valor = float(input("Informe o valor para saque: "))           
        
        falha_quantidade_saques = numero_saque > LIMITE_SAQUES
        falha_limite_saldo = valor >= saldo
        falha_limite_saques = valor > limite
        
        if falha_quantidade_saques:
            print("FALHA: Só é possivel realizar 3 saques!")
        
        elif falha_limite_saques:
            print("FALHA: Só é possivel realizar saques abaixo de R$ 500")
        
        elif falha_limite_saldo:
            print("FALHA: Saldo insuficiente!")
        else:
            numero_saque += 1
            saldo -= valor
            extrato += f"""
            Saque: R$ {valor}
Saldo: R$ {saldo}
            """
                        
    # EXTRATO
    elif opcao == "3":
        print(f"{extrato}")
        print(f"SALDO: R$ {saldo}")
        print("#########################")
    
    # SAIR
    elif opcao == "4":
        print("Sair")
        break
    
    else: 
        print("Operação invalida, tente novamente")
    
        
    