import queue

# Estruturas de dados do sistema

frota = []

fila_caminhoes = queue.Queue()

pilha_conteineres = []

rotas = {}


# FUNÇÃO PARA CADASTRAR VEICULOS

def cadastrar_veiculo():

    print("\n--- CADASTRO DE VEICULO ---")

    id_veiculo = int(input("Informe o ID do veiculo: "))

    # VERIFICAR SE O ID JA EXISTE
    for veiculo in frota:
        if veiculo[0] == id_veiculo:
            print("\nErro: ja existe um veiculo com esse ID!")
            return

    placa = input("Informe a placa: ")
    modelo = input("Informe o modelo: ")
    transportadora = input("Informe a transportadora: ")
    motorista = input("Informe o nome do motorista: ")

    veiculo = [id_veiculo, placa, modelo, transportadora, motorista]

    frota.append(veiculo)

    print("\nVeiculo cadastrado com sucesso!")


# FUNÇÃO PARA LISTAR VEICULOS

def listar_veiculos():

    print("\n--- VEICULOS CADASTRADOS ---")

    if len(frota) == 0:
        print("Nenhum veiculo cadastrado.")

    else:
        for veiculo in frota:

            print("\nID:", veiculo[0])
            print("Placa:", veiculo[1])
            print("Modelo:", veiculo[2])
            print("Transportadora:", veiculo[3])
            print("Motorista:", veiculo[4])


# FUNÇÃO PARA CONSULTAR VEICULO PELO ID

def consultar_veiculo():

    print("\n--- CONSULTAR VEICULO ---")

    id_busca = int(input("Informe o ID do veiculo: "))

    encontrado = False

    for veiculo in frota:

        if veiculo[0] == id_busca:

            print("\nVeiculo encontrado!")
            print("ID:", veiculo[0])
            print("Placa:", veiculo[1])
            print("Modelo:", veiculo[2])
            print("Transportadora:", veiculo[3])
            print("Motorista:", veiculo[4])

            encontrado = True

    if encontrado == False:
        print("\nVeiculo nao encontrado.")


# FUNÇÃO PARA ATUALIZAR VEICULO

def atualizar_veiculo():

    print("\n--- ATUALIZAR VEICULO ---")

    id_busca = int(input("Informe o ID do veiculo: "))

    encontrado = False

    for veiculo in frota:

        if veiculo[0] == id_busca:

            print("\nVeiculo encontrado!")
            print("Informe os novos dados:")

            veiculo[1] = input("Nova placa: ")
            veiculo[2] = input("Novo modelo: ")
            veiculo[3] = input("Nova transportadora: ")
            veiculo[4] = input("Novo motorista: ")

            print("\nVeiculo atualizado com sucesso!")

            encontrado = True

    if encontrado == False:
        print("\nVeiculo nao encontrado.")


# FUNÇÃO PARA EXCLUIR VEICULO

def excluir_veiculo():

    print("\n--- EXCLUIR VEICULO ---")

    id_busca = int(input("Informe o ID do veiculo: "))

    encontrado = False

    for veiculo in frota:

        if veiculo[0] == id_busca:

            frota.remove(veiculo)

            print("\nVeiculo excluido com sucesso!")

            encontrado = True

            break

    if encontrado == False:
        print("\nVeiculo nao encontrado.")


# FUNÇÃO PARA CADASTRAR CAMINHAO NA FILA

def cadastrar_caminhao():

    print("\n--- CADASTRO DE CAMINHAO NA FILA ---")

    id_caminhao = int(input("Informe o ID do caminhao: "))

    # VERIFICAR SE O ID JA EXISTE
    quantidade = fila_caminhoes.qsize()

    for i in range(quantidade):
        caminhao = fila_caminhoes.get()

        if caminhao[0] == id_caminhao:
            fila_caminhoes.put(caminhao)

            # RESTAURAR OS CAMINHOES RESTANTES
            for j in range(i + 1, quantidade):
                caminhao = fila_caminhoes.get()
                fila_caminhoes.put(caminhao)

            print("\nErro: ja existe um caminhao com esse ID!")
            return

        fila_caminhoes.put(caminhao)

    placa = input("Informe a placa: ")
    transportadora = input("Informe a transportadora: ")
    motorista = input("Informe o nome do motorista: ")

    caminhao = [id_caminhao, placa, transportadora, motorista]

    fila_caminhoes.put(caminhao)

    print("\nCaminhao adicionado a fila com sucesso!")


