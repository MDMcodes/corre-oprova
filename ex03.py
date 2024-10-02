# Função para adicionar um pedido
def adicionar_pedido(pedidos):
    # Pede o nome do cliente e capitaliza a primeira letra
    nome_cliente = input("Digite o nome do cliente: ").capitalize()
    # Pede o nome do prato e capitaliza a primeira letra
    nome_prato = input("Digite o nome do prato que deseja adicionar: ").capitalize()

    # Verifica se o cliente já está no dicionário de pedidos
    if nome_cliente in pedidos:
        # Se sim, adiciona o prato à lista de pedidos do cliente
        pedidos[nome_cliente].append(nome_prato)
    else:
        # Se não, cria uma nova lista de pedidos para o cliente
        pedidos[nome_cliente] = [nome_prato]

    # Mostra uma mensagem de confirmação
    print(f"Prato '{nome_prato}' adicionado ao pedido do cliente {nome_cliente}.")

# Função para atualizar um pedido
def atualizar_pedido(pedidos):
    # Pede o nome do cliente e capitaliza a primeira letra
    nome_cliente = input("Digite o nome do cliente: ").capitalize()
    if nome_cliente in pedidos:
        # Pede o nome do prato que deseja substituir e capitaliza a primeira letra
        nome_prato_atual = input("Digite o nome do prato que deseja substituir: ").capitalize()
        if nome_prato_atual in pedidos[nome_cliente]:
            # Pede o nome do novo prato e capitaliza a primeira letra
            novo_prato = input("Digite o nome do novo prato: ").capitalize()
            # Substitui o prato na lista de pedidos do cliente
            index = pedidos[nome_cliente].index(nome_prato_atual)
            pedidos[nome_cliente][index] = novo_prato
            # Mostra uma mensagem de confirmação
            print(f"Prato '{nome_prato_atual}' substituído por '{novo_prato}' para o cliente {nome_cliente}.")
        else:
            # Mostra um erro se o prato não está cadastrado para o cliente
            print(f"Erro: O prato '{nome_prato_atual}' não está cadastrado para o cliente {nome_cliente}.")
    else:
        # Mostra um erro se o cliente não está cadastrado
        print(f"Erro: Cliente '{nome_cliente}' não encontrado.")

# Função para remover um pedido
def remover_pedido(pedidos):
    # Pede o nome do cliente e capitaliza a primeira letra
    nome_cliente = input("Digite o nome do cliente: ").capitalize()
    if nome_cliente in pedidos:
        # Pede o nome do prato que deseja remover e capitaliza a primeira letra
        nome_prato = input("Digite o nome do prato que deseja remover: ").capitalize()
        if nome_prato in pedidos[nome_cliente]:
            # Remove o prato da lista de pedidos do cliente
            pedidos[nome_cliente].remove(nome_prato)
            # Mostra uma mensagem de confirmação
            print(f"Prato '{nome_prato}' removido do pedido do cliente {nome_cliente}.")
        else:
            # Mostra um erro se o prato não está cadastrado para o cliente
            print(f"Erro: O prato '{nome_prato}' não está cadastrado para o cliente {nome_cliente}.")
    else:
        # Mostra um erro se o cliente não está cadastrado
        print(f"Erro: Cliente '{nome_cliente}' não encontrado.")

# Função para filtrar pedidos por cliente
def filtrar_pedidos_por_cliente(pedidos):
    # Pede o nome do cliente e capitaliza a primeira letra
    nome_cliente = input("Digite o nome do cliente para ver os pedidos: ").capitalize()
    if nome_cliente in pedidos:
        # Mostra os pedidos do cliente
        print(f"Pedidos do cliente {nome_cliente}: {', '.join(pedidos[nome_cliente])}")
    else:
        # Mostra um erro se o cliente não está cadastrado
        print(f"Erro: Cliente '{nome_cliente}' não encontrado.")

# Função para visualizar todos os pedidos
def visualizar_todos_os_pedidos(pedidos):
    if pedidos:
        # Mostra a lista de todos os pedidos
        print("Lista de todos os pedidos")

#fiquei sem tempo pra terminar esse exercicio, n vou mentir que 50% dele foi cópia da net, e que eu entendi bem mais ou menos