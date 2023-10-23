CMD = str(input("Prompt de Comando - Digite seu Comando: "))

addComandos = []
verif = 0
resp = ''

def NegocioInput():
    global verif, resp
    resp = str(input("Deseja adicionar outro comando? (S/N): "))
    if resp == "N":
        verif = 0
    else:
        verif = 1
    return verif

def ComandoAdd():
    add = str(input("Digite seu comando para adicionar: "))
    addComandos.append(add)

while True:
    NegocioInput()
    if verif == 0:
        resp = str(input("Apagar o comando anterior? (S/N): "))
        print(addComandos)

        if resp == "S":
            print(f"Comando anterior apagado com sucesso: {addComandos[-1]}")
            addComandos.pop()
            if len(addComandos) != 0:
                print(f"Comandos: {addComandos}")
            else:
                print("Sem comandos para apagar.") 
        else:
            break
    else:
        ComandoAdd()               
