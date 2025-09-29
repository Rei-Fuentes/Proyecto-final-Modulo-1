 🚢 Hundir la Flota en Python

## 📌 Descripción
Este proyecto implementa el clásico juego **Hundir la Flota** (versión simplificada) en **Python** para terminal. El jugador se enfrenta contra la máquina en un tablero de **10x10** con barcos posicionados aleatoriamente. Gana quien hunda toda la flota enemiga o, si se acaban los turnos, quien tenga más aciertos.

## 🎮 Reglas del Juego
- El tablero es de **10 × 10** casillas.
- Los barcos se colocan automáticamente de forma aleatoria:
  - 🚢 P → Portaaviones (4 casillas, 1 en total)  
  - 🚢 C → Crucero (3 casillas, 2 en total)  
  - 🚢 S → Submarino (2 casillas, 3 en total)  
- Símbolos durante la partida:
  - _ → Agua sin disparar  
  - A → Agua donde se disparó  
  - X → Disparo acertado (barco tocado)  
- El jugador introduce coordenadas (fila y columna) con números **del 1 al 10**.
- La máquina dispara de manera aleatoria.
- El juego termina cuando:
  1. Algún jugador pierde todos sus barcos.
  2. O se acaban los turnos → gana el que tenga más aciertos.

## ⚡ Requisitos
- **Python 3.10 o superior**  
- Librería **NumPy**  
Instalación rápida en terminal:  
pip install numpy

## ▶️ Ejecución
1. Clonar el repositorio o descargarlo:  
git clone https://github.com/TU-USUARIO/hundir_la_flota.git && cd hundir_la_flota  
2. Ejecutar desde la terminal:  
python3 main.py

## 📋 Ejemplo de partida (recortado)
=== INICIO DEL JUEGO ===  
=== LEYENDA DEL TABLERO ===  
_ → Agua  
P → Portaaviones  
C → Crucero  
S → Submarino  
X → Barco tocado  
A → Agua disparada  

=========== TURNO 1 ===========  
Elige fila (1-10): 3  
Elige columna (1-10): 4  
🌊 Agua... fallaste.  
🤖 La máquina acertó en uno de tus barcos!

## 👨‍💻 Autor
Proyecto realizado por **Reiner Fuentes Ferrada** como proyecto final del **Módulo 1 de Data Science – The Bridge**." > README.md
