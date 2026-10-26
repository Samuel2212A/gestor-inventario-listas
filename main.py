productos = []
cantidades = []


def pedir_cantidad(mensaje):
    texto = input(mensaje).strip()
    while not texto.isdigit():
        print("Debe ingresar un número mayor o igual a 0")
        texto = input(mensaje).strip()
    return int(texto)


def buscar_indice(nombre):
    nombre = nombre.lower()
    for i in range(len(productos)):
        if productos[i].lower() == nombre:
            return i
    return -1


def registrar_producto():
    nombre = input("Nombre del producto: ").strip()

    if nombre == "":
        print("El nombre no puede estar vacío.")
    elif buscar_indice(nombre) != -1:
        print("Ese producto ya está registrado. Use la opción 4 para cambiar su cantidad.")
    else:
        cantidad = pedir_cantidad("Cantidad disponible: ")
        productos.append(nombre)
        cantidades.append(cantidad)
        print("Producto registrado correctamente.")


def mostrar_inventario():
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        print("\n--- INVENTARIO ---")
        for i in range(len(productos)):
            print(i + 1, "-", productos[i], ":", cantidades[i])


def buscar_producto():
    nombre = input("Nombre del producto a buscar: ").strip()
    posicion = buscar_indice(nombre)

    if posicion == -1:
        print("El producto no existe en el inventario.")
    else:
        print("Producto encontrado:", productos[posicion])
        print("Cantidad disponible:", cantidades[posicion])


def modificar_cantidad():
    nombre = input("Nombre del producto a modificar: ").strip()
    posicion = buscar_indice(nombre)

    if posicion == -1:
        print("El producto no existe, no se puede modificar.")
    else:
        print("Cantidad actual de", productos[posicion], ":", cantidades[posicion])
        nueva_cantidad = pedir_cantidad("Nueva cantidad: ")
        cantidades[posicion] = nueva_cantidad
        print("Cantidad actualizada.")


def eliminar_producto():
    nombre = input("Nombre del producto a eliminar: ").strip()
    posicion = buscar_indice(nombre)

    if posicion == -1:
        print("El producto no existe, no se puede eliminar.")
    else:
        productos.pop(posicion)
        cantidades.pop(posicion)
        print("Producto eliminado.")


def mostrar_total_productos():
    print("Cantidad de productos diferentes:", len(productos))


def mostrar_mayor_cantidad():
    if len(productos) == 0:
        print("El inventario está vacío.")
    else:
        mayor = max(cantidades)
        print("Mayor cantidad disponible:", mayor)
        print("Producto(s) con esa cantidad:")
        for i in range(len(productos)):
            if cantidades[i] == mayor:
                print("-", productos[i])


def mostrar_menu():
    print("\n===== GESTOR DE INVENTARIO =====")
    print("1. Registrar un producto")
    print("2. Mostrar inventario")
    print("3. Buscar un producto")
    print("4. Modificar cantidad de un producto")
    print("5. Eliminar un producto")
    print("6. Ver cuántos productos diferentes hay")
    print("7. Ver producto con mayor cantidad")
    print("8. Salir")


def main():
    opcion = ""

    while opcion != "8":
        mostrar_menu()
        opcion = input("Elija una opción (1-8): ").strip()

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            mostrar_inventario()
        elif opcion == "3":
            buscar_producto()
        elif opcion == "4":
            modificar_cantidad()
        elif opcion == "5":
            eliminar_producto()
        elif opcion == "6":
            mostrar_total_productos()
        elif opcion == "7":
            mostrar_mayor_cantidad()
        elif opcion == "8":
            print("Gracias por usar el programa. ¡Hasta pronto!")
        else:
            print("Opción no válida. Por favor elija un número del 1 al 8.")


main()
