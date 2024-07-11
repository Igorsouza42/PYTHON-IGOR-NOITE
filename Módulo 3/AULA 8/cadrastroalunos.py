def coletar_informacoes():
    nome = input("Nome completo: ")
    endereco = input("Endereço: ")
    cpf = input("CPF: ")
    email = input("Email: ")
    cep = input("CEP: ")
    idade = input("Idade: ")
    telefone = input("Telefone: ")
    
    return {
        "nome": nome,
        "endereco": endereco,
        "cpf": cpf,
        "email": email,
        "cep": cep,
        "idade": idade,
        "telefone": telefone
    }

def salvar_aluno(aluno):
    nome_arquivo = aluno['nome'].replace(" ", "_") + ".txt"
    with open(nome_arquivo, "w") as file:
        file.write(f"Nome: {aluno['nome']}\n")
        file.write(f"Endereço: {aluno['endereco']}\n")
        file.write(f"CPF: {aluno['cpf']}\n")
        file.write(f"Email: {aluno['email']}\n")
        file.write(f"CEP: {aluno['cep']}\n")
        file.write(f"Idade: {aluno['idade']}\n")
        file.write(f"Telefone: {aluno['telefone']}\n")

if __name__ == "__main__":
    while True:
        aluno = coletar_informacoes()
        salvar_aluno(aluno)
        print(f"Informações do aluno {aluno['nome']} salvas em '{aluno['nome'].replace(' ', '_')}.txt'.")
        
        continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
        if continuar != 's':
            break

    print("Cadastro de alunos finalizado.")
