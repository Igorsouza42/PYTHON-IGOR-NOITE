Algoritmo "boletim"
// Disciplina   : [Linguagem e L�gica de Programa��o]


Var
// Se��o de Declara��es das vari�veis 

  nota1, nota2, media: Real

  nomeAluno: caracter


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

  escreva("Digite o nome do aluno: ")
  Leia(nomeAluno)
  
  escreva("Digite a 1� nota: ")
  Leia(nota1)
  
  escreva("Digite a 2� nota: ")
  Leia (nota2)
  
//Processamento dos dados

  media <- (nota1 + nota2)/2
  
//Estrutura de decis�o

  se media >= 7 entao

  escreva("o aluno", nomeAluno, "est� aprovado.")
  escreva("sua m�dia �", media)

  senao
  
  se media <4 entao
  
 escreva("o aluno", nomeAluno, "est� reprovado.")
  escreva("sua m�dia �, media)
  
   senao
  
  
  escreva("o aluno", nomeAluno, "est� recupera��o.")
  escreva("sua m�dia �", media)


    fimse

  fimse
  
Fimalgoritmo