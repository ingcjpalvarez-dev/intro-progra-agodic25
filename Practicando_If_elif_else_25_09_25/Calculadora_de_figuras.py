
#from math import * #Nos importamos toda la librería
#from math import sqrt, pi #aquí importamos la función de raíz cuadrada y el valor de pi
from math import pi #importamos solo el valor de la constate pi

print("---- Bienvenida a mi Calculadora de Figuras ---")
print("-°-°-°- Menú de figuras -°-°-°-")
print("1. Cubo")
print("2. Prisma")
print("3. Pirámide")
print("4. Cilindro")
print("5. Cono")
print("6. Esfera")

figura = input("Figura (1-6): ")

print("-°-°-°- Menú de opciones -°-°-°-")
print("1. Calcular el área")
print("2. Calcular el volumen")
print("3. Calcular ambos")
print("4. Salir")

opcion = input("Opción (1-4): ")

print("Todas las medidas a ingresar deben ser en centímetros")
if opcion == "1": #Este if controla qué quiere el usuario calcular.
    if figura == "1": #Este if aninado controla la figura para calcular el área.
        lado = float(input("Lado (cm):"))
        areaCubo = 6*lado**2
        print(f"El área total del cubo es: {areaCubo:.2} centímetros cuadrados") #El .2 indica el numero de decimales

    elif figura == "2":
        areaDeBase = float(input("Ingrese el área de la base del Prisma:"))
        perimetroDeBase = float(input("Ingrese el perimetro de la base del Prisma"))
        alturaH = float(input("Ingrese la altura del Prisma"))
        areaPrisma = 2 * areaDeBase + perimetroDeBase * alturaH
        print(f"El área total del Prisma es: {areaPrisma:.2} centímetros cuadrados")
        pass      
                                            #El pass es para omitir esta linea y evitar que se este corriendo todo el code y solo corra la linea que ocupes
    elif figura == "3":
        ladoPiramide = float(input("Ingrese el valor de un lado de la Pirámide: "))
        areaBasePiramide = ladoPiramide**2
        alturaHpiramide = float(input("Ingrese el valor de la altura de la Pirámide:"))
        areaTriangulo = ((ladoPiramide * alturaHpiramide)/2)*4
        areaTotalPiramide = areaBasePiramide + areaTriangulo
        print(f"El área total de la Pirámide es: {areaTotalPiramide} centímetros cuadrados")
        pass

    elif figura == "4":
        radioCilindro = float(input("Ingrese el valor del radio del Círculo: "))
        alturaCilindro = float(input("Ingrese la altura del Cilindro: "))
        areaCilindro = (2*pi*radioCilindro*alturaCilindro) + (2*pi*(radioCilindro**2))
        print(f"El área total del Cilindro es: {areaCilindro} centímetros cuadrados")
        pass

    elif figura == "5":
        radioCono = float(input("Ingrese el radio de la base del Cono: "))
        pendienteCono = float(input("Ingrese el valor de la pendiente que va desde el extremo del radio hasta la altura máxima del cono: "))
        areaCono = pi*radioCono*(radioCono+pendienteCono)
        print(f"El área total del Cono es: {areaCono} centímetros cuadrados")
        pass

    elif figura == "6":
        radioEsfera = float(input("Ingrese el radio de la Esfera: "))
        areaEsfera = 4*pi*radioEsfera**2
        print(f"El área total de la Esfera es: {areaEsfera} centímetros cuadrados")
        pass
    else:
        print("No conozco esa figura. ")

#Opción 2, calcular volúmenes
        
