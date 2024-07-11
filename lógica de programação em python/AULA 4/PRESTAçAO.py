Algoritmo "Prestaçao"
// Disciplina   : [Linguagem e Lógica de Programação]

Var
// Seção de Declarações das variáveis 

  valorprestacao, multa, totalpagar, taxa: real

  quantdias, diasmsg: inteiro


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

    escreval("Digite o valor da prestação:", valorprestacao)
    Leia(valorprestacao)
    
    escreval("Quantidade de dias em atraso:")
    Leia(quantdias)
    
    taxa <- 2-100
    multa <- valorprestacao * (taxa * quantdias)
    
    totalpagar <- valorprestacao + multa
     escreval("o valor a pagar é", totalpagar)


     se quantdias > 15 entao
     escreval("Entrar em contato com o usuario:")

     senao
     
     diasmsg <- 15 - quantdias
     escreval("Faltam", diasmsg,"para a mensagem.")

     fimse

Fimalgoritmo