from math import *

# Exercicio 1
""" pontoA=[]
pontoB=[]
pontoC=[]

print('Plano:')

for i in range(3):
  print(f'Coordenadas do ponto {chr(65+i)}:')
  for j in range(3):
    ponto = int(input(f'Digite a {j+1}a. coordenada: '))
    if(i==0):
      pontoA.append(ponto)
    if(i==1):
      pontoB.append(ponto)
    if(i==2):
      pontoC.append(ponto)

vetorAB = []
vetorAC = []

for i in range(len(pontoA)):
  sub1 = pontoB[i]-pontoA[i]
  sub2 = pontoC[i]-pontoA[i]
  vetorAB.append(sub1)
  vetorAC.append(sub2)

prodEscalar = sqrt((pow((vetorAB[0] - vetorAC[0]),2)+pow((vetorAB[1] - vetorAC[1]),2)+pow((vetorAB[2] - vetorAC[2]),2)))

print(f'prodEscalar: {prodEscalar}')

if(prodEscalar>0):
  print('O ponto C pertence a reta.')
elif(prodEscalar<0):
  print('O ponto C pertence a reta.')
elif(prodEscalar==0):
  print('O ponto C não pertence a reta.') """

# Exercicio 2
""" plano = []

print("Equação Geral do Plano: ax + by + cz + d = 0")
for i in range(4):
  plano.append(int(input(f"Digite o valor de {chr(97+i)}: ")))
print('\n')
pontoX = []
vetorU = []

print("Equação da Reta: X = A + t*u")
print("Coordenadas do ponto A:")
for i in range(3):
  pontoX.append(int(input(f"Digite a {i+1}a. coordenada: ")))
print('\n')
print("Coordenadas do vetor u:")
for i in range(3):
  vetorU.append(int(input(f"Digite a {i+1}a. coordenada: ")))
print('\n')
prodEscalar = sqrt(
  (
    pow((plano[0] - vetorU[0]), 2)
    + pow((plano[1] - vetorU[1]), 2)
    + pow((plano[2] - vetorU[2]), 2)
  )
)

# plano[0]*(pontoX[0]+vetorU[0]t)+plano[1]*(pontoX[1]+vetorU[1]t)+plano[2]*(pontoX[2]+vetorU[2]*t)=0

# ((plano[0]*pontoX[0])+(plano[0]*vetorU[0]t)) + ((plano[1]*pontoX[1])+(plano[1]*vetorU[1]t)) + ((plano[2]*pontoX[2])+(plano[2]*vetorU[2]t)) = plano[3]

# ((plano[0]*pontoX[0]) + (plano[1]*pontoX[1]) + (plano[2]*pontoX[2])) + ((plano[0]*vetorU[0]t) + (plano[1]*vetorU[1]t) + (plano[2]*vetorU[2]t)) = plano[3]

# ((plano[0]*vetorU[0])*t) + ((plano[1]*vetorU[1]) * t) + ((plano[2]*vetorU[2]) * t) = plano[3] - ((plano[0]*pontoX[0]) + (plano[1]*pontoX[1]) + (plano[2]*pontoX[2]))

# t = (plano[3] - ((plano[0]*pontoX[0]) + (plano[1]*pontoX[1]) + (plano[2]*pontoX[2]))) / ((plano[0]*vetorU[0]) + (plano[1]*vetorU[1]) * (plano[2]*vetorU[2]))

# 2+2t+2+8t-3+2t = 0
# 1+12t = 0
# t=-1/12

print(f"prodEscalar {prodEscalar}")

print('\n')

if prodEscalar != 0:
  conta = (
    plano[3]
    - ((plano[0] * pontoX[0]) + (plano[1] * pontoX[1]) + (plano[2] * pontoX[2]))
  ) / ((plano[0] * vetorU[0]) + (plano[1] * vetorU[1]) * (plano[2] * vetorU[2]))

  print("Ponto de Intersecção:")
  print(
    f"x = {round(pontoX[0]+(vetorU[0]*conta), 2)}, y = {round(pontoX[1]+(vetorU[1]*conta), 2)}, z = {round(pontoX[2]+(vetorU[2]*conta), 2)}"
  )
elif prodEscalar == 0:
  print("A reta esta contida no plano")
else:
  print("A reta esta e paralela ao plano") """

# Exercicio 3
""" pontoA = []
pontoB = []
pontoC = []

print("Plano:")

for i in range(3):
  print(f"Coordenadas do ponto {chr(65+i)}:")
  for j in range(3):
    ponto = int(input(f"Digite a {j+1}a. coordenada: "))
    if i == 0:
      pontoA.append(ponto)
    if i == 1:
      pontoB.append(ponto)
    if i == 2:
      pontoC.append(ponto)

vetorAB = []
vetorAC = []

for i in range(len(pontoA)):
  sub1 = pontoB[i] - pontoA[i]
  sub2 = pontoC[i] - pontoA[i]
  vetorAB.append(sub1)
  vetorAC.append(sub2)

print("Equação Geral do plano:")
print("ax + by + cz + d = 0")
print("onde:")
print(
  f"a = {round((vetorAB[1]*vetorAC[2]) - (vetorAC[2]*vetorAB[1]))}, b = {round((vetorAB[2]*vetorAC[0]) - (vetorAC[0]*vetorAB[2]))}, c = {round((vetorAB[0]*vetorAC[1]) - (vetorAC[1]*vetorAB[0]))} e d = {round((pontoA[0]*((vetorAB[1]*vetorAC[2]) - (vetorAC[2]*vetorAB[1]))) + (pontoA[1]*((vetorAB[2]*vetorAC[0]) - (vetorAC[0]*vetorAB[2]))) + (pontoA[2]*((vetorAB[0]*vetorAC[1]) - (vetorAC[1]*vetorAB[0]))))}"
) """
