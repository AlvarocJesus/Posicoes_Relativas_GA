# Exercício 1
pontoA=[]
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

a = vetorAB[0]/vetorAC[0]
b = vetorAB[1]/vetorAC[1]
c = vetorAB[2]/vetorAC[2]
if(a==b==c):
  print('O ponto C pertence a reta.')
else:
  print('O ponto C não pertence a reta.')


# Exercício 2
plano = []

print("Equação Geral do Plano: ax + by + cz + d = 0")
for i in range(4):
    plano.append(float(input(f"Digite o valor de {chr(97+i)}: ")))
print("\n")
pontoX = []
vetorU = []

print("Equação da Reta: X = A + t*u")
print("Coordenadas do ponto A:")
for i in range(3):
    pontoX.append(float(input(f"Digite a {i+1}a. coordenada: ")))
print("\n")
print("Coordenadas do vetor u:")
for i in range(3):
    vetorU.append(float(input(f"Digite a {i+1}a. coordenada: ")))
print("\n")

const = (
    (plano[0] * pontoX[0]) + (plano[1] * pontoX[1]) + (plano[2] * pontoX[2]) + plano[3]
)
variavel = (plano[0] * vetorU[0]) + (plano[1] * vetorU[1]) + (plano[2] * vetorU[2])

if variavel == 0:
    print("\nReta Paralela ao Plano")
else:
    alfa = (-1 * const) / variavel

    x = pontoX[0] + (vetorU[0] * alfa)
    y = pontoX[1] + (vetorU[1] * alfa)
    z = pontoX[2] + (vetorU[2] * alfa)

    print("Ponto de Intersecção:")
    print(f"x = {x:.2f}, y = {y:.2f}, z = {z:.2f}")

# Exercício 3
pontoA = []
pontoB = []
pontoC = []

print("Plano:")

for i in range(3):
  print(f"Coordenadas do ponto {chr(65+i)}:")
  for j in range(3):
    ponto = float(input(f"Digite a {j+1}a. coordenada: "))
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

print(f"vetorAB: {vetorAB}")
print(f"vetorAC: {vetorAC}")

print(f"a = {round((vetorAB[1]*vetorAC[2])-(vetorAB[2]*vetorAC[1]), 2)}")
a = round((vetorAB[1]*vetorAC[2])-(vetorAB[2]*vetorAC[1]), 2)
print(f"b = {round((vetorAB[2]*vetorAC[0])-(vetorAB[0]*vetorAC[2]), 2)}")
b = round((vetorAB[2]*vetorAC[0])-(vetorAB[0]*vetorAC[2]), 2)
print(f"c = {round((vetorAB[0]*vetorAC[1])-(vetorAB[1]*vetorAC[0]), 2)}")
c = round((vetorAB[0]*vetorAC[1])-(vetorAB[1]*vetorAC[0]), 2)
print(f"d = {round((pontoA[0]*(vetorAB[1] * vetorAC[2]) + pontoA[1] * (vetorAB[2] * vetorAC[0]) + pontoA[2] * (vetorAC[1] * vetorAB[0])) - (pontoA[0]*(vetorAB[1] * vetorAC[0]) + pontoA[1] * (vetorAB[0] * vetorAC[2]) + pontoA[2] * (vetorAC[1] * vetorAB[2])) , 2)}")
d = round((a*pontoA[0]) + (b*pontoA[1]) + (c*pontoA[2]), 2)

if a < 0:
  a *= -1
  b *= -1
  c *= -1
  print("Equação Geral do plano:")
  print("ax + by + cz + d = 0")
  print("onde:")
  print(f"a = {a}0, b = {b}0, c = {c}0 e d = {d}0")
elif a == 0 and b == 0 and c == 0 and d == 0:
	print("Dados Incorretos")
