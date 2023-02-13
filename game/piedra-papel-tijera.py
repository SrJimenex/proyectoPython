import random
def run ():
    opciones =('piedra','papel','tijeras')
    ganadorU = 0
    ganadorM = 0
    ronda = 1
    print ('*'*24)
    print ('* Bienvenido al inicio *')
    print ('*'*24)
    while True: 
        jugador = str (input ("\n Digite su opcion piedra, papel o tijeras => \n"))
        jugador = jugador.lower()
        maquina = random.choice(opciones)
        if jugador == maquina:
            print ()
            print ('-'*8)
            print ('- empate -')
            print ('-'*8,'\n')
        elif jugador == 'piedra' and maquina == 'tijeras':
            ganadorU += 1 
            print ()
            print ('-'*12)
            print ('- haz ganado -')
            print ('-'*12,'\n')
        elif jugador == 'piedra' and maquina == 'papel':
            ganadorM += 1
            print ('-'*12)
            print('haz perdido')
            print ('-'*12,'\n')
        elif jugador == 'papel' and maquina == 'piedra':
            ganadorU += 1
            print ('-'*12)
            print ('haz ganado')
            print ('-'*12,'\n')
        elif jugador == 'papel' and maquina == 'tijeras':
            ganadorM += 1
            print ('-'*12)
            print ('haz perdido')
            print ('-'*12,'\n')
        elif jugador == 'tijeras' and maquina == 'papel':
            ganadorU += 1
            print ('-'*12,)
            print ('Haz ganado')
            print ('-'*12,'\n')
        elif jugador == 'tijeras' and maquina == 'piedra':
            ganadorM += 1
            print ('-'*12)
            print ('Haz perdido')
            print ('-'*12,'\n')
        else:
            print ('='*29)
            print('= Esta opcion no es valida =')
            print ('-'*29,'\n')
            ronda -=1
        if ganadorU == 2 or ganadorM == 2:
            break
        print ('*'*12)
        print (f"* RONDA {ronda} *")
        print ('*'*12,'\n')
        print (f"rondas ganadas maquina=> {ganadorM} \t rondas ganadas por usuario=> {ganadorU}")
        ronda +=1

    
    if ganadorM == 2:
        print (':)'*18)
        print (f"El gandor es la maquina con un puntaje \n maquina: {ganadorM} \t usuario: {ganadorU} ")
        print (':)'*18)

    else:
        print (':)'*18)
        print (f"El gandor es el usuario con un puntaje \n maquina: {ganadorM} \t usuario: {ganadorU} ")
        print (':)'*18)

if __name__ == "__main__":
    run()
