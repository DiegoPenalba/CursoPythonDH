import random
from clases.enemigo import Enemigo
from clases.jugador import Jugador



def main():
    nombreJugador = input("Bienvenido a la aventura en el Espacio! Por favor, ingrese su nombre: ")
    jugador = Jugador(nombreJugador)

    enemigos = [
        Enemigo("Alien", 50, 10),
        Enemigo("Robot", 30, 5),
        Enemigo("Monstruo", 70, 15)
    ]

    enemigosDerrotados = []

    print("COMIENZA LA AVENTURA")

    while enemigos:
        enemigoActual = random.choice(enemigos)

        if enemigoActual in enemigosDerrotados:
            continue

        print(f"Te encuentras con un {enemigoActual.nombre}, en tu camino")

        while enemigoActual.salud > 0:
            accion = input("Que deseas hacer? (atacar / huir): ").lower()

            if accion == "atacar":
                danoJugador = jugador.atacar()
                print(f"Has atacado al enemigo {enemigoActual.nombre} y le has causado {danoJugador} de daño")
                enemigoActual.recibirDano(danoJugador)

                if enemigoActual.salud > 0:
                    danoEnemigo = enemigoActual.atacar()
                    print(f"El {enemigoActual.nombre} y te causo {danoEnemigo} de daño")
                    jugador.recibirDano(danoEnemigo)
            
            elif accion == "huir":
                print("Has decidido huir del combate")
                break
        
        if jugador.salud <= 0:
            print(f"{jugador.nombre}, has perdido la partida")
        
        if enemigoActual.salud <= 0:
            enemigosDerrotados.append(enemigoActual)
            enemigos.remove(enemigoActual)
        
        jugador.ganarExperiencia(20)
        
        continuar = input("Quieres seguir explorando (s/n): ").lower()

        if continuar != "s":
            print("Gracias por jugar la batalla espacial!")
            break
    
    if not enemigos:
        print("Felicitaciones! has destruido a todos los enemigos!")

if __name__ == "__main__":
    main() # Algo propio de python, asegura que solo podes ejecutar este script en el programa principal

        