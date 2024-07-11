Algoritmo "boletim"
// Disciplina   : [Linguagem e Lógica de Programação]


Var
// Seção de Declarações das variáveis 

  nota1, nota2, media: Real

  nomeAluno: caracter


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

  escreva("Digite o nome do aluno: ")
  Leia(nomeAluno)
  
  escreva("Digite a 1ª nota: ")
  Leia(nota1)
  
  escreva("Digite a 2ª nota: ")
  Leia (nota2)
  
//Processamento dos dados

  media <- (nota1 + nota2)/2
  
//Estrutura de decisão

  se media >= 7 entao

  escreva("o aluno", nomeAluno, "está aprovado.")
  escreva("sua média é", media)

  senao
  
  se media <4 entao
  
 escreva("o aluno", nomeAluno, "está reprovado.")
  escreva("sua média é, media)
  
   senao
  
  
  escreva("o aluno", nomeAluno, "está recuperação.")
  escreva("sua média é", media)


    fimse

  fimse
  
Fimalgoritmo