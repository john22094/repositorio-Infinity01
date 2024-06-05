from funcoes import adicionar_tarefas
from funcoes import remover_tarefas

tarefas = []

while True:
      print("""
      vou lhe dar um menu interativo para o senhor realizar suas atividades:
      1 - adicionar uma tarefa
      2 - retirar uma tarefa
      3 - visualizar lista de tarefas
      4 - sair da lista
      """)
      opcao = int(input('qual opção?: '))
      
      if opcao == 1:
            adicionar_tarefas.criar_tarefa(tarefas)

      elif opcao == 2:
            remover_tarefas.remover_tarefa(tarefas)

      elif opcao == 3:
            print(tarefas)

      elif opcao == 4:
            print("saindo...")
            break

      else:
            print("opção invalida")
            

      

