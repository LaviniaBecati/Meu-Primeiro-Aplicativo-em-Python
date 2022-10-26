alcool= float(input("preço do alcool: "))
gasolina= float(input("preço da gasolina: "))

resultado = alcool/gasolina

print("resultado do calculo:",resultado)
if resultado<=0.70:
    print("compensa usar alcool")
else:
    print("Compensa usar gasolina!")
