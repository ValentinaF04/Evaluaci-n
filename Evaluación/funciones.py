juegos=['valorant', 'fortnite', 'fifa']
TIPO=['principiante', 'avanzado', 'experto']

def registrar_puntajes(jugadores):
    while True:
        lista_juegoSeleccionado=[]

        id_jugador=input('Ingrese id del jugador: ')
        nombre=input('Ingrese nombre y apelido: ')
        while True: 
            juego_seleccionado=input('Ingrese juego(Fortnite, Valorant, Fifa): ')
            while juego_seleccionado not in juegos: #valido que el juego seleccionado esté en la lista juegos
                print('Juego no válido, ingrese nuevamente')
                juego_seleccionado=input('Ingrese juego(Fortnite, Valorant, Fifa): ')
            opcion=input('Desea ingresar otro juego? (si/no): ')
            if opcion=='no':
                break
            elif opcion=='si':
                ()
        #iterar en el juego seleccionado para que ingrese el puntaje de este
        for juego in juego_seleccionado:
            puntaje_obtenido=input(f'Ingrese el puntaje obtenido del juego {juego_seleccionado}: ')
            break

        tipo_jugador=input('ingrese tipo de jugador(Principiante - Avanzado - Experto): ')
        while tipo_jugador not in TIPO: #valido que el tipo de jugador esté en la lista TIPO
            print('Tipo de jugador no válido, intente nuevamente')
            tipo_jugador=input('ingrese tipo de jugador(Principiante - Avanzado - Experto): ')
            break


        jugadores={
            'Id' : id_jugador,
            'Nombre' : nombre,
            'Juego' : juego_seleccionado,
            'Puntaje_obtenido': puntaje_obtenido,
            'Tipo_jugador' : tipo_jugador
        }

        print('Jugador registrado con éxito')

        return jugadores
    
def listar_puntajes(jugadores):
    nombreArchivo='planilla_todos.txt'
    with open (nombreArchivo, 'w') as archivo:
        archivo.write(f"Id: {jugadores['Id']}")
        archivo.write(f"Nombre: {jugadores['Nombre']}")
        archivo.write(f"Juego: {jugadores['Juego']}")
        archivo.write(f"Puntaje obtenido: {jugadores['Puntaje_obtenido']}")
        archivo.write(f"Tipo jugador: {jugadores['Tipo_jugador']}")
    return archivo.readlines

def imprimir_tipo(jugador):
    seleccionar_tipo=input('¿Qué tipo de jugador desea imprimir?(Principiante - Avanzado - Experto): ')
    lista_tipoJugador=[]

    while seleccionar_tipo not in TIPO:
        print('Tipo de jugador no válido intente nuevamente')
        seleccionar_tipo=input('ingrese tipo de jugador(Principiante - Avanzado - Experto): ')
        break
    lista_tipoJugador.append(jugador)
    nombreArchivo=f'planilla_jugadores {seleccionar_tipo}.txt'
    with open (nombreArchivo, 'w') as archivo:
        archivo.write(f'Id: {jugador['Id']}')
        archivo.write(f'Nombre: {jugador['Nombre']}')
        archivo.write(f'Juego: {jugador['Juego']}')
        archivo.write(f'Puntaje obtenido: {jugador['Puntaje_obtenido']}')
        archivo.write(f'Tipo jugador: {jugador['Tipo_jugador']}')
    return archivo.readlines



    
#creo una lista de los juegos para que itere en el juego seleccionado al preguntarle por el puntaje
        #lista_juegoSeleccionado.append(juego_seleccionado)
        #for juego in range(lista_juegoSeleccionado):  


