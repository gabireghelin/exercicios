#-----INPUT/DADOS---------------------------------------
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,6,7,8,11,12,13,67]

# interseccao de x e y

# criar vetor para armazenar a interseccao
inter = [0]*10

#marcador proximo indice livre
prox = 0

# pegar umelemnto de x e comparar com os de y
#quando encontar um igual, adicionar na lista INTER, e parar de procurar para aquele x[i]
#proximo x, rodando todos os y.
#se nao encontrar, proximo x.

for i in range(10): # indexador X

  for j in range(10): # indexador Y
    
    #segura x e roda y
    if x[i] == y[j]:
      inter[prox] = x[i]
      prox +=1
      break
    
print (inter)