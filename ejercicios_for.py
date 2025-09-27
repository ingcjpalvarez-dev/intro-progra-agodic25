frutas = ["kiwi", "fresa", "piña", "uvas", "sandía"]

for fruta in frutas:
    print(f"{frutas.index(fruta)+1}. {fruta}")

frutas.append("plátano")
print(frutas)
print(frutas[3])
frutas[3] = "moras"
print(frutas)
print()

milista = ["Juli", 12, True, False, 32.124, [1, 2, 3], "Adiós"]

for item in milista:
    print(f"{milista.index(item)}: {item}")

print()

A = {1, 2, 3, 4, 8}
B = {3, 4, 5, 6}
interseccion = set()
print(type(A))
print(type(B))
print(type(interseccion))
print()

for x in A:
    if x in B:
        interseccion.add(x)

print(f"A: {A}, B: {B}, Intersección: {interseccion}")


tabla_del = input("De qué número te calculo la tabla del 1 al 10: ")

for i in range(1, 11):
    print(f"{i} x {tabla_del} = {i*int(tabla_del)}")

mi_tupla = (10, 20, 30)
print("Tupla original: ", mi_tupla)
print(mi_tupla[1])

