def imprimirRonda (lista,i):
    for jugador,stats in lista[i].items():
        print (f"{jugador} =", end= " ")
        print (" ")
        for event,value in stats.items():
            print(f" {event} : {value} ", end= " ")
        print (" ")