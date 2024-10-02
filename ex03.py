def adicionar_pedido(pedidos):
    nome_cliente = input("Digite o nome do cliente: ").capitalize()
    nome_prato = input("Digite o nome do prato que deseja adicionar: ").capitalize()

    # Verificar se o cliente já está no dicionário de pedidos
    if nome_cliente in pedidos:
        pedidos[nome_cliente].append(nome_prato)
    else:
        pedidos[nome_cliente] = [nome_prato]

    print(f"Prato '{nome_prato}' adicionado ao pedido do cliente {nome_cliente}.")

def atualizar_pedido(pedidos):
    nome_cliente = input("Digite o nome do cliente: ").capitalize()
    if nome_cliente in pedidos:
        nome_prato_atual = input("Digite o nome do prato que deseja substituir: ").capitalize()
        if nome_prato_atual in pedidos[nome_cliente]:
            novo_prato = input("Digite o nome do novo prato: ").capitalize()
            # Substituir o prato
            index = pedidos[nome_cliente].index(nome_prato_atual)
            pedidos[nome_cliente][index] = novo_prato
            print(f"Prato '{nome_prato_atual}' substituído por '{novo_prato}' para o cliente {nome_cliente}.")
        else:
            print(f"Erro: O prato '{nome_prato_atual}' não está cadastrado para o cliente {nome_cliente}.")
    else:
        print(f"Erro: Cliente '{nome_cliente}' não encontrado.")

def remover_pedido(pedidos):
    nome_cliente = input("Digite o nome do cliente: ").capitalize()
    if nome_cliente in pedidos:
        nome_prato = input("Digite o nome do prato que deseja remover: ").capitalize()
        if nome_prato in pedidos[nome_cliente]:
            pedidos[nome_cliente].remove(nome_prato)
            print(f"Prato '{nome_prato}' removido do pedido do cliente {nome_cliente}.")
        else:
            print(f"Erro: O prato '{nome_prato}' não está cadastrado para o cliente {nome_cliente}.")
    else:
        print(f"Erro: Cliente '{nome_cliente}' não encontrado.")
def filtrarpedidosporcliente(pedidos):
    nomecliente = input("Digite o nome do cliente para ver os pedidos: ").capitalize()
    if nome_cliente in pedidos:
        print(f"Pedidos do cliente {nome_cliente}: {', '.join(pedidos[nome_cliente])}")
    else:
        print(f"Erro: Cliente '{nome_cliente}' não encontrado.")

def visualizar_todos_os_pedidos(pedidos):
    if pedidos:
        print("Lista de todos os pedidos:")
        for cliente, pratos in sorted(pedidos.items()):
            print(f"Cliente: {cliente}, Pratos: {', '.join(pratos)}")
    else:
        print("Nenhum pedido cadastrado no sistema.")

def main():
    pedidos = {}
    while True:
        print("\nMenu do Sistema de Controle de Pedidos")
        print("1. Adicionar Pedido")
        print("2. Atualizar Pedido")
        print("3. Remover Pedido")
        print("4. Filtrar Pedidos por Cliente")
        print("5. Visualizar Todos os Pedidos")
        print("6. Encerrar")

        opcao = input("Escolha uma opção (1-6): ")

        if opcao == '1':
            adicionar_pedido(pedidos)
        elif opcao == '2':
            atualizar_pedido(pedidos)
        elif opcao == '3':
            remover_pedido(pedidos)
        elif opcao == '4':
            filtrar_pedidos_por_cliente(pedidos)
        elif opcao == '5':
            visualizar_todos_os_pedidos(pedidos)
        elif opcao == '6':
            print("Encerrando o sistema. Obrigado e volte sempre!")
            break
        else:
            print("Opção inválida, tente novamente.")