num01 = int(input("Digite um número: "))
num02 = int(input("Digite o segundo número: "))
cod01 = int(input("Digite o código: "))

if cod01 == 1 or cod01 == 2:
    if num01 > num02:
        print(num01,"é maior que",num02)
    elif num01 < num02:
        print(num02,"é maior que",num01)
        
    else:
        print("Ambos são iguais.")
elif cod01 == 3 or cod01 == 4:
    if num01 < num02:
        print("o",num01, "é menor.")
    elif num01 > num02:
        print("o",num02, "é menor.")
    else:
        print("Valores errados.")