# FUNÇÃO PARA CONSULTAR A FILA

def consultar_fila():

    print("\n--- SITUACAO DA FILA ---")

    quantidade = fila_caminhoes.qsize()

    print("Caminhoes aguardando:", quantidade)

    print("Fila vazia:", fila_caminhoes.empty())


# FUNÇÃO PARA ATENDER CAMINHAO

def atender_caminhao():

    print("\n--- ATENDIMENTO DE CAMINHAO ---")

    if fila_caminhoes.empty():

        print("Nao existem caminhoes aguardando atendimento.")

    else:

        caminhao = fila_caminhoes.get()

        print("\nCaminhao atendido com sucesso!")
        print("ID:", caminhao[0])
        print("Placa:", caminhao[1])
        print("Transportadora:", caminhao[2])
        print("Motorista:", caminhao[3])


# FUNÇÃO PARA LISTAR CAMINHÕES NA FILA

def listar_fila():

    print("\n--- CAMINHOES AGUARDANDO ATENDIMENTO ---")

    if fila_caminhoes.empty():

        print("A fila esta vazia.")

    else:

        quantidade = fila_caminhoes.qsize()

        contador = 0

        while contador < quantidade:

            caminhao = fila_caminhoes.get()

            print("\nID:", caminhao[0])
            print("Placa:", caminhao[1])
            print("Transportadora:", caminhao[2])
            print("Motorista:", caminhao[3])

            fila_caminhoes.put(caminhao)

            contador = contador + 1


# FUNÇÃO PARA ATUALIZAR CAMINHAO NA FILA

def atualizar_caminhao():

    print("\n--- ATUALIZAR CAMINHAO ---")

    id_busca = int(input("Informe o ID do caminhao: "))

    encontrado = False

    quantidade = fila_caminhoes.qsize()

    contador = 0

    while contador < quantidade:

        caminhao = fila_caminhoes.get()

        if caminhao[0] == id_busca:

            print("\nCaminhao encontrado!")
            print("Informe os novos dados:")

            caminhao[1] = input("Nova placa: ")
            caminhao[2] = input("Nova transportadora: ")
            caminhao[3] = input("Novo motorista: ")

            print("\nCaminhao atualizado com sucesso!")

            encontrado = True

        fila_caminhoes.put(caminhao)

        contador = contador + 1

    if encontrado == False:

        print("\nCaminhao nao encontrado.")


# FUNÇÃO PARA EXCLUIR CAMINHAO DA FILA

def excluir_caminhao():

    print("\n--- EXCLUIR CAMINHAO DA FILA ---")

    id_busca = int(input("Informe o ID do caminhao: "))

    encontrado = False

    quantidade = fila_caminhoes.qsize()

    contador = 0

    while contador < quantidade:

        caminhao = fila_caminhoes.get()

        if caminhao[0] == id_busca:

            print("\nCaminhao excluido da fila com sucesso!")

            encontrado = True

        else:

            fila_caminhoes.put(caminhao)

        contador = contador + 1

    if encontrado == False:

        print("\nCaminhao nao encontrado.")


# FUNÇÃO PARA CADASTRAR CONTEINER

