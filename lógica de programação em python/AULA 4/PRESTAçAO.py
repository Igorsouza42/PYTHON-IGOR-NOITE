Algoritmo "Presta�ao"
// Disciplina   : [Linguagem e L�gica de Programa��o]

Var
// Se��o de Declara��es das vari�veis 

  valorprestacao, multa, totalpagar, taxa: real

  quantdias, diasmsg: inteiro


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

    escreval("Digite o valor da presta��o:", valorprestacao)
    Leia(valorprestacao)
    
    escreval("Quantidade de dias em atraso:")
    Leia(quantdias)
    
    taxa <- 2-100
    multa <- valorprestacao * (taxa * quantdias)
    
    totalpagar <- valorprestacao + multa
     escreval("o valor a pagar �", totalpagar)


     se quantdias > 15 entao
     escreval("Entrar em contato com o usuario:")

     senao
     
     diasmsg <- 15 - quantdias
     escreval("Faltam", diasmsg,"para a mensagem.")

     fimse

Fimalgoritmo