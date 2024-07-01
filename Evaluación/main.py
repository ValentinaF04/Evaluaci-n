import funciones as f

jugadores=[]

while True:
    print("""
        ---------------MENÚ---------------
          1. Registrar puntajes torneo
          2. Listar todos los puntajes
          3. Imprimir por tipo
          4. Salir""" )
    op=int(input('Ingrese opción: '))

    if op==1:
        print('---------------REGISTRAR PUNTAJE---------------')
        f.registrar_puntajes(jugadores)
    elif op==2:
        print('---------------LISTA JUGADORES---------------')
        f.listar_puntajes(jugadores)
    elif op==3:
        print('---------------PLANILLA PUNTAJES---------------')
        f.imprimir_tipo(jugadores)
    elif op==4:
        break
    else:
        print('Opción no válida, intente nuevamente')
