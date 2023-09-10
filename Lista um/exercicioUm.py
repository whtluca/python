# 1. Faça um Programa que peça dois números e imprima o maior deles.

while(True):
    try:
        numero_um = float(input("digite um numero: "))
        break        
    except:
        print("Apenas números ")
    
while(True):
    try:
        numero_dois = float(input("digite um numero: "))
        break   
    except:
        print("Apenas números ")
        
if(numero_um > numero_dois):
    print(f"o mairo número é:   {numero_um}")
else:
    print(f"o maior número é:  {numero_dois}")
       