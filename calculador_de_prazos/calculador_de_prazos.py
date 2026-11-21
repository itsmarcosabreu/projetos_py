#Variáveis das listas que vão guardar as tarefas cadastradas
nomes = []
dias = []
concluidas = []
status_lista = []

#Nome do arquivo onde as tarefas ficam salvas
arquivo_tarefas = "tarefas.txt"


#Função que define o status da tarefa
def definir_status(concluida, dias_restantes):
    if concluida:
        return "Concluída"
    elif dias_restantes < 0:
        return "ATRASADA"
    elif dias_restantes <= 2:
        return "Urgente"
    else:
        return "Em dia"


#Função que pede um número inteiro e repete até o usuário digitar certo
def ler_numero(mensagem):
    while True:
        try:
            numero = int(input(mensagem))
            return numero
        except ValueError:
            print("Entrada inválida! Digite um número inteiro.")


#Função que salva as tarefas no arquivo (uma tarefa por linha)
def salvar_tarefas():
    try:
        arquivo = open(arquivo_tarefas, "w", encoding="utf-8")
        for i in range(len(nomes)):
            arquivo.write(f"{nomes[i]};{dias[i]};{concluidas[i]}\n")
        arquivo.close()
    except OSError:
        print("Não foi possível salvar as tarefas no arquivo.")


#Função que carrega as tarefas do arquivo quando o programa abre
def carregar_tarefas():
    try:
        arquivo = open(arquivo_tarefas, "r", encoding="utf-8")
    except FileNotFoundError:
        # Ainda não existe arquivo, então começa com a lista vazia
        return

    for linha in arquivo:
        try:
            nome, dias_restantes, concluida = linha.strip().split(";")
            dias_restantes = int(dias_restantes)
            concluida = concluida == "True"
        except ValueError:
            print("Linha inválida no arquivo, ela foi ignorada.")
            continue

        nomes.append(nome)
        dias.append(dias_restantes)
        concluidas.append(concluida)
        status_lista.append(definir_status(concluida, dias_restantes))

    arquivo.close()
    print(f"{len(nomes)} tarefa(s) carregada(s) do arquivo.")


# Função do cadastro das tarefas
def cadastrar_tarefas():
    quantidade = 0
    while quantidade <= 0:
        quantidade = ler_numero("Quantas tarefas você quer cadastrar? ")
        if quantidade <= 0:
            print("Digite um número maior que zero.")

    for numero in range(1, quantidade + 1):
        print(f"\n---- Tarefa {numero} de {quantidade} ----")
        nome = input("Nome da tarefa: ")
        dias_restantes = ler_numero("Dias até o prazo final (negativo se já passou): ")
        resposta = input("A tarefa já foi concluída? (s/n): ")

        concluida = resposta == "s" or resposta == "S"
        status = definir_status(concluida, dias_restantes)

        nomes.append(nome)
        dias.append(dias_restantes)
        concluidas.append(concluida)
        status_lista.append(status)

        print(f"Resultado: {nome} --> {status}")

    salvar_tarefas()


#Função que mostra a lista de tarefas inseridas
def listar_tarefas():
    print("\n==== LISTA DE TAREFAS ====")
    if len(nomes) == 0:
        print("Nenhuma tarefa cadastrada.")
    for i in range(len(nomes)):
        print(f"{i + 1}. {nomes[i]} | prazo: {dias[i]} dias | {status_lista[i]}")


