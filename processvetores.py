#Faça um programa que receba dez números e armazene em uma lista.
#-----INPUT---------------------------------------------

#criar e preencher lista
lista = [0]*10

for i in range(10):
  lista[i] = int(input("Digite um número: "))

#print (lista)


  
#-----PROCESSAMENTO------------------------------------
# 1) mostre apenas os números cujo valor seja superior a 10.

maior = [0]*10
livre=0

for i in range(10):
  if lista[i] > 10:
    maior[livre] = lista[i]
    livre += 1

#print(maior)


# 2) apresente quantos números são impar e quantos são par.

contimpar = 0
contpar = 0

for i in range(10):
  if lista[i] %2 == 0 :
    contpar +=1
  else:
    contimpar +=1


# 3) calcule a soma de todos os números da lista. Apresente a soma e a média baseada na soma e no número de números armazenados.

soma = 0

#for i in range(10):
#  soma += lista[i]

#Alternativa
for numero in lista :
  soma += numero
  

# 4) procure qual o MAIOR e o MENOR valor dentro da lista. 

maior = lista[0]
menor = lista[0]

for numero in lista:
  if numero >= maior:
    maior = numero
  if numero <= menor:
    menor = numero


# 5) solicite um outro número e armazene em uma variável chamada multiplicador. Percorra todo a lista e multiplique cada número pelo multiplicador e apresente em tela.

mult = int(input("Informe multiplicador: "))
novalista = [0] * 10

for i in range(10):
  novalista[i] = mult * lista[i]

#Alternativa
#for i in range(10):
#    result = lista[i] * mult
#    print(result)


  
#-------OUTPUTS-------------------------------------------------
print("\n-----RELATÓRIO-----\n")
#1
print("Os números maiores que dez são:")
#percorremos os numeros da lista, utilizando as entradas na contagem
for numero in lista :
  if numero > 10:
    print (numero)

#Alternativa:
#percorremos os numeros no range 0 até 9
#for i in range(10):
#  if lista[i] > 10 :
#    print(lista[i])
  
#2
print("Número de pares: ", contpar)
print("Número de ímpares: ", contimpar)

#3
print("A soma dos número é: ", soma)
print("A média dos número é: ", soma/10)

#4
print("O maior número é: ", maior)
print("O menor número é: ", menor)

#5
print("O vetor multiplicado por", mult,"é:")
print(novalista)