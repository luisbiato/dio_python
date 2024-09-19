import sys


def menu():
    print("""
[d]  = Depositar
[s]  = Sacar
[e]  = Extrato
[nc] = Nova Conta
[ls] = Listar Contas
[nu] = Novo Usuário
[q]  = Sair

: """, end = "")
    return input()


def depositar(saldo:float, deposito:float, extrato:str,/):
    deposito = float(input("Valor a ser depositado: "))
    if deposito > 0:
        saldo += deposito
        extrato += f"Depósito: R$ {deposito:.2f}\n"
    else:
        print("O valor é inválido. Operação não realizada!")

    return saldo, extrato


def sacar(*,saldo:float, extrato:str, limite:int, numero_saques:int, limite_saques:int):
    saque = float(input("Valor a ser sacado: "))
    if saque > saldo:
        print("Saldo insuficiente. Operação não realizada!")

    elif saque > limite:
        print("Valor máximo de saque é de R$500,00. Operação não realizada!")

    elif numero_saques >= limite_saques:
        print("Numero máximo de saques diário atingido. Operação não realizada!")

    elif saque > 0:
        numero_saques += 1
        saldo -= saque
        extrato += f"Saque: R$ {saque:.2f}\n"
        print(numero_saques)

    else:
        print("O valor é inválido. Operação não realizada!")

    return saldo, extrato, numero_saques

def extrato(saldo:float,/,*,extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"Saldo: R$ {saldo:.2f}")
    print("==========================================")

def criar_usuario(usuarios:list):
    cpf:str = input("CPF (somente numeros): ")
    cpf_cadastrado = validar_usuario(cpf, usuarios )
    if cpf_cadastrado:
        print("Usuário já cadastrado")
        return usuarios
    nome:str = input("Nome: ")
    data_nascimento:str = input("Data de nascimento(dd-mm-aaaa): ")
    endereco:str = input("Entre com endereço: (logradouro - bairro - cidade/UF)")
    usuario: dict = {}
    usuario["nome"] = nome
    usuario["cpf"] = cpf
    usuario["endereco"] = endereco
    usuario['data_nascimento'] = data_nascimento


    usuarios.append(usuario)
    return usuarios
    
def validar_usuario(cpf, usuarios):
    for i in range(len(usuarios)):
        if  cpf in usuarios[i].values():
            print(usuarios[i])
            return usuarios[i]
        else:
            return None    
        

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Entre com o CPF do titular: ") 
    usuario = validar_usuario(cpf,usuarios )
    print(usuario)

    if usuario:
        print(f"Conta criada com sucesso. AG:{agencia}, Numero de conta: {numero_conta}")
        return {"agencia": agencia, "numero_conta":numero_conta, "usuario": usuario }    
    
    print("Usuario não cadastrado. Não foi possivel criar a conta")

def listar_contas(contas):
    if not contas:
        print("Não existem contas cadastradas.")
    for conta in contas:
        linha = f"Titular: {conta['usuario']['nome']}\nAG:{conta['agencia']}\nNumero de conta: {conta['numero_conta']}"
        print(linha)
        print("-" * 50)
  

def main():
    LIMITE: int = 500
    AGENCIA = "0001"

    saldo: float = 0
    extratos: str= ""
    numero_saque: int = 0
    limite_saque: int = 3
    usuarios: list = []
    contas: list = []
    

    while True:
        operacao:str = menu()

        match operacao:
            case "d":
               saldo, extratos = depositar(saldo,operacao,extratos)

            case "s":
                saldo, extratos, numero_saque = sacar(saldZo= saldo, extrato= extratos, limite= LIMITE, limite_saques= limite_saque, numero_saques= numero_saque)
    
            case "e":
                extrato(saldo, extrato = extratos)

            case "nu":
                usuario = criar_usuario(usuarios)
                usuarios.append(usuario)

            case "nc":
                numero_conta = len(contas) +1
                conta = criar_conta(AGENCIA,numero_conta,usuarios)

                if conta:
                    contas.append(conta)
                

            case "ls":
                listar_contas(contas)

            case "q":
                sys.exit()
                break

        
if __name__ == "__main__":
    main()