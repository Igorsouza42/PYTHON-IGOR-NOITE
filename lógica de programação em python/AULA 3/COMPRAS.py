Algoritmo "compras"

Var
// Se��o de Declara��es das vari�veis 

   nomeProduto: caracter
   quantidade:inteiro
   valorProduto, valorCompra, valorPagar: Real


Inicio
// Se��o de Comandos, procedimento, fun��es, operadores, etc... 

//Entrada de dados

   escreva ("Digite o nome do produto: ")
   Leia(nomeProduto)

   escreva ("Digite a quantidade do produto: ")
   Leia(quantidade)
   
   escreval ("Digite o valor do produto: ")
   Leia(valorProduto)
   
   
//Processamento dos dados
   
  valorCompra <- quantidade * valorProduto
  
  se valorCompra > 500 entao
  
  valorPagar <- valorCompra - 10
  fimse


//Saida dos dados

   escreval("o valor da compra do produto, ", nomeProduto,"�", valorcompra, "o valor a pagar �", valorPagar, ".")
   
Fimalgoritmo