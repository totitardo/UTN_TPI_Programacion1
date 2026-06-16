import csv # se importa la biblioteca csv para trabajar con archivos CSV

def agregar_pais(): # función para agregar un nuevo país al archivo CSV
    while True: # se inicia un bucle para solicitar al usuario que ingrese los datos del nuevo país, y se repite hasta que el usuario ingrese datos válidos
     nombre = str(input("Ingrese el nombre del país: ")) # se solicita al usuario que ingrese el nombre del país y se almacena en la variable "nombre"
     poblacion = int(input("Ingrese la población del país: ")) # se solicita al usuario que ingrese la población del país y se almacena en la variable "poblacion"
     superficie = int(input("Ingrese la superficie del país (en km²): ")) # se solicita al usuario que ingrese la superficie del país y se almacena en la variable "superficie"
     continente = str(input("Ingrese el continente del país: ")) # se solicita al usuario que ingrese el continente del país y se almacena en la variable "continente"
     if nombre == "" or poblacion <= 0 or superficie <= 0 or continente == "": # se verifica que el nombre del país y continente no esté vacío, que la población y superficie sean mayores a 0,
        print("Datos no válidos.") # si alguno de los datos ingresados no es válido se muestra un mensaje de error indicando que se han ingresado datos no válidos y se repite el bucle para solicitar los datos nuevamente
     else: # si todos los datos ingresados son válidos se sale del bucle
        break
    with open("Paises.csv", mode="a", encoding="utf-8", newline='') as archivo: # se abre el archivo CSV en modo de escritura 
        escritor = csv.writer(archivo) # se crea un objeto escritor para escribir en el archivo CSV
        escritor.writerow([nombre, poblacion, superficie, continente]) # se escribe una nueva fila en el archivo CSV con los datos del nuevo país

def actualizar_datos(): # función para actualizar los datos de un país existente en el archivo CSV
    nombre = str(input("Ingrese el nombre del país a actualizar: ")) # se solicita al usuario que ingrese el nombre del país que desea actualizar y se almacena en la variable "nombre"
    with open("Paises.csv", mode="r", encoding="utf-8") as archivo: # se abre el archivo CSV en modo de lectura 
        lector = csv.reader(archivo) # se crea un objeto lector para leer el archivo CSV
        paises = list(lector) # se convierte el objeto lector en una lista de países para poder modificarla
    for i, pais in enumerate(paises): # se itera sobre la lista de países para buscar el país que se desea actualizar
        if pais[0].lower() == nombre.lower(): # se compara el nombre del país con el nombre ingresado por el usuario, ignorando mayúsculas y minúsculas
            print(f"Datos actuales de {nombre}: Población: {pais[1]}, Superficie: {pais[2]} km², Continente: {pais[3]}") # se muestra al usuario los datos actuales del país que se desea actualizar
            while True: # se inicia un bucle para solicitar al usuario que ingrese los nuevos datos del país, y se repite hasta que el usuario ingrese datos válidos
             poblacion = int(input("Ingrese la nueva población del país: ")) # se solicita al usuario que ingrese la nueva población del país y se almacena en la variable "poblacion"
             superficie = int(input("Ingrese la nueva superficie del país (en km²): ")) # se solicita al usuario que ingrese la nueva superficie del país y se almacena en la variable "superficie"
             continente = str(input("Ingrese el nuevo continente del país: ")) # se solicita al usuario que ingrese el nuevo continente del país y se almacena en la variable "continente"
             if poblacion <= 0 or superficie <= 0 or continente == "": # se verifica que la población y superficie sean mayores a 0, y que el continente no esté vacío
                print("Datos no válidos.") # si alguno de los datos ingresados no es válido se muestra un mensaje de error indicando que se han ingresado datos no válidos y se repite el bucle para solicitar los datos nuevamente
             else:
                 paises[i] = [nombre, poblacion, superficie, continente] # se actualizan los datos del país en la lista de países con los nuevos datos ingresados por el usuario        
                 break    
    if i == len(paises) - 1 and paises[i][0].lower() != nombre.lower(): # si se ha iterado sobre toda la lista de países y no se ha encontrado el país que se desea actualizar, se muestra un mensaje indicando que no se encontró el país
     input(f"No se encontró el país {nombre}.") 
    with open("Paises.csv", mode="w", encoding="utf-8", newline='') as archivo: # se abre el archivo CSV en modo de escritura para guardar los cambios realizados en la lista de países
        escritor = csv.writer(archivo)
        escritor.writerows(paises)

