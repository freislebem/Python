#Denis de Almeida Freislebem
#Pós-Graduação: Big Data
#RA 7162689-1

# 1) 85.3 , 84.3 , 79.5 , 82.5 , 80.2 , 84.6 , 79.2 , 70.9 , 78.6 , 86.2 , 74.0 , 83.7

import math

a = 85.3
b = 84.3
c = 79.5
d = 82.5
e = 80.2
f = 84.6
g = 79.2
h = 70.9
i = 78.6
j = 86.2
l = 74.0
m = 83.7

# a) Média

valores = (a+b+c+d+e+f+g+h+i+j+l+m)
media = valores / 12

print("\n------------Valor da Media------------")
print("\nLista de valores: ",a,b,c,d,e,f,g,h,i,j,l,m)
print("\nValor da Média: ", media)

# b) Mediana

Lista = [a,b,c,d,e,f,g,h,i,j,l,m]
Lista.sort()
print("\n\n------------Valor da Mediana------------")
print("\nValores ordenados em ordem crescente: ",Lista)


print("Quantidade total de valores da lista: ", len(Lista))
valor1 = Lista[int(len(Lista) / 2 - 1)]
valor2 = Lista[int(len(Lista) / 2)]
print("Valores Centrais: ",valor1, " e ", valor2)

valorMediana = (valor1 + valor2) / 2
print("Valores centrais somados e dividos por 2: ", valorMediana)


# c) Desvio Padrão

Lista = [a,b,c,d,e,f,g,h,i,j,l,m]
print("\n\n------------Valor do Desvio Padrão------------")
print("\nValor da média para ser usado como base de calculo: ",media)

a = (a - media)**2
b = (b - media)**2
c = (c - media)**2
d = (d - media)**2
e = (e - media)**2
f = (f - media)**2
g = (g - media)**2
h = (h - media)**2
i = (i - media)**2
j = (j - media)**2
l = (l - media)**2
m = (m - media)**2

print("\nValores subtraindo Media, depois elevando ao quadrado, somando tudo,"
      "\ndividindo pela quantidade e depois a raiz quadrada: ", math.sqrt((a+b+c+d+e+f+g+h+i+j+l+m) / len(Lista)))

