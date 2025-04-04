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

        rankingPorRonda = sorted(puntajes_ronda.items(), key=lambda x: x[1], reverse=True)
        print (" ")
        print ("RANKING DE RONDA: ", i + 1)
        print ("-" * 25)
        for jugador, puntos in rankingPorRonda:
            print(f"{jugador}: {puntos} puntos")
        print ("-" * 25)

def imprimirRankingFinal (puntajes_totales,contadorMVP):
    print ("RANKING FINAL: ")
    print (" ")
    rankingFinal = sorted(puntajes_totales.items(), key=lambda x: x[1]['puntos'], reverse=True)
    print("Jugador | Kills | Asistencias | Muertes | MVPs | Puntos")
    print("-" * 55)
    for jugador, data in rankingFinal:
        print(f"{jugador:<7} | {data['kills']:<5} | {data['assists']:<10} | {data['deaths']:<7} | {contadorMVP.get(jugador, 0):<4} | {data['puntos']:<6}")