import funciones

if __name__ == "__main__":
    while True:
        print("\nMenú de opciones:")
        print("1. Listado de videojuegos con su año de lanzamiento")
        print("2. Contar cuántos videojuegos hay por plataforma")
        print("3. Buscar videojuegos por género")
        print("4. Buscar videojuegos por desarrollador")
        print("5. Mostrar los 5 juegos mejor valorados")
        print("6. Salir")
        
        opcion = input("Seleccione una opción del proyecto: ")
        
        if opcion == "1":
            funciones.listar_videojuegos()
        elif opcion == "2":
            funciones.contar_por_plataforma()
        elif opcion == "3":
            funciones.filtrar_por_genero()
        elif opcion == "4":
            funciones.buscar_por_desarrollador()
        elif opcion == "5":
            funciones.top_5_mejor_valorados()
        elif opcion == "6":
            print("Este proyecto terminó. OOOOH")
            break
        else:
            print("Opción que no vale una trucha, repite.")