def cadastrar_conteiner():

    print("\n--- CADASTRO DE CONTEINER ---")

    id_conteiner = int(input("Informe o ID do conteiner: "))

    # VERIFICAR SE O ID JA EXISTE
    for conteiner in pilha_conteineres:
        if conteiner[0] == id_conteiner:
            print("\nErro: ja existe um conteiner com esse ID!")
            return

    codigo = input("Informe o codigo do conteiner: ")
    tipo = input("Informe o tipo do conteiner: ")
    destino = input("Informe o destino: ")

    conteiner = [id_conteiner, codigo, tipo, destino]

    pilha_conteineres.append(conteiner)

    print("\nConteiner adicionado a pilha com sucesso!")


# FUNÇÃO PARA CONSULTAR A PILHA

def consultar_pilha():

    print("\n--- SITUACAO DA PILHA ---")

    print("Conteineres armazenados:", len(pilha_conteineres))

    if len(pilha_conteineres) == 0:

        print("A pilha esta vazia.")

    else:

        print("ID do conteiner no topo:", pilha_conteineres[-1][0])


# FUNÇÃO PARA LISTAR CONTEINERES

def listar_conteineres():

    print("\n--- CONTEINERES NA PILHA ---")

    if len(pilha_conteineres) == 0:

        print("A pilha esta vazia.")

    else:

        contador = len(pilha_conteineres) - 1

        while contador >= 0:

            conteiner = pilha_conteineres[contador]

            print("\nID:", conteiner[0])
            print("Codigo:", conteiner[1])
            print("Tipo:", conteiner[2])
            print("Destino:", conteiner[3])

            contador = contador - 1


# FUNÇÃO PARA RETIRAR CONTEINER DO TOPO

def retirar_conteiner():

    print("\n--- RETIRAR CONTEINER ---")

    if len(pilha_conteineres) == 0:

        print("A pilha esta vazia. Nao ha conteineres para retirar.")

    else:

        conteiner = pilha_conteineres.pop()

        print("\nConteiner retirado com sucesso!")
        print("ID:", conteiner[0])
        print("Codigo:", conteiner[1])
        print("Tipo:", conteiner[2])
        print("Destino:", conteiner[3])

# FUNÇÃO PARA ATUALIZAR CONTEINER DO TOPO

def atualizar_conteiner():

    print("\n--- ATUALIZAR CONTEINER ---")

    if len(pilha_conteineres) == 0:

        print("A pilha esta vazia.")

    else:

        conteiner = pilha_conteineres[-1]

        print("\nConteiner no topo encontrado!")
        print("Informe os novos dados:")

        conteiner[1] = input("Novo codigo: ")
        conteiner[2] = input("Novo tipo: ")
        conteiner[3] = input("Novo destino: ")

        print("\nConteiner atualizado com sucesso!")

# FUNÇÃO PARA EXCLUIR CONTEINER PELO ID

def excluir_conteiner():

    print("\n--- EXCLUIR CONTEINER ---")

    id_busca = int(input("Informe o ID do conteiner: "))

    encontrado = False

    quantidade = len(pilha_conteineres)

    contador = 0

    while contador < quantidade:

        conteiner = pilha_conteineres.pop()

        if conteiner[0] == id_busca:

            print("\nConteiner excluido com sucesso!")

            encontrado = True

        else:

            pilha_conteineres.insert(0, conteiner)

        contador = contador + 1

    if encontrado == False:

        print("\nConteiner nao encontrado.")



# FUNÇÃO PARA CADASTRAR ROTA NA ARVORE

def cadastrar_rota():

    print("\n--- CADASTRO DE ROTA ---")

    porto = input("Informe o nome do porto: ").strip()

    # VERIFICAR SE O PORTO JA EXISTE
    resultado = localizar_porto(rotas, porto)

    if resultado is not None:
        print("\nErro: esse porto ja esta cadastrado na arvore!")
        return

    porto_pai = input("Informe o porto de origem (ou deixe vazio para raiz): ").strip()

    if porto_pai == "":

        if len(rotas) == 0:

            rotas[porto] = {}

            print("\nPorto raiz cadastrado com sucesso!")

        else:

            print("\nA arvore ja possui uma raiz.")

    else:

        pai = localizar_porto(rotas, porto_pai)

        if pai is not None:

            pai[porto] = {}

            print("\nRota cadastrada com sucesso!")

        else:

            print("\nPorto de origem nao encontrado.")



