import math 
import matplotlib.pyplot as plt
import numpy as np

while True:
    try:
        v0 = float(input("• Digite a velocidade inicial em m/s: "))
        break
    except ValueError:
        print("> Apenas números são aceitos <")

while True:
    try:
        angulo = float(input("• Digite o ângulo de lançamento: "))
        break
    except ValueError:
        print("> Apenas números são aceitos <")

v0y = v0*(math.sin(math.radians(angulo)))
v0x = v0*(math.cos(math.radians(angulo)))

#Calculo das distancias maximas

a = 9.8
ay = -9.8
tDistanciay = v0y/a
distanciaMaximaY = v0y*tDistanciay+(1/2)*ay*(tDistanciay**2)
t = tDistanciay*2
distanciaMaximaX = v0x*t

#Calculo da trajetoria nos pontos de x

pontos_X = []
for i in np.arange(0, t, 0.1):
    ponto_X = v0x*i
    pontos_X.append(ponto_X)

#Calculo da trajetoria nos pontos de y

pontos_Y = []
for i in np.arange(0, tDistanciay, 0.1):
    ponto_Y = v0y*i+(1/2)*ay*(i**2)
    pontos_Y.append(ponto_Y)
for i in np.arange(tDistanciay, t, 0.1):
    ponto_Y = -(-v0y*i+1/2*a*(i**2))
    pontos_Y.append(ponto_Y)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajetória sem Resistência do ar')
plt.plot(pontos_X, pontos_Y)
plt.axis([0, distanciaMaximaX, 0, distanciaMaximaY])
plt.show()

print("")
input("""• Agora vamos para a parte com resistência do ar
        Aperte ENTER para cotinuar ...""")

#Parte com Resistência do AR

dt = 0.1
while True:
    try:
        k = float(input("• Digite o valor da resistência do ar: ")) #Resistência do ar
        break
    except ValueError:
        print("> Apenas números são aceitos <")
m = 50
Fx = 0
Fy = -m*a

#Calculo da trajetoria nos pontos de x

xn = 0
pontosra_X = []
for i in np.arange(0, t, 0.1):
    vx = v0x + ((Fx*dt/m)-(k*dt*((v0x)**2)/m))
    x = xn + vx*dt
    xn = x
    pontosra_X.append(x)

#Calculo da trajetoria nos pontos de y

yn = 0
pontosra_Y = []
for i in np.arange(0, tDistanciay, 0.1):
    vy = v0y + ((Fy*dt/m)-(k*dt*((v0y)**2)/m))
    y = yn + vy*dt
    v0y = vy
    yn = y
    pontosra_Y.append(y)
for i in np.arange(tDistanciay, t, 0.1):
    vy = v0y + ((Fy*dt/m)+(k*dt*((v0y)**2)/m))
    y = yn + vy*dt
    v0y = vy
    yn = y
    pontosra_Y.append(y)

plt.xlabel('X')
plt.ylabel('Y')
plt.title('Trajetória com Resistência do ar')
plt.plot(pontosra_X, pontosra_Y)
plt.axis([0, distanciaMaximaX, 0, distanciaMaximaY])
plt.show()