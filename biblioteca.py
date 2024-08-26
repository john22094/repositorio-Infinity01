class Biblioteca:
    def __init__(self, nome):
        self.nome = nome
        self.livros = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f"Livro '{livro}' adicionado com sucesso!")

    def listar_livros(self):
        if not self.livros:
            print("Nenhum livro na biblioteca.")
        else:
            print(f"Livros na biblioteca '{self.nome}':")
            for livro in self.livros:
                print(f"- {livro}")
                
    def reservar_livro(self, livro):
        if livro in self.livros:
            if livro not in self.livros_reservados:
                self.livros_reservados.append(livro)
                print(f"Livro '{livro}' reservado com sucesso!")
            else:
                print(f"Livro '{livro}' já está reservado.")
        else:
            print(f"Livro '{livro}' não encontrado na biblioteca.")
        

def exibir_menu():
    print("\nMenu da Biblioteca:")
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. reservar livro")
    print("4. Sair")

def main():
    nome_biblioteca = input("Digite o nome da biblioteca: ")
    biblioteca = Biblioteca(nome_biblioteca) 
    
    while True:
        exibir_menu()
        opcao = input("Escolha uma opção: ")
        
        if opcao == "1":
            livro = input("Digite o nome do livro a ser adicionado: ")
            biblioteca.adicionar_livro(livro)
        elif opcao == "2":
            biblioteca.listar_livros()
        elif opcao == "3":
            reserva = input("qual o nome do livro?: ")
            if reserva in biblioteca.livros:
                print("livro reservado com sucesso!")
            elif reserva not in biblioteca.livros:
                print("livro pode estar reservado ou não existe na lista")
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()