# FUNÇÃO PARA LOCALIZAR PORTO NA ARVORE

def localizar_porto(arvore, nome_porto):

    for porto, filhos in arvore.items():

        if porto == nome_porto:

            return filhos

        resultado = localizar_porto(filhos, nome_porto)

        if resultado is not None:

            return resultado

    return None


# FUNÇÃO PARA LISTAR AS ROTAS

def listar_rotas(arvore, nivel=0):

    for porto, filhos in arvore.items():

        print("    " * nivel + "- " + porto)

        listar_rotas(filhos, nivel + 1)


# FUNÇÃO PARA CONSULTAR UM PORTO

def consultar_rota():

    print("\n--- CONSULTA DE ROTA ---")

    nome_porto = input("Informe o nome do porto: ")

    resultado = localizar_porto(rotas, nome_porto)

    if resultado is not None:

        print("\nPorto encontrado:", nome_porto)

        if len(resultado) > 0:

            print("Portos ligados a ele:")

            listar_rotas(resultado, 1)

        else:

            print("Este porto nao possui outros portos ligados a ele.")

    else:

        print("\nPorto nao encontrado.")


# FUNÇÃO PARA ATUALIZAR UMA ROTA

def atualizar_rota():

    print("\n--- ATUALIZACAO DE ROTA ---")

    nome_antigo = input("Informe o nome atual do porto: ").strip()

    novo_nome = input("Informe o novo nome do porto: ").strip()

    # VERIFICAR SE O PORTO ATUAL EXISTE
    resultado = localizar_porto(rotas, nome_antigo)

    if resultado is None:
        print("\nPorto nao encontrado.")
        return

    # VERIFICAR SE O NOVO NOME JA EXISTE
    resultado = localizar_porto(rotas, novo_nome)

    if resultado is not None:
        if novo_nome == nome_antigo:
            print("\nO novo nome e igual ao nome atual.")
        else:
            print("\nErro: ja existe um porto com esse nome!")
        return

    # ATUALIZAR PORTO RAIZ
    if nome_antigo in rotas:

        rotas[novo_nome] = rotas[nome_antigo]

        del rotas[nome_antigo]

        print("\nPorto atualizado com sucesso!")

        return

    # ATUALIZAR PORTO EM OUTRO NIVEL
    pai = localizar_pai(rotas, nome_antigo)

    if pai is not None:

        pai[novo_nome] = pai[nome_antigo]

        del pai[nome_antigo]

        print("\nPorto atualizado com sucesso!")

    else:

        print("\nPorto nao encontrado.")


# FUNÇÃO PARA LOCALIZAR O PAI DE UM PORTO

def localizar_pai(arvore, nome_porto):

    for porto, filhos in arvore.items():

        if nome_porto in filhos:

            return filhos

        resultado = localizar_pai(filhos, nome_porto)

        if resultado is not None:

            return resultado

    return None


# FUNÇÃO PARA EXCLUIR UMA ROTA

def excluir_rota():

    print("\n--- EXCLUSAO DE ROTA ---")

    nome_porto = input("Informe o nome do porto que deseja excluir: ").strip()

    pai = localizar_pai(rotas, nome_porto)

    if pai is not None:

        del pai[nome_porto]

        print("\nPorto e suas rotas seguintes excluidos com sucesso!")

    elif nome_porto in rotas:

        del rotas[nome_porto]

        print("\nPorto raiz e toda sua hierarquia excluidos com sucesso!")

    else:

        print("\nPorto nao encontrado.")


# FUNÇÃO PARA SALVAR OS DADOS

