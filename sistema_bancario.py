saldo = 0
limite = 500
limite_diario = 1500
saque_total = 0
extrato = []
numero_saques = 0
LIMITE_SAQUES = 3

def menu():
    opcao = input ("""    
    Digita a letra referente a transação que deseja realizar:
    
    [d] Depositar
    [s] Sacar
    [e] Extrato
    [q] Sair
    """)
    
    return opcao

def depositar():
    valor = float(input("Digite quanto deseja depositar: "))
    return valor

def sacar():
    valor = float(input("Digite quanto deseja sacar: "))
    return valor

def exibe_extrato(extrato):
    print("===============================") 
    print("          EXTRATO       ")
    print("===============================") 
    print("")
    if len(extrato) > 0:            
            for operacao in extrato:
                 print (operacao)
            print("")
            print(f"     saldo \033[34mR${saldo: .2f}\033[0m")
            print("===============================") 
    else:
        print("não há transações registradas em sua conta")

while True:

    opcao = menu()

    if opcao == "d":
        deposito = depositar()
        if deposito > 0:
            saldo += deposito
            extrato.append(f"depósito      \033[32mR${deposito: .2f}\033[0m")
        else:
            print ("Operação inválida")
        

    elif opcao == "s":
        saque = sacar()
        saque_total += saque
        if (saque <= limite) and (numero_saques < LIMITE_SAQUES) and (saque_total <= limite_diario) and (saque <= saldo) and (saque > 0):
            saldo -= saque
            numero_saques += 1
            extrato.append(f"saque          \033[31m-R${saque: .2f}\033[0m")
        else:
            print ("Operação inválida")
    
    elif opcao == "e":
        exibe_extrato(extrato)        

    elif opcao == "q":
        break
    else:
        print ("Operação inválida")