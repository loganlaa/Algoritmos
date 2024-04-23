#A função input retorna uma string (se quiser número, tem q converter)!!!!!!!!!!!!!!!!


from fractions import Fraction #precisa passar números como argumentos
meio = Fraction(1, 2)
#num1 = float(input("Digite o primeiro número: "))
#num2 = float(input("Digite o 2° número: "))
#num3 = float(input("Digite o 3° número:"))
#soma = num1 + num2
#print("soma =", soma)
#subtracao = num1 - num2
#print("subtracao =", subtracao)
#multiplicacao = num1 * num2
#print("multiplicação =", multiplicacao)
#divisao = num1/num2
#print("divisão =", divisao)
#potenciacao = num2**num1
#print("potenciação =", potenciacao)
#radiciacao = num2**meio
#print("raiciação =", radiciacao)
#media = (num1*2 + num2*3 + num3*5)/10
#print("A média das notas é=", media)


#Condicionais (if-elif-else)
#Tem que ter a identação do que está dentro da estrutura!!!!!!!!!!!!!!!!
#if num1 < 18:
#   print("menor de idade")
#elif num1 >= 18 and num1 < 65 :
#    print("Adulto")
#else:
 #   print("Idoso")
 
#if num1 > num2:
#    print(num1, "é maior que", num2)
#elif num1< num2:
#    print(num2, "é maior que", num1)
#else:
#    print(num1, "é igual a", num2)


#if num1 % 2 == 0 :
#    print(num1, "é par")
#elif num1 % 2 != 0 :
#    print(num1, "é impar")



#Algorítimo aumento de salário
#if num1 < 1500.00 and num1 > 0:
 #   num1 = num1 + 0.1*num1
 #   print(num1)
#elif num1 >= 1500.00 :
#    num1 = num1 + 0.05*num1
 #   print(num1)
#else:
 #   print("Número inválido")
 
 
 
#condição de existência de um triangulo
#if (num1 < num2 + num3 and num2 < num1 + num3 and num3 < num1 + num2) and (num1 > 0 and num2 > 0 and num3 > 0):
 #   print("Esse triângulo existe")
#else:
#    print("Esse triângulo é impossível")



#Algoritmo peso ideal
#sexo = input("Sexo: (masculino/feminino)")
#altura = float(input("Altura (em metros):"))


#//o que deve ser realizado atrelado a uma função
#def masculino():
#    peso = (72.7 * altura) - 58
#    print("Peso ideal é:", peso)
    
#def feminino():
#    peso = (62.1 * altura) - 44.7
#    print(peso)
    
#def outrocaso():
#    print("Sexo inválido")
    
#atrela as funções às possíveis respostas corretas (CRIA O DICIONÁRIO)
#sexo_funcoes = {
#        "masculino": masculino,
 #       "feminino": feminino
}
 #//define o "Caso contrário"   
#def switch_case(sexo):    #DEFINE A FUNÇÃO SWITCH_CASE ATRELADA À VARIÁVEL SEXOO
#        sexo_funcoes.get(sexo, outrocaso)()       #Pega o valor de sexo via .get() do dicionário.... Se o valor do sexo existir no dicionário, ele retorna a função indicada no dicionário; se não existir, ele executa a função outrocaso()
        
#//executa o switch_case do sexo        
#switch_case(sexo)








#Verifica se o n° é multiplo e 3 e 5 ao mesmo tempo
#n = int(input("Insira o número:"))
#if n%3 == 0 and n%5 == 0 :
#    print("Esse número é múltiplo de 3 e 5 simultâneamente")
#elif n%3 ==0 and n%5 != 0 :
#    print("Esse número é multiplo apenas de 3")
#elif n%5 ==0 and n%3 != 0 :
#    print("Esse número é multiplo apenas de 5")
#else: 
#    print("Esse número não é múltiplo nem de 3 nem de 5 ")




#//SWITCH CASE MESES
#n = int(input("Insira número do mês:"))


#def jan():
#    print("Janeiro")
#def fev():
#    print("Fevereiro")
#def mar():
#    print("Março")
#def abr():
#    print("Abril")
#def mai():
#    print("Maio")
#def jun():
#    print("Junho")
#def jul():
#   print("Julho")
#def ago():
#    print("Agosto")
#def set():
 #   print("Seetembro")
#def out():
 #   print("Outubro")
#def nov():
#    print("Novembro")
#def dez():
#    print("Dezembro")
#def outrocaso():
#    print("Número inválido")
    
    
#mes_funcoes = {
#        1:jan,
#        2: fev,
 #       3: mar,
 #       4: abr,
 #       5: mai,
#        6: jun,
 #       7: jul,
 #       8: ago,
 #       9: set,
 #       10: out,
 #       11: nov,
 #       12: dez
 #   }


#def switch_case(n):
#    mes_funcoes.get(n, outrocaso)()
    
#switch_case(n)

