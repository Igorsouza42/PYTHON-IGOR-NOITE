def coletar_informacoes():
    # Coletando informações básicas
    nome = input("Nome completo: ")
    idade = input("Idade: ")
    email = input("Email: ")
    telefone = input("Telefone: ")
    endereco = input("Endereço: ")

    # Coletando formação acadêmica
    formacao_academica = []
    while True:
        curso = input("Curso (ou 'sair' para finalizar): ")
        if curso.lower() == 'sair':
            break
        instituicao = input("Instituição: ")
        ano_conclusao = input("Ano de Conclusão: ")
        formacao_academica.append((curso, instituicao, ano_conclusao))

    # Coletando experiências profissionais
    experiencias_profissionais = []
    while True:
        cargo = input("Cargo (ou 'sair' para finalizar): ")
        if cargo.lower() == 'sair':
            break
        empresa = input("Empresa: ")
        periodo = input("Período (Ex: 2019-2021): ")
        responsabilidades = input("Responsabilidades: ")
        experiencias_profissionais.append((cargo, empresa, periodo, responsabilidades))

    # Coletando habilidades
    habilidades = []
    while True:
        habilidade = input("Habilidade (ou 'sair' para finalizar): ")
        if habilidade.lower() == 'sair':
            break
        habilidades.append(habilidade)

    return {
        "nome": nome,
        "idade": idade,
        "email": email,
        "telefone": telefone,
        "endereco": endereco,
        "formacao_academica": formacao_academica,
        "experiencias_profissionais": experiencias_profissionais,
        "habilidades": habilidades
    }

def salvar_curriculo(informacoes):
    with open("curriculo.txt", "w") as file:
        # Salvando informações básicas
        file.write(f"Nome: {informacoes['nome']}\n")
        file.write(f"Idade: {informacoes['idade']}\n")
        file.write(f"Email: {informacoes['email']}\n")
        file.write(f"Telefone: {informacoes['telefone']}\n")
        file.write(f"Endereço: {informacoes['endereco']}\n")
        file.write("\n")

        # Salvando formação acadêmica
        file.write("Formação Acadêmica:\n")
        for curso, instituicao, ano_conclusao in informacoes['formacao_academica']:
            file.write(f"- Curso: {curso}, Instituição: {instituicao}, Ano de Conclusão: {ano_conclusao}\n")
        file.write("\n")

        # Salvando experiências profissionais
        file.write("Experiências Profissionais:\n")
        for cargo, empresa, periodo, responsabilidades in informacoes['experiencias_profissionais']:
            file.write(f"- Cargo: {cargo}, Empresa: {empresa}, Período: {periodo}\n")
            file.write(f"  Responsabilidades: {responsabilidades}\n")
        file.write("\n")

        # Salvando habilidades
        file.write("Habilidades:\n")
        for habilidade in informacoes['habilidades']:
            file.write(f"- {habilidade}\n")

if __name__ == "__main__":
    informacoes = coletar_informacoes()
    salvar_curriculo(informacoes)
    print("Currículo salvo em 'curriculo.txt'.")
