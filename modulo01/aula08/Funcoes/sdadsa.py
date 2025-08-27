# Exercicio 3
num1 = int(input("Informe um número inteiro: "))
num2 = int(input("Informe um número inteiro: "))
num3 = int(input("Informe um número inteiro: "))
numeros = ""
if num1 >= num2 and num1 >= num3:
    numeros += f" {num1}"
    if num2 >= num3:
        numeros += f" {num2}"
        numeros += f" {num3}"
    elif num3>=num2:
        numeros += f" {num3}"
        numeros += f" {num2}"

elif num2 >= num1 and num2 >= num3:
    numeros += f" {num2}"
    if num1 >= num3:
        numeros += f" {num1}"
        numeros += f" {num3}"
    elif num3>=num1:
        numeros += f" {num3}"
        numeros += f" {num1}"

else:
    numeros += f" {num3}"
    if num1 >= num2:
        numeros += f" {num1}"
        numeros += f" {num2}"
    elif num2>=num1:
        numeros += f" {num2}"
        numeros += f" {num1}"