def buscar_pais(): # función para buscar un país en el archivo CSV y mostrar sus datos
    nombre = str(input("Ingrese el nombre del país a buscar: ")) # se solicita al usuario que ingrese el nombre del país que desea buscar y se almacena en la variable "nombre"
    with open("Paises.csv", mode="r", encoding="utf-8") as archivo: # se abre el archivo CSV en modo de lectura 
        lector = csv.reader(archivo) # se crea un objeto lector para leer el archivo CSV
        for pais in lector: # se itera sobre el objeto lector
            if pais[0].lower() == nombre.lower(): # se compara el nombre del país con el nombre ingresado por el usuario, ignorando mayúsculas y minúsculas
                input(f"Datos de {nombre}: Población: {pais[1]}, Superficie: {pais[2]} km², Continente: {pais[3]}...") # se muestra al usuario los datos del país que se ha encontrado
                break
        else: # si no se encuentra el país se muestra un mensaje indicando que no se encontró el país
            input(f"No se encontró el país {nombre}...")

def filtrar_por_continente(): # función para filtrar los países por continente y mostrar sus datos
    continente = str(input("Ingrese el continente para filtrar los países: ")) # se solicita al usuario que ingrese el continente por el cual desea filtrar los países y se almacena en la variable "continente"
    with open("Paises.csv", mode="r", encoding="utf-8") as archivo: # se abre el archivo CSV en modo de lectura
        lector = csv.reader(archivo) # se crea un objeto lector para leer el archivo CSV
        print(f"Países en el continente {continente}:") # se muestra un mensaje indicando el continente por el cual se están filtrando los países
        for pais in lector: # se itera sobre el objeto lector para filtrar los países por continente
            if pais[3].lower() == continente.lower(): # se compara el continente del país con el continente ingresado por el usuario, ignorando mayúsculas y minúsculas
                print(f"{pais[0]}: Población: {pais[1]}, Superficie: {pais[2]} km²") # se muestra al usuario el nombre del país y sus datos de población y superficie si el país pertenece al continente ingresado por el usuario

def filtrar_por_poblacion(): # función para filtrar los países por población y mostrar sus datos
    poblacion_min = int(input("Ingrese la población mínima para filtrar los países: ")) # se solicita al usuario que ingrese la población mínima para filtrar los países y se almacena en la variable "poblacion_min"
    with open("Paises.csv", mode="r", encoding="utf-8") as archivo: # se abre el archivo CSV en modo de lectura 
        lector = csv.reader(archivo) # se crea un objeto lector para leer el archivo CSV
        print(f"Países con población mayor a {poblacion_min}:") # se muestra un mensaje indicando la población mínima para filtrar los países
        for pais in lector: # se itera sobre el objeto lector para filtrar los países por población
            if pais[1].lower() == "poblacion":  # se Salta la fila de encabezado
                continue
            if int(pais[1]) > poblacion_min: # se compara la población del país con la población mínima ingresada por el usuario
                print(f"{pais[0]}: Población: {pais[1]}, Superficie: {pais[2]} km², Continente: {pais[3]}")

