menu = """
[d] = Depositar
[s] = Sacar
[e] = Extrato
[q] = Sair

"""

saldo: float = 0
limite: int = 500
limite_saques: int = 3
extrato: str= ""
numero_saque: int = 0

while True:
    operacao = input(menu)

    match operacao.lower():
        case "d":
            deposito = float(input("Valor a ser depositado: "))
            if deposito > 0:
                saldo += deposito
                extrato += f"Depósito: R$ {deposito:.2f}\n"
            else:
                print("O valor é inválido. Operação não realizada!")

        case "s":
            saque = int(input("Valor a ser sacado: "))

            if saque > saldo:
                print("Saldo insuficiente. Operação não realizada!")

            elif saque > limite:
                print("Valor máximo de saque é de R$500,00. Operação não realizada!")
            
            elif numero_saque >= limite_saques:
                print("Numero máximo de saques diário atingido. Operação não realizada!")

            elif saque > 0:
                numero_saque +=1
                saldo -= saque
                extrato += f"Saque: R$ {saque:.2f}\n"

            else:
                print("O valor é inválido. Operação não realizada!")
        
        case "e":
            print("\n================ EXTRATO ================")
            print("Não foram realizadas movimentações." if not extrato else extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            print("==========================================")
        
        case "q":
            break
        
        case _ :
            print("Operação inválida, por favor selecione novamente a operação desejada.")