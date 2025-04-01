import json
import os
from collections import defaultdict

# Cargar el JSON sin depender de una ruta absoluta
def cargar_datos():
    try:
        # Obtener la ruta del directorio actual del script
        base_dir = os.path.dirname(os.path.abspath(__file__))
        json_path = os.path.join(base_dir, "proyecto mejorado.json")
        
        with open(json_path, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print("Error: El archivo 'proyecto mejorado.json' no se encuentra en el directorio actual.")
        return {"videojuegos": []}

data = cargar_datos()

# Resto del código permanece igual
def listar_videojuegos():
    for juego in data["videojuegos"]:
        print(f"{juego['titulo']} - {juego['año_lanzamiento']}")

def contar_por_plataforma():
    conteo = defaultdict(int)
    for juego in data["videojuegos"]:
        for plataforma in juego["plataforma"]:
            conteo[plataforma] += 1
    
    for plataforma, cantidad in conteo.items():
        print(f"{plataforma}: {cantidad} juegos")

def filtrar_por_genero():
    genero = input("Ingrese un género: ")
    print(f"Juegos del género '{genero}':")
    for juego in data["videojuegos"]:
        if genero in juego["genero"]:
            print(f"- {juego['titulo']}")

def buscar_por_desarrollador():
    nombre_dev = input("Ingrese el nombre del desarrollador: ")
    print(f"Juegos desarrollados por '{nombre_dev}':")
    for juego in data["videojuegos"]:
        if juego["desarrollador"]["nombre"].lower() == nombre_dev.lower():
            print(f"- {juego['titulo']}")

def top_5_mejor_valorados():
    top_juegos = sorted(data["videojuegos"], key=lambda x: x["puntuacion"], reverse=True)[:5]
    print("Top 5 juegos mejor valorados:")
    for juego in top_juegos:
        print(f"{juego['titulo']} - {juego['puntuacion']}")
