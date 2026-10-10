import os
nombre_mascotas=[""]*3 #pupi
edad_mascotas=[0]*3  #3
def insertar():
    for i in range(len(nombre_mascotas)): #.Length en c#
        nombre_mascotas[i]=input(f"ingrese nombre de la mascota: ")
        edad_mascotas[i]=int (input(f"ingrese edad mascota: "))

def mostrar():
    for i in range(len(nombre_mascotas)): #.Length en c#
      print(f"nombre: {nombre_mascotas[i]},edad: {edad_mascotas[i]}")
    input("presione para continuar")

def eliminar(nombreAborrar):
    for i in range(len(nombre_mascotas)):
      if nombre_mascotas[i].lower() ==nombreAborrar.lower(): #encontre a la mascota que quiero borrar
        nombre_eliminado = nombre_mascotas[i]
        for j in range(i, len(nombre_mascotas)-1): #penultimo registro
          #desplazando los elementos hacia la izquierda
          nombre_mascotas[j]= nombre_mascotas[j+1]
          edad_mascotas[j] = edad_mascotas[j+1]

          #dejar en blanco la ultima ubicacion
          nombre_mascotas[-1] = ""
          edad_mascotas[-1] = 0
          print(f"mascota eliminada {nombre_mascotas[i]}")
          return #detener la busqueda de mascotas con el mismo nombre OPCIONAL 
    print ("no se encontro la mascota")
def ordenar():
   for i in range(len(nombre_mascotas)):
      for j in range(i+1, len (nombre_mascotas)):
         if nombre_mascotas[i] == "":
            continue
         if nombre_mascotas[j]!="" and
         nombre_mascotas[i].lower() > nombre_mascotas[j].lower():
         nombre_mascotas[i], nombre_mascotas[j] = nombre_mascotas[j], nombre_mascotas[i]
         edad_mascotas[i], edad_mascotas[j] = edad_mascotas[j], edad_mascotas[i]
   print("Mascotas ordenadas alfabéticamente.")
            
def main():
   global nombre_mascotas, edad_mascotas #para modificar las listas declaradas fuera del arreglo
   #arreglos paralelos ambas listas deben tener la misma longitud
   nombre_mascotas=[""]*3 #iniciar la lista vacia para cadenas de longitud 3
   edad_mascotas=[0]*3 #iniciar la lista vacia para numeros enteros de longitud 3
   opcion=0
   while opcion !=5: ##opcion distinto a 4 (true)
    os.system('cls' if os.name== 'nt' else 'clear') #limpiar la consola
    print ("[1] Insertar mascota (nombre|edad)")
    print ("[2] Mostrar mascota (nombre|edad)")
    print ("[3] Eliminar mascota por nombre (en ambos vesctores)")
    print ("[4] Ordenar mascotas alfabeticamente")
    print ("[5] Salir")
    opcion = int(input("elije una opcion: "))
    if opcion ==1:
      insertar()
    elif opcion==2:
      mostrar()
    elif opcion==3:
      mascotaAborrar=input("ingrese mascota a borrar: ")
      eliminar(mascotaAborrar)
    elif opcion==4:
      ordenar()
    elif opcion==5:
      print ("saliendo...")
    else: print("opcion invalida")
    if opcion !=5: input("presioe para continuar..") #espere a la interaccion del usuario para recargar el manu
main()
     