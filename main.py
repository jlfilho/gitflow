from div import div
from sum import sum
from sub import subtracao
from mult import mult

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
print("A soma é: ", sum(x, y))
print("A subtração é: ", subtracao(x, y))
print("A multiplicação é: ", mult(x, y))
print("A divisão é: ", div(x, y))
    