def salvar_dados():

    arquivo = open("dados_sistema.txt", "w")

    # SALVAR A FROTA

    for veiculo in frota:

        linha = "LISTA|" + str(veiculo[0]) + "|" + veiculo[1] + "|" + veiculo[2] + "|" + veiculo[3] + "|" + veiculo[4] + "\n"

        arquivo.write(linha)

    # SALVAR A FILA DE CAMINHOES

    quantidade = fila_caminhoes.qsize()

    for i in range(quantidade):

        caminhao = fila_caminhoes.get()

        linha = "FILA|" + str(caminhao[0]) + "|" + caminhao[1] + "|" + caminhao[2] + "|" + caminhao[3] + "\n"

        arquivo.write(linha)

        fila_caminhoes.put(caminhao)


    # SALVAR A PILHA DE CONTEINERES

    for conteiner in pilha_conteineres:

        linha = "PILHA|" + str(conteiner[0]) + "|" + conteiner[1] + "|" + conteiner[2] + "|" + conteiner[3] + "\n"

        arquivo.write(linha)

    salvar_arvore(rotas, arquivo)

    arquivo.close()

    print("\nDados salvos com sucesso!")


# FUNÇÃO PARA SALVAR A ARVORE DE ROTAS

def salvar_arvore(arvore, arquivo, caminho=""):

    for porto, filhos in arvore.items():

        if caminho == "":

            novo_caminho = porto

        else:

            novo_caminho = caminho + "|" + porto

        if len(filhos) == 0:

            linha = "ARVORE|" + novo_caminho + "\n"

            arquivo.write(linha)

        else:

            salvar_arvore(filhos, arquivo, novo_caminho)


# FUNÇÃO PARA CARREGAR A ARVORE DE ROTAS

def carregar_arvore(dados):

    arvore = rotas

    for i in range(1, len(dados)):

        porto = dados[i]

        if porto not in arvore:

            arvore[porto] = {}

        arvore = arvore[porto]


# FUNÇÃO PARA CARREGAR OS DADOS

def carregar_dados():

    global fila_caminhoes

    frota.clear()

    fila_caminhoes = queue.Queue()

    pilha_conteineres.clear()

    rotas.clear()

    arquivo = open("dados_sistema.txt", "r")

    for linha in arquivo:

        dados = linha.strip().split("|")

        if dados[0] == "LISTA":

            veiculo = [int(dados[1]), dados[2], dados[3], dados[4], dados[5]]

            frota.append(veiculo)

        elif dados[0] == "FILA":

            caminhao = [int(dados[1]), dados[2], dados[3], dados[4]]

            fila_caminhoes.put(caminhao)

        elif dados[0] == "PILHA":

            conteiner = [int(dados[1]), dados[2], dados[3], dados[4]]

            pilha_conteineres.append(conteiner)

        elif dados[0] == "ARVORE":

            carregar_arvore(dados)


    arquivo.close()

    print("\nDados carregados com sucesso!")


# SUBMENU DA FROTA DE VEICULOS

def menu_frota():

    opcao = 0

    while opcao != 6:

        print("\n================================")
        print(" GERENCIAMENTO DA FROTA")
        print("================================")

        print("1 - Cadastrar veiculo")
        print("2 - Listar veiculos")
        print("3 - Consultar veiculo")
        print("4 - Atualizar veiculo")
        print("5 - Excluir veiculo")
        print("6 - Voltar ao menu principal")

        opcao = int(input("\nEscolha uma opcao: "))

        if opcao == 1:
            cadastrar_veiculo()
        elif opcao == 2:
            listar_veiculos()
        elif opcao == 3:
            consultar_veiculo()
        elif opcao == 4:
            atualizar_veiculo()
        elif opcao == 5:
            excluir_veiculo()
        elif opcao == 6:
            print("\nVoltando ao menu principal...")
        else:
            print("\nOpcao invalida!")


# SUBMENU DA FILA DE CAMINHOES

