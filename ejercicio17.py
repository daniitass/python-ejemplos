num=int(input("Ingrese un valor de hasta tres digitos positivo:"))
if num<10:
    print("Tiene un dígito")
else:
    if num<100:
        print("Tiene dos dígitos")
    else:
        if num<1000:
            print("Tiene tres dígitos")
        else:
            print("Error, debe ingresar un numero de hasta 3 digitos")