elif opcion == "2":
    if figura == "1": #Este if aninado controla la figura para calcular el volumen.
        lado = float(input("Lado (cm):"))
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:.4} centímetros cúbicos")

    elif figura == "2":
        areaDeBase = float(input("Ingrese el área de la base del Prisma:"))
        alturaH = float(input("Ingresa la altura del Prisma:"))
        volumenPrisma = areaDeBase * alturaH
        print(f"El volumen del prisma es: {volumenPrisma:.4} centímetros cúbicos")
        pass

    elif figura == "3":
        ladoPiramide = float(input("Lado (cm):"))
        alturaHpiramide = float(input("Altura (cm):"))
        volumenPiramide = 1/3*(ladoPiramide**2)*alturaHpiramide
        print(f"El volumen de la Pirámide es: {volumenPiramide:.4} centímetros cúbicos")
        pass

    elif figura == "4":
        radioCilindro = float(input("Ingrese el radio del Cilindro: "))
        alturaCilindro = float(input("Ingrese la altura del Cilindro: "))
        volumenCilindro = pi*(radioCilindro**2)*alturaCilindro
        print(f"El volumen del Ciilindro es: {volumenCilindro} centímetros cúbicos")
        pass

    elif figura == "5":
        radioCono = float(input("Ingrese el radio del cono (cm)"))
        alturaCono = float(input("Ingrese la altura (cm): "))
        volumenCono = (1/3)*pi*(radioCono**2)*alturaCono
        print(f"El volumne del Cono es: {volumenCono} centímetros cúbicos")
        pass

    elif figura == "6":
        radioEsfera = float(input("Ingrese el radio de la Esfera: "))
        volumenEsfera = (4/3)*pi*(radioEsfera**2)
        print(f"El volumen de la Esfera es: {volumenEsfera}")
        pass

    else:
        print("No conozco esa figura. ")

#Calcular ambos
elif opcion == "3":
    if figura == "1": #Este if aninado controla la figura para calcular ambos.
        lado = float(input("Lado (cm):"))
        areaCubo = 6*lado**2
        print(f"El área del cubo es: {areaCubo:}")
        volumenCubo = lado**3
        print(f"El volumen del cubo es: {volumenCubo:}")

    elif figura == "2":
        areaDeBase = float(input("Ingresa el área de la base del Prisma:"))
        perimetroDeBase = float (input("Ingrese el perímetro de la base del Prisma"))
        alturaH = float(input("Ingrese la altura del prisma:"))
        areaPrismaOp3 = 2 * areaDeBase + perimetroDeBase + alturaH
        volumenPrismaOp3 = areaDeBase * alturaH
        print(f"El area total del prisma es: {areaPrismaOp3}")
        print(f"El volumen del Prisma es: {volumenPrismaOp3}")

    elif figura == "3":
        ladoPiramide = float(input("Ingrese el valor de un lado de la Pirámide: "))
        areaBasePiramide = ladoPiramide**2
        alturaHpiramide = float(input("Ingrese el valor de la altura de la Pirámide:"))
        areaTriangulo = ((ladoPiramide * alturaHpiramide)/2)*4
        areaTotalPiramide = areaBasePiramide + areaTriangulo
        volumenPiramide = 1/3*(ladoPiramide**2)*alturaHpiramide
        print(f"El área total de la Pirámide es: {areaTotalPiramide} centímetros cuadrados")
        print(f"El volumen de la Pirámide es: {volumenPiramide:.4} centímetros cúbicos")
        pass

    elif figura == "4":
        radioCilindro = float(input("Ingrese el valor del radio del Círculo: "))
        alturaCilindro = float(input("Ingrese la altura del Cilindro: "))
        areaCilindro = (2*pi*radioCilindro*alturaCilindro) + (2*pi*(radioCilindro**2))
        volumenCilindro = pi*(radioCilindro**2)*alturaCilindro
        print(f"El área total del Cilindro es: {areaCilindro} centímetros cuadrados")
        print(f"El volumen total del Cilindro es: {volumenCilindro} centímetros cuadrados")
        pass

    elif figura == "5":
        radioCono = float(input("Ingrese el radio de la base del Cono: "))
        pendienteCono = float(input("Ingrese el valor de la pendiente que va desde el extremo del radio hasta la altura máxima del cono: "))
        areaCono = pi*radioCono*(radioCono+pendienteCono)
        alturaCono = float(input("Ingrese la altura (cm): "))
        volumenCono = (1/3)*pi*(radioCono**2)*alturaCono
        print(f"El área total del Cono es: {areaCono} centímetros cuadrados")
        print(f"El volumne del Cono es: {volumenCono} centímetros cúbicos")
        pass

    elif figura == "6":
        radioEsfera = float(input("Ingrese el radio de la Esfera: "))
        areaEsfera = 4*pi*radioEsfera**2
        volumenEsfera = (4/3)*pi*(radioEsfera**2)
        print(f"El área total de la Esfera es: {areaEsfera} centímetros cuadrados")
        print(f"El volumen de la Esfera es: {volumenEsfera}")
        pass

    else:
        print("No conozco esa figura. ")

elif opcion == "4":
    print("Hastal luego =)")

else:
    print("Opción incorrecta, adiós. =D")
#calculadoraFiguras.py
#Mostrando calculadoraFiguras.py.