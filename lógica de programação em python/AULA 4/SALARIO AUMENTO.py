Algoritmo "salario aumento"
// Disciplina   : [Linguagem e L�gica de Programa��o]

Var
// Se��o de Declara��es das vari�veis 

   salario, aumento, salarioReajuste:caracter

Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

    escreval("Digite o seu nome: ")
     Leia(nome)

     escreval("Digite o seu salario:")
     Leia(salario)

    aumento <- (salario * 15)/100

   salarioReajuste <- salario + aumento
   
   
   escreval("nome:", nome)
   escreval("salario:", salario)
   escreval("aumento:", aumento)
   escreval ("salario com reajuste:", salarioReajuste)


Fimalgoritmo