def menu_fila():

    opcao = 0

    while opcao != 7:

        print("\n================================")
        print(" GERENCIAMENTO DA FILA")
        print("================================")

        print("1 - Cadastrar caminhao na fila")
        print("2 - Listar caminhoes na fila")
        print("3 - Consultar fila")
        print("4 - Atualizar caminhao")
        print("5 - Excluir caminhao")
        print("6 - Atender caminhao")
        print("7 - Voltar ao menu principal")

        opcao = int(input("\nEscolha uma opcao: "))

        if opcao == 1:
            cadastrar_caminhao()
        elif opcao == 2:
            listar_fila()
        elif opcao == 3:
            consultar_fila()
        elif opcao == 4:
            atualizar_caminhao()
        elif opcao == 5:
            excluir_caminhao()
        elif opcao == 6:
            atender_caminhao()
        elif opcao == 7:
            print("\nVoltando ao menu principal...")
        else:
            print("\nOpcao invalida!")


# SUBMENU DA PILHA DE CONTEINERES

def menu_pilha():
    opcao = 0
    while opcao != 7:
        print("\n================================")
        print(" GERENCIAMENTO DA PILHA")
        print("================================")
        print("1 - Cadastrar conteiner")
        print("2 - Listar conteineres")
        print("3 - Consultar pilha")
        print("4 - Atualizar conteiner do topo")
        print("5 - Excluir conteiner")
        print("6 - Retirar conteiner")
        print("7 - Voltar ao menu principal")

        opcao = int(input("\nEscolha uma opcao: "))

        if opcao == 1:
            cadastrar_conteiner()
        elif opcao == 2:
            listar_conteineres()
        elif opcao == 3:
            consultar_pilha()
        elif opcao == 4:
            atualizar_conteiner()
        elif opcao == 5:
            excluir_conteiner()
        elif opcao == 6:
            retirar_conteiner()
        elif opcao == 7:
            print("\nVoltando ao menu principal...")
        else:
            print("\nOpcao invalida!")


# SUBMENU DA ÁRVORE DE ROTAS

def menu_arvore():

    opcao = 0

    while opcao != 6:

        print("\n================================")
        print(" GERENCIAMENTO DA ARVORE DE ROTAS")
        print("================================")

        print("1 - Cadastrar rota")
        print("2 - Listar rotas")
        print("3 - Consultar rota")
        print("4 - Atualizar rota")
        print("5 - Excluir rota")
        print("6 - Voltar ao menu principal")

        opcao = int(input("\nEscolha uma opcao: "))

        if opcao == 1:
            cadastrar_rota()
        elif opcao == 2:
            print("\n--- ROTAS CADASTRADAS ---")

            if len(rotas) == 0:
                print("\nNenhuma rota cadastrada.")
            else:
                listar_rotas(rotas)
        elif opcao == 3:
            consultar_rota()
        elif opcao == 4:
            atualizar_rota()
        elif opcao == 5:
            excluir_rota()
        elif opcao == 6:
            print("\nVoltando ao menu principal...")
        else:
            print("\nOpcao invalida!")


# FUNÇÃO DO MENU PRINCIPAL

def menu_principal():

    opcao = 0

    while opcao != 7:

        print("\n================================")
        print(" SISTEMA DE LOGISTICA PORTUARIA")
        print("================================")

        print("1 - Gerenciar frota de veiculos")
        print("2 - Gerenciar fila de caminhoes")
        print("3 - Gerenciar pilha de conteineres")
        print("4 - Gerenciar arvore de rotas")
        print("5 - Salvar dados")
        print("6 - Carregar Dados")
        print("7 - Sair")

        opcao = int(input("\nEscolha uma opcao: "))

        if opcao == 1:
            
            menu_frota()

        elif opcao == 2:

            menu_fila()

        elif opcao == 3:

            menu_pilha()

        elif opcao == 4:

            menu_arvore()

        elif opcao == 5:

            salvar_dados()

        elif opcao == 6:

            carregar_dados()
        
        elif opcao == 7:

            print("\nEncerrando o sistema...")

        else:

            print("\nOpcao invalida!")

menu_principal()