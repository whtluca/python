# 2. Faça um Programa que peça um valor e mostre na tela se o valor épositivo ou negativo.

while(True):
    try:
        numero = float(input("digite um numero: "))
        break        
    except:
        print("Apenas números ")
        
if(numero < 0):
    print(f"O número é negativo.")
else:
    print(f"O número é positivo.")
       