def filtrar_por_superficie(): # función para filtrar los países por superficie y mostrar sus datos
    superficie_min = int(input("Ingrese la superficie mínima para filtrar los países (en km²): ")) # se solicita al usuario que ingrese la superficie mínima para filtrar los países y se almacena en la variable "superficie_min"
    with open("Paises.csv", mode="r", encoding="utf-8") as archivo: # se abre el archivo CSV en modo de lectura
        lector = csv.reader(archivo) # se crea un objeto lector para leer el archivo CSV
        print(f"Países con superficie mayor a {superficie_min} km²:") # se muestra un mensaje indicando la superficie mínima para filtrar los países
        for pais in lector: # se itera sobre el objeto lector 
            if pais[2].lower() == "superficie":  # se Salta la fila de encabezado
                continue
            if int(pais[2]) > superficie_min: # se compara la superficie del país con la superficie mínima ingresada por el usuario
                print(f"{pais[0]}: Población: {pais[1]}, Superficie: {pais[2]} km², Continente: {pais[3]}")                
    
def ordenar_por_nombre(): # función para ordenar los países por nombre y mostrar sus datos
    with open("Paises.csv", mode="r", encoding="utf-8") as archivo: # se abre el archivo CSV en modo de lectura 
        lector = csv.reader(archivo) # se crea un objeto lector para leer el archivo CSV
        paises = sorted(list(lector), key=lambda i: i[0].lower()) # se convierte el objeto lector en una lista de países y se ordena alfabéticamente por el nombre del país, ignorando mayúsculas y minúsculas
    print("Países ordenados por nombre:")
    for pais in paises: # se itera sobre la lista de países ordenados para mostrar sus datos
        if pais[0].lower() == "nombre":  #se Salta la fila de encabezado
            continue
        print(f"{pais[0]}: Población: {pais[1]}, Superficie: {pais[2]} km², Continente: {pais[3]}") 

def ordenar_por_poblacion(): # función para ordenar los países por población y mostrar sus datos
    with open("Paises.csv", mode="r", encoding="utf-8") as archivo:
        lector = csv.reader(archivo)
        next(lector)  # Saltar la fila de encabezado
        paises = sorted(list(lector), key=lambda i: int(i[1]), reverse=True)
    print("Países ordenados por población (de mayor a menor):")
    for pais in paises:
        print(f"{pais[0]}: Población: {pais[1]}, Superficie: {pais[2]} km², Continente: {pais[3]}")

def ordenar_por_superficie(): # función para ordenar los países por superficie y mostrar sus datos
    orden = int(input("1- mayor a menor 2- menor a mayor: ")) # se solicita al usuario que ingrese el orden en el que desea ordenar los países por superficie y se almacena en la variable "orden"
    with open("Paises.csv", mode="r", encoding="utf-8") as archivo: # se abre el archivo CSV en modo de lectura
        lector = csv.reader(archivo) # se crea un objeto lector para leer el archivo CSV
        next(lector)  #se salta la fila de encabezado
        if orden == 1: # se ordena la lista de países por superficie de mayor a menor si el usuario ingresó 1
            paises = sorted(list(lector), key=lambda i: int(i[2]), reverse=True)
            print("Países ordenados por superficie (de mayor a menor):")
        else: # se ordena la lista de países por superficie de menor a mayor si el usuario ingresó 2
            paises = sorted(list(lector), key=lambda i: int(i[2]), reverse=False)
            print("Países ordenados por superficie (de menor a mayor):")
    for pais in paises: # se itera sobre la lista de países ordenados para mostrar sus datos
        print(f"{pais[0]}: Población: {pais[1]}, Superficie: {pais[2]} km², Continente: {pais[3]}")

