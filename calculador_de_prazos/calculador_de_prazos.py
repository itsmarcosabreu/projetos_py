#Variáveis das listas que vão guardar as tarefas cadastradas
nomes = []
dias = []
status_lista = []

#Função que define o status da tarefa
def definir_status(conluida, dias_restantes):
    if conluida:
        return "Concluída"
    elif dias_restantes < 0:
        return "ATRASADA"
    elif dias_restantes <= 2:
        return "Urgente"
    else:
        return "Em dia"


# Função do cadastro das tarefas
def cadastrar_tarefas():
    quantidade = 0
    while quantidade <= 0:
        quantidade = int(input("Quantas tarefas você quer cadastrar? "))
        if quantidade <= 0:
            print("Digite um número maior que zero.")

    for numero in range(1, quantidade + 1):
        print(f"\n---- Tarefa {numero} de {quantidade} ----")
        nome = input("Nome da tarefa: ")
        dias_restantes = int(input("Dias até o prazo final (negativo se já passou): "))
        resposta = input("A tarefa já foi concluída? (s/n): ")

        concluida = resposta == "s" or resposta == "S"
        status = definir_status(concluida, dias_restantes)

        nomes.append(nome)
        dias.append(dias_restantes)
        status_lista.append(status)

        print(f"Resultado: {nome} --> {status}")


#Função que mostra a lista de tarefas inseridas
def listar_tarefas():
    print("\n==== LISTA DE TAREFAS ====")
    for i in range(len(nomes)):
        print(f"{i + 1}. {nomes[i]} | prazo: {dias[i]} dias | {status_lista[i]}")


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
cadastrar_tarefas()

while True:
    if input("\nDeseja listar as tarefas cadastradas? (s/n): ").lower() == 's':
        listar_tarefas()

    if input("\nDeseja ver o status das tarefas cadastradas? (s/n): ").lower() == 's':  
        ver_status()

    if input("\nDeseja ver o resumo final? (s/n): ").lower() == 's':
        mostrar_resumo()

    if input("\nDeseja cadastrar mais tarefas? (s/n): ").lower() == 's':
        cadastrar_tarefas()

    if input("\nDeseja finalizar? (s/n): ").lower() == 's':
        break
    
    #Se não for finalizar irá mostrar as outras opções
    
    print("\n---- OUTRAS OPÇÕES ----")
    print("1 - Cadastrar mais tarefas")
    print("2 - Voltar ao resumo")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        cadastrar_tarefas()

print("\nPrograma finalizado. Até mais!")