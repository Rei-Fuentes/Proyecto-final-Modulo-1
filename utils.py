import numpy as np
import random
import time

# ================================
# CREAR Y MOSTRAR TABLEROS
# ================================
def crear_tablero(tamaño=(10, 10)):
    return np.full(tamaño, "_")

def mostrar_tablero(tablero):
    # muestro tablero con cabecera 1-10 (más natural para humanos)
    print("    " + " ".join(str(i) for i in range(1, tablero.shape[1]+1)))
    for idx, fila in enumerate(tablero):
        print(f"{idx+1:2} " + " ".join(fila))

def mostrar_dos_tableros(tablero_jugador, tablero_maquina):
    # oculto barcos del enemigo hasta ser impactados
    oculto = np.where(np.isin(tablero_maquina, ["P","C","S"]), "_", tablero_maquina)
    print("\n    TU TABLERO                TABLERO ENEMIGO")
    print("    " + " ".join(str(i) for i in range(1, tablero_jugador.shape[1]+1)) +
          "      " + " ".join(str(i) for i in range(1, tablero_maquina.shape[1]+1)))
    for i in range(tablero_jugador.shape[0]):
        fila_jug = " ".join(tablero_jugador[i])
        fila_mac = " ".join(oculto[i])
        print(f"{i+1:2} {fila_jug}     {i+1:2} {fila_mac}")


# ================================
# COLOCAR BARCOS
# ================================
def colocar_barco(barco, tablero, nombre):
    for (f, c) in barco:
        tablero[f, c] = nombre

def crear_barco(eslora, tamaño=10):
    direcciones = [(0,1), (1,0), (0,-1), (-1,0)]  # Este, Sur, Oeste, Norte
    while True:
        f = random.randint(0, tamaño-1)
        c = random.randint(0, tamaño-1)
        df, dc = random.choice(direcciones)
        coords = [(f + i*df, c + i*dc) for i in range(eslora)]
        if all(0 <= x < tamaño and 0 <= y < tamaño for x,y in coords):
            return coords

def colocar_barcos(tablero):
    flota = [
        ("P", 4, 1),  # 1 portaaviones
        ("C", 3, 2),  # 2 cruceros
        ("S", 2, 3)   # 3 submarinos
    ]
    barcos = []
    for nombre, eslora, cantidad in flota:
        for _ in range(cantidad):
            colocado = False
            while not colocado:
                barco = crear_barco(eslora, tablero.shape[0])
                if all(tablero[f, c] == "_" for f, c in barco):
                    colocar_barco(barco, tablero, nombre)
                    barcos.append(barco)
                    colocado = True
    return barcos


# ================================
# DISPAROS
# ================================
def disparar(casilla, tablero):
    f, c = casilla
    if tablero[f, c] in ["P", "C", "S"]:
        tablero[f, c] = "X"   # tocado
        return "Tocado"
    elif tablero[f, c] == "_":
        tablero[f, c] = "A"   # agua
        return "Agua"
    else:
        return "Ya disparado"

def disparo_aleatorio(tablero):
    tamaño = tablero.shape[0]
    while True:
        f = random.randint(0, tamaño-1)
        c = random.randint(0, tamaño-1)
        if tablero[f, c] in ["_", "P", "C", "S"]:
            return disparar((f, c), tablero)


# ================================
# LEYENDA
# ================================
LEYENDA = {
    "_": "Agua (no disparado)",
    "P": "Portaaviones (4 casillas)",
    "C": "Crucero (3 casillas)",
    "S": "Submarino (2 casillas)",
    "X": "Tocado (barco alcanzado)",
    "A": "Agua disparada (fallo)"
}

def mostrar_leyenda():
    print("\n=== LEYENDA DEL TABLERO ===")
    for k, v in LEYENDA.items():
        print(f" {k}  →  {v}")
    print("============================\n")


# ================================
# PARTIDA COMPLETA CON PUNTUACIÓN
# ================================
def partida_limitada():
    tamaño_tablero = 10
    turnos_totales = 10
    turno_actual = 1

    tablero_jugador = crear_tablero((tamaño_tablero, tamaño_tablero))
    tablero_maquina = crear_tablero((tamaño_tablero, tamaño_tablero))

    colocar_barcos(tablero_jugador)
    colocar_barcos(tablero_maquina)

    barcos_restantes_jugador = True
    barcos_restantes_maquina = True

    # ✅ NUEVO: contadores de aciertos
    aciertos_jugador = 0
    aciertos_maquina = 0

    print("=== INICIO DEL JUEGO ===")
    mostrar_leyenda()

    while turno_actual <= turnos_totales and barcos_restantes_jugador and barcos_restantes_maquina:
        print(f"\n=========== TURNO {turno_actual} ===========")

        # turno jugador (introducción 1-10)
        fila = int(input("Elige fila (1-10): ")) - 1
        col  = int(input("Elige columna (1-10): ")) - 1

        resultado = disparar((fila, col), tablero_maquina)
        if resultado == "Tocado":
            print("👉 ¡Has tocado un barco enemigo!")
            aciertos_jugador += 1
        elif resultado == "Agua":
            print("🌊 Agua... fallaste.")
        else:
            print("⚠️ Ya habías disparado ahí.")

        # turno máquina
        resultado = disparo_aleatorio(tablero_jugador)
        if resultado == "Tocado":
            print("🤖 La máquina acertó en uno de tus barcos!")
            aciertos_maquina += 1
        elif resultado == "Agua":
            print("🤖 La máquina disparó al agua...")

        # mostrar tableros actualizados
        mostrar_dos_tableros(tablero_jugador, tablero_maquina)

        # quedan barcos?
        barcos_restantes_jugador = np.any(np.isin(tablero_jugador, ["P", "C", "S"]))
        barcos_restantes_maquina = np.any(np.isin(tablero_maquina, ["P", "C", "S"]))

        turno_actual += 1
        time.sleep(1)

    # RESULTADO FINAL
    print("\n=== FIN DE LA PARTIDA ===")
    print(f"Tus aciertos: {aciertos_jugador}")
    print(f"Aciertos de la máquina: {aciertos_maquina}")

    if not barcos_restantes_maquina and barcos_restantes_jugador:
        print("🎉 ¡Has hundido toda la flota enemiga!")
    elif not barcos_restantes_jugador and barcos_restantes_maquina:
        print("☠️ La máquina ha hundido tu flota...")
    else:
        if aciertos_jugador > aciertos_maquina:
            print("🎉 ¡Ganaste por mayor número de aciertos!")
        elif aciertos_maquina > aciertos_jugador:
            print("☠️ La máquina ganó por más aciertos...")
        else:
            print("🤝 ¡Empate total!")