#Função que edita uma tarefa já cadastrada
def editar_tarefa():
    if len(nomes) == 0:
        print("Nenhuma tarefa para editar.")
        return

    listar_tarefas()
    numero = ler_numero("\nQual o número da tarefa que deseja editar? ")

    if numero < 1 or numero > len(nomes):
        print("Número de tarefa inexistente.")
        return

    posicao = numero - 1
    print(f"\nEditando: {nomes[posicao]}")
    print("1 - Mudar o nome")
    print("2 - Mudar os dias até o prazo")
    print("3 - Mudar se foi concluída ou não")
    opcao = ler_numero("Escolha uma opção: ")

    if opcao == 1:
        nomes[posicao] = input("Novo nome: ")
    elif opcao == 2:
        dias[posicao] = ler_numero("Novos dias até o prazo: ")
    elif opcao == 3:
        resposta = input("A tarefa foi concluída? (s/n): ")
        concluidas[posicao] = resposta == "s" or resposta == "S"
    else:
        print("Opção inválida.")
        return

    #Como pode ter mudado o prazo ou a conclusão, calcula o status
    status = definir_status(concluidas[posicao], dias[posicao])
    status_lista[posicao] = status
    salvar_tarefas()
    print("Tarefa editada com sucesso!")


#Função que remove uma tarefa
def remover_tarefa():
    if len(nomes) == 0:
        print("Nenhuma tarefa para remover.")
        return

    listar_tarefas()
    numero = ler_numero("\nQual o número da tarefa que deseja remover? ")

    if numero < 1 or numero > len(nomes):
        print("Número de tarefa inexistente.")
        return

    posicao = numero - 1
    nome_removido = nomes[posicao]

    #Remove a mesma posição de todas as listas
    nomes.pop(posicao)
    dias.pop(posicao)
    concluidas.pop(posicao)
    status_lista.pop(posicao)

    salvar_tarefas()
    print(f"Tarefa '{nome_removido}' removida!")


#Função de calculo do resumo das tarefas cadastradas
def ver_status():
    total_concluidas = sum(1 for status in status_lista if status == "Concluída")
    total_atrasadas = sum(1 for status in status_lista if status == "ATRASADA")
    total_urgentes = sum(1 for status in status_lista if status == "Urgente")
    total_em_dia = sum(1 for status in status_lista if status == "Em dia")

    print("\n==== STATUS DAS TAREFAS ====")
    print(f"Concluídas: {total_concluidas}")
    print(f"Em dia: {total_em_dia}")
    print(f"Urgentes: {total_urgentes}")
    print(f"Atrasadas: {total_atrasadas}")


# Função que mostra o resumo final
def mostrar_resumo():
    total_concluidas = sum(1 for status in status_lista if status == "Concluída")
    total_atrasadas = sum(1 for status in status_lista if status == "ATRASADA")
    quantidade = len(nomes)

    percentual = (total_concluidas / quantidade * 100) if quantidade > 0 else 0
    tem_atraso = total_atrasadas > 0

    print("\n==== RESUMO FINAL ====")
    print(f"Total de tarefas cadastradas: {quantidade}")
    print(f"Concluídas: {total_concluidas}")
    print(f"Atrasadas: {total_atrasadas}")
    print(f"Percentual concluído: {percentual:.1f}%")

    if tem_atraso:
        print("Atenção: existem algumas tarefas atrasadas!")
    else:
        print("Tudo sob controle! Nenhuma tarefa atrasada.")


#============ Programa principal ============

print("==== CONTROLE DE PRAZOS ====")
carregar_tarefas()

while True:
    print("\n==== MENU ====")
    print("1 - Cadastrar tarefas")
    print("2 - Listar tarefas")
    print("3 - Ver status")
    print("4 - Ver resumo final")
    print("5 - Editar tarefa")
    print("6 - Remover tarefa")
    print("0 - Sair")
    opcao = ler_numero("Escolha uma opção: ")

    if opcao == 1:
        cadastrar_tarefas()
    elif opcao == 2:
        listar_tarefas()
    elif opcao == 3:
        ver_status()
    elif opcao == 4:
        mostrar_resumo()
    elif opcao == 5:
        editar_tarefa()
    elif opcao == 6:
        remover_tarefa()
    elif opcao == 0:
        break
    else:
        print("Opção inválida! Escolha um número de 0 a 6.")

print("\nPrograma finalizado. Até mais!")
