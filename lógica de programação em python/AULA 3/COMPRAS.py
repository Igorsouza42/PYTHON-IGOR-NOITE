Algoritmo "compras"

Var
// Seção de Declarações das variáveis 

   nomeProduto: caracter
   quantidade:inteiro
   valorProduto, valorCompra, valorPagar: Real


Inicio
// Seção de Comandos, procedimento, funções, operadores, etc... 

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

   escreval("o valor da compra do produto, ", nomeProduto,"é", valorcompra, "o valor a pagar é", valorPagar, ".")
   
Fimalgoritmo