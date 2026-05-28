import winsound
import time
print("=== Simulador de microtonos ===")
maximo_microtonos = 25
microtonos_libres = 25
microtonos_activos = 0
ejecutando = True 
while ejecutando:
    print("\n=== Panel de microtonos ===")
    print("1.- Ver cuantos microtonos quedan libres")
    print("2.- Activar microtonos (Activacion de sonido)")
    print("3.- Recuperar microtonos ")
    print("4.- Monitorear el sonido actual")
    print("5.- Salir")
    opcion = int(input("Elige una opcion(1-5): "))
    if opcion == 1:
        print(f"\n[INFO] tienes{microtonos_libres} microtonos disponibles para usar")
    elif opcion == 2:
        print(f"\n ACTIVAR MICROTONOS (Disponibles: {microtonos_libres})")
        if microtonos_libres == 0:
            print("Ya no se pueden emitir mas microtonos, sonido al limite")
        else:
            try:
                cantidad = int(input("¿Cuantos micrtonos quieres activar?: "))
                if cantidad <= 0:
                    print("Tienes que activar al menos 1 microtono")
                elif cantidad > microtonos_libres:
                    print(f"Solo puedes activar hasta {microtonos_libres} microtonos")
                else:
                    microtonos_libres -= cantidad
                    microtonos_activos += cantidad
                    print("Reproduciendo microtonos")
                   #for range (1,cantidad +1):
                    # print(f"Microtono {i} activando. . .")
                    #  winsound.Beep(440,300) #440 HZ por 300 milesimas de segundo
                    #   time.sleep(0.05)
                    frecuencias = [440,440,440,587,880,784,740,659]
                    duraciones = [300,300,300,700,700,200,200,200]
                    for i in range (1,cantidad +1):
                        nota_actual = frecuencias[(i-1) % len(frecuencias)]
                        duracion_actual = duraciones[(i-1) % len (duraciones)]
                        winsound.Beep(nota_actual,duracion_actual)
                        time.sleep(0.05)
            except ValueError:
                print("Error")
    elif opcion ==3:
        try:
            print(f"\n Recuperar microtonos, actualmente hay {microtonos_activos} microtonos activos")           
            cantidad = int(input("¿Cuantos microtonos quieres recuperar?: "))
            if cantidad <= 0:
                print("Error, la cantidad de micrtonos a recuperar debe ser mayor a 0")
            elif microtonos_libres + cantidad > maximo_microtonos:
                print(f"error: no puedes apagar tantos microtonos porque el maximo es {maximo_microtonos}")
            else:
                microtonos_libres += cantidad
                microtonos_activos -= cantidad
                print(f"Recuperaste {cantidad} de microtonos para ser usados en otro momento")
                winsound.beep(440,150)
        except ValueError:
            print("Error, debes colocar un numero entero")
    elif opcion == 4:
        print(f"Hay {microtonos_activos} microtonos activos haciendo vibrar el ambiente ")
    elif opcion == 5:
        print("Saliendo del sistema")
        ejecutando = False
    else:
        print("Error")

