def adicionar_livro():
    with open("livros.txt", "a") as arquivo:
        while True:
            nome_livro = input("Digite o nome do livro (ou 'sair' para terminar): ")
            if nome_livro.lower() == "sair":
                break
            autor_livro = input("Digite o nome do autor: ")
            if autor_livro.lower() == "sair":
                break
            arquivo.write(f"{nome_livro} - {autor_livro}\n")
        print("Os livros foram salvos no arquivo livros.txt.")

if __name__ == "__main__":
    adicionar_livro()
