def adicionar_tarefa(tarefas, nome_tarefa):
    tarefa = {"tarefa": nome_tarefa, "completada": False}
    tarefas.append(tarefa)
    print(f"Tarefa '{nome_tarefa}' adicionada com sucesso!")


def listar_tarefas(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
        return
    for tarefa in tarefas:
        print(f"Tarefa: {tarefa['tarefa']} - Completada: {tarefa['completada']}")


def atualizar_tarefa(tarefas, nome_tarefa, novo_nome_tarefa):
    for tarefa in tarefas:
        if tarefa["tarefa"] == nome_tarefa:
            tarefa["tarefa"] = novo_nome_tarefa
            print(f"Tarefa '{nome_tarefa}' atualizada para '{novo_nome_tarefa}'")
            return
    print(f"Tarefa '{nome_tarefa}' não encontrada")


def completar_tarefa(tarefas, nome_tarefa):
    for tarefa in tarefas:
        if tarefa["tarefa"] == nome_tarefa:
            tarefa["completada"] = True
            print(f"Tarefa '{nome_tarefa}' completada")
            return
    print(f"Tarefa '{nome_tarefa}' não encontrada")


def deletar_tarefas_completadas(tarefas):
    tarefas[:] = [tarefa for tarefa in tarefas if not tarefa["completada"]]
    print("Tarefas completadas deletadas")


tarefas = []
while True:
    print("\nMenu do Gerenciador de Tarefas")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Atualizar tarefa")
    print("4 - Completar tarefa")
    print("5 - Deletar tarefas completadas")
    print("6 - Sair")

    escolha = input("Escolha uma opção: ")

    if escolha == "1":
        nome_tarefa = input("Digite o nome da tarefa: ")
        adicionar_tarefa(tarefas, nome_tarefa)
    elif escolha == "2":
        listar_tarefas(tarefas)
    elif escolha == "3":
        listar_tarefas(tarefas)
        nome_tarefa = input("Digite o nome da tarefa que deseja atualizar: ")
        novo_nome_tarefa = input("Digite o novo nome da tarefa: ")
        atualizar_tarefa(tarefas, nome_tarefa, novo_nome_tarefa)
    elif escolha == "4":
        listar_tarefas(tarefas)
        nome_tarefa = input("Digite o nome da tarefa que deseja completar: ")
        completar_tarefa(tarefas, nome_tarefa)
    elif escolha == "5":
        deletar_tarefas_completadas(tarefas)
        listar_tarefas(tarefas)
    elif escolha == "6":
        print("Programa finalizado")
        break
    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
