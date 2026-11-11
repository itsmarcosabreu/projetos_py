print("==== CONTROLE DE PRAZOS ====")

#Lógica da repetição até que a entrada seja válida usando o "while"
quantidade = 0
while quantidade <= 0:
    quantidade = int(input("Quantas tarefas você quer cadastrar? "))
    if quantidade <= 0:
        print("Digite um número maior que zero.")

#Variáveis das contagens de tarefas
total_concluidas = 0
total_atrasadas = 0
total_urgentes = 0
total_em_dia = 0

#Lógica de repetição para cadastrar as tarefas usando o "for"
for numero in range(1, quantidade + 1):
    print(f"\n---- Tarefa {numero} de {quantidade} ----")
    nome = input("Nome da tarefa: ")
    dias_restantes = int(input("Dias até o prazo final (negativo se já passou): "))
    resposta = input("A tarefa já foi concluída? (s/n): ")

    #Variável para decidir a pergunta feita na variável "resposta" para a estrutura de decisão de sim ou não
    concluida = resposta == "s" or resposta == "S"

    #Lógica da estrutura de decisão para definir o status da tarefa usando "if", "elif" e "else"
    if concluida:
        status = "Concluída"
        total_concluidas += 1  # operador de soma e atribuição
    elif dias_restantes < 0:
        status = "ATRASADA"
        total_atrasadas += 1
    elif dias_restantes <= 2:
        status = "Urgente"
        total_urgentes += 1
    else:
        status = "Em dia"
        total_em_dia += 1

    print(f"Resultado: {nome} -> {status}")

#Resumo das tarefas cadastradas
percentual = total_concluidas / quantidade * 100
tem_atraso = total_atrasadas > 0

#Print do resumo das tarefas cadastradas
print("\n==== RESUMO ====")
print(f"Concluídas: {total_concluidas}")
print(f"Em dia: {total_em_dia}")
print(f"Urgentes: {total_urgentes}")
print(f"Atrasadas: {total_atrasadas}")
print(f"Percentual concluído: {percentual:.1f}%")

if tem_atraso:
    print("Atenção: existem algumas tarefas atrasadas!")
else:
    print("Tudo sob controle! Nenhuma tarefa atrasada.")