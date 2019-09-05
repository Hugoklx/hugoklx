#esse programa deve ler do usuario a quantidade de elementos a serem inseridos numa lista
#depois, deve ler esses elementos e inseri-los em uma lista
#logo em seguida, deve imprimir os elementos na ordem contrária de insercao (o último inserido é o primeiro a ser impresso)...


nElementos= int(input("Digite a quantidade de números que serão inseridos na lista: \n"))
listaNumeros = []
cont= 0

while (cont < nElementos):
  numero = int(input("digite um numero: "))
  listaNumeros.append(numero)
  cont+=1

cont2 = nElementos
while (cont2 > 0):
  print(listaNumeros[cont2-1])
  cont2-=1