def estadisticas(): # función para calcular y mostrar estadísticas sobre los países en el archivo CSV
    with open("Paises.csv", mode="r", encoding="utf-8") as archivo: # se abre el archivo CSV en modo de lectura
        lector = csv.reader(archivo)
        next(lector)  # se salta la fila de encabezado
        paises = list(lector) # se convierte el objeto lector en una lista de países para poder calcular las estadísticas
    total_paises = len(paises) # se calcula el total de países en la lista de países
    poblacion_total = sum(int(pais[1]) for pais in paises) # se calcula la población total sumando la población de cada país en la lista de países
    superficie_total = sum(int(pais[2]) for pais in paises) # se calcula la superficie total sumando la superficie de cada país en la lista de países
    mayor_poblacion = max(paises, key=lambda i: int(i[1])) # se encuentra el país con mayor población utilizando la función max y una función lambda para comparar la población de cada país
    menor_poblacion = min(paises, key=lambda i: int(i[1])) # se encuentra el país con menor población utilizando la función min y una función lambda para comparar la población de cada país
    promedio_poblacion = poblacion_total / total_paises # se calcula el promedio de población dividiendo la población total entre el total de países
    promedio_superficie = superficie_total / total_paises # se calcula el promedio de superficie dividiendo la superficie total entre el total de países
    pais_por_continente = {} # se crea un diccionario para contar el número de países por continente
    for pais in paises: # se itera sobre la lista de países para contar el número de países por continente
        continente = pais[3] # se obtiene el continente de cada país
        if continente not in pais_por_continente: # se verifica si el continente ya está en el diccionario, si no está se agrega con una lista vacía
            pais_por_continente[continente] = [] # se agrega el país a la lista de países del continente correspondiente en el diccionario
        pais_por_continente[continente].append(pais) # se agrega el país a la lista de países del continente correspondiente en el diccionario
     
    print("------------------------------------------------------------------------------") 
    print(f"Total de países: {total_paises}")
    print(f"Población total: {poblacion_total}")
    print(f"Superficie total: {superficie_total} km²")
    print(f"País con mayor población: {mayor_poblacion[0]} con {mayor_poblacion[1]} habitantes")
    print(f"País con menor población: {menor_poblacion[0]} con {menor_poblacion[1]} habitantes")
    print(f"Promedio de población: {promedio_poblacion}")
    print(f"Promedio de superficie: {promedio_superficie} km²")
    print("Número de países por continente:")
    for continente, paises in pais_por_continente.items():
        print(f"{continente}: {len(paises)} países")
    print("------------------------------------------------------------------------------")    


opcion = 0 # se inicializa la variable "opcion" en 0 para controlar el bucle del menú principal del programa
while opcion != 11: # se ejecuta el bucle del menú principal del programa mientras la opción ingresada por el usuario no sea 11 (salir del programa)
   try:
    print("1- Agregar país 2- Actualizar datos de un país 3- Buscar país 4- Filtrar por continente 5- Filtrar por población \n 6- Filtrar por superficie 7- Ordenar por nombre 8- Ordenar por población 9- Ordenar por superficie 10- Estadísticas")
    opcion = int(input("Ingrese una opción: "))
    if opcion == 1:
        agregar_pais()
    elif opcion == 2:
        actualizar_datos()
    elif opcion == 3:
        buscar_pais()
    elif opcion == 4:
        filtrar_por_continente()
    elif opcion == 5:
        filtrar_por_poblacion()
    elif opcion == 6:
        filtrar_por_superficie()
    elif opcion == 7:
        ordenar_por_nombre()
    elif opcion == 8:
        ordenar_por_poblacion()
    elif opcion == 9:
        ordenar_por_superficie()
    elif opcion == 10:
        estadisticas()
    elif opcion == 11:
        input("Saliendo del programa...") 
        print("adios (:")
        quit()
    else:
        print("Opción no válida. Por favor, ingrese una opción del 1 al 11.") # si el usuario ingresa una opción que no está entre 1 y 11 se muestra un mensaje de error indicando que la opción ingresada no es válida    
   except (ValueError , IndexError) as E:   # se captura la excepción ValueError e IndexError que pueden ocurrir si el usuario ingresa un valor no numérico en las opciones del menú o en los datos de los países, y se muestra un mensaje de error indicando que se ha ingresado un valor no válido     
        print(f"Descripcion del error: {E} ")