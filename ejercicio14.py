nota1=int(input("Ingrese la primer nota:"))
nota2=int(input("Ingrese la segunda nota:"))
nota3=int(input("Ingrese la tercer nota:"))
promedio=(nota1+nota2+nota3)/3
if promedio>=7:
    print("Promocionado")
else:
    if promedio>=4:
        print("Regular")
    else:
        print("Reprobado")
