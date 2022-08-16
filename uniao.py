#-----INPUT/DADOS---------------------------------------
x = [1,2,3,4,5,6,7,8,9,10]
y = [1,2,3,6,7,8,11,12,13,67]

# união de x e y, sem mostrar valores iguais

# criar vetor para a uniao
uniao = [0]*20

for i in range(10):
  uniao[i] = x[i]
# pre = [1,2,3,4,5,6,7,8,9,10,0,0,0,0,0,0,0,0,0,0]

#marcador para proximo indice livre
proxlivre = 10

#encontrar elementos de Y diferentes dos de X, ou diferentes dos de UNIAO, se houverem repeticoes dentro de Y.


for i in range(10): #indexador Y
  
  #Flag indicando que nao achei um numero igual
  achei = False
  
  for j in range(10): #indexador X
    
    if y[i] == uniao[j]:
      achei = True
      break
      
  # se cheguei aqui com achei==false, para esse y[i], nao ha elemento igual em X, e devo adiciona-lo em UNIAO.
      
  #if not achei:
  if achei == False:
    uniao[proxlivre] = y[i]
    proxlivre+=1

print (uniao)

# Alternativa:
#uniao=list(set(x + y))