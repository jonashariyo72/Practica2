def imprimirRonda (lista,i):
    for jugador,stats in lista[i].items():
        print (f"{jugador} =", end= " ")
        print (" ")
        for event,value in stats.items():
            print(f" {event} : {value} ", end= " ")
        print (" ")


def recorrerLista (lista,puntajes_totales,contadorMVP):
    for i in range (5):
        puntajes_ronda = {}
        print (" ")
        print ("RONDA NÚMERO: ", i + 1)
        print (" ")
        imprimirRonda(lista,i)
        print (" ")
        for jugador,stats in lista[i].items():
            puntaje = stats['kills'] * 3 + stats['assists'] * 1 - (1 if stats['deaths'] else 0)

            puntajes_ronda[jugador] = puntaje

            if jugador in puntajes_totales:
                puntajes_totales[jugador]['kills'] += stats['kills']
                puntajes_totales[jugador]['assists'] += stats['assists']
                puntajes_totales[jugador]['deaths'] += 1 if stats['deaths'] else 0
                puntajes_totales[jugador]['puntos'] += puntaje
            else:
                puntajes_totales[jugador] = {'kills': stats['kills'], 'assists': stats['assists'], 'deaths': 1 if stats['deaths'] else 0,'puntos': puntaje}

        mvp = max(puntajes_ronda, key=puntajes_ronda.get)
        contadorMVP[mvp] = contadorMVP.get(mvp, 0) + 1