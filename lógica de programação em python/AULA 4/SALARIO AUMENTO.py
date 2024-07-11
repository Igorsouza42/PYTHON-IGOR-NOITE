Algoritmo "salario aumento"
// Disciplina   : [Linguagem e Lógica de Programação]

Var
// Seção de Declarações das variáveis 

   salario, aumento, salarioReajuste:caracter

Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

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