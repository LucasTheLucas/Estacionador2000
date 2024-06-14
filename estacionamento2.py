'''
Aluno: Lucas Novaes Dias
1° Semestre

Desenvolva uma aplicação Python que utilize ao menos 2 coleções e funções, para que seja possível realizar o 
cadastro de veículos em um estacionamento com o seguinte menu:

1 - Estacionar veículo
2 - Retirar veículo
3 - Veículos estacionados
4 - Está estacionado?
0 - Sair

Deve gravar a placa do veículo que será a chave, marca, modelo, cor e proprietário.
'''
vagas = []

#Essa é a função menu ela mostra todas a opções que o usúario tem e pede para que digite o que vai fazer!
def menu():
    print("Bem-Vindo ao estacinado 3000™")
    print("1 - Estacionar veículo")
    print("2 - Retirar veículo")
    print("3 - Veículos estacionados")
    print("4 - Está estacionado?")
    print("0 - Sair")
    return int(input("Digite sua opção: "))


'''
Essa é a função verificar ela vai pedir ao usúario qual a vaga que ele quer estacionar
e Vai verificar se o número é maior ou igual a ha 1 pois não a vagas com números menores
depois vai verificar se a vaga desejada está criada se não vai criar até chegar nessa vaga e vai devolver 
a posição dessa vaga para ser utilizada.
'''
def verifcar():
    while True:
        vaga_desejada = int(input("Digite o número da vaga que quer estacionar: "))
        if(vaga_desejada >= 1):
            if(len(vagas) < vaga_desejada):
                for _ in range(vaga_desejada - len(vagas)):
                    vagas.append({"carro":"","ocupado":False})
            return vaga_desejada - 1

        else:
            print("O número da vaga deve ser maior que 0!")

'''
A função estacionar vai precisar da variavel que foi retornada da função verificar e então vai 
verificar se a vaga está ocupada se estiver vai avisar o usúario que hava um veículo nessa vaga e se não
estiver ocupada vai pedir as informaçoes desse veículo e vai guardar no vetor em sua vaga desejada.
'''
def estacinar(vaga):
    if(vagas[vaga]['ocupado'] == False):
        carro = {}
        carro["placa"] = input("Digite a placa do veiculo: ")
        carro["marca"] = input("Digite a marca do veiculo: ")
        carro["modelo"] = input("Digite o modelo do veiculo: ")
        carro["cor"] = input("Digite a cor do veiculo: ")
        carro["proprietario"] = input("Digite o proprietario do veiculo: ")
        vagas[vaga]['carro'] = carro
        vagas[vaga]['ocupado'] = True

    else:
        print(f"Ha um veiculo estacionado na vaga {vaga+1}")
    
    input("Aperte a tecla ENTER para continuar: ")


'''
Ja na função remover vai ser pedido a placa do veículo e vai ser verificado cada uma das posiçoes do 
vetor e ver se a vaga estiver ocupada, se estiver vai verificar a placa do carro que está naquela vaga
e se bater com o placa que o usúario digitou vai liberar a vaga.
'''
def remover():
    placa = input("Qual a placa do veículo: ")
    encontrou = False
    for i in range(len(vagas)):
        if(vagas[i]['ocupado'] == True):
           if(vagas[i]['carro']['placa'] == placa):
               vagas[i]['carro'] = ""
               vagas[i]['ocupado'] = False
               encontrou = True
    if(encontrou == True):
        print(f"Veículo de placa {placa} desocupou a vaga!")

    else:
        print(f"Veículo de placa {placa} não foi encontrado!")

    input("Aperte a tecla ENTER para continuar: ")

            
'''
Na função lista vai passar por todas as posiçoes do vetor vagas e vai verificar se aquela vaga está ocupada,
se estiver ocupada vai imprimir ao usúario as caracteristicas do veículo e a vaga onde está.
'''
def lista():
    quantidade = 0
    print("Carros estacionados:")
    for i in range(len(vagas)):
        if(vagas[i]['ocupado'] == True):
            print(f"---------------------------")
            print(f"placa: {vagas[i]['carro']['placa']}")
            print(f"marca: {vagas[i]['carro']['marca']}")
            print(f"modelo: {vagas[i]['carro']['modelo']}")
            print(f"cor: {vagas[i]['carro']['cor']}")
            print(f"propríetario: {vagas[i]['carro']['proprietario']}")
            print(f"VAGA: {i+1}")
            quantidade += 1

    if(quantidade == 0):
        print("Nenhum veículo encontrado!")

    print("")
    input("Aperte a tecla ENTER para continuar: ")


'''
Na função conferir o usúario vai ser requisitado pedindo qual a placa do veículo e o programa vai passar
por todas as posiçoes do vetor vagas e vai verificar se está ocupada se estiver vai verificar se a placa e
a placa fornecida são iguais o programa vai dizer que o veiculo está estacionado
'''
def conferir():
    placa = input("Digite a placa do carro que você que encontrar: ")
    encontrado = False
    vaga_ocupada = -1
    for i in range(len(vagas)):
        if(vagas[i]["ocupado"] == True):
            if(vagas[i]["carro"]["placa"] == placa):
                encontrado = True
                vaga_ocupada = i+1

    if(encontrado == True):
        print(f"Veiculo estacionado na vaga N°{vaga_ocupada}")

    else:
        print("Veiculo não encontrado")
    
    input("Aperte a tecla ENTER para continuar: ")


'''
essa é a estrutura principal e se o usúario digitar 0 no menu ele vai fechar o programa!
'''
while True:
    opcao = menu()

    match opcao:

        case 0:
            break

        case 1:
            estacinar(verifcar())

        case 2:
            remover()

        case 3:
            lista()

        case 4:
            conferir()

            
print("Fechando Aplicação!")
