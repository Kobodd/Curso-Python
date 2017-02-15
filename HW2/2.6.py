def play_nims(pile, max_stones):
    '''
    An interactive two-person game; also known as Stones.

    @param pile: the number of stones in the pile to start
    @param max_stones: the maximum number of stones you can take on one turn
    '''

    def correcto(piedras):
        '''
        A function to determine if a players input is valid
        for nims
        '''
        piedras = int(piedras)
        if(piedras >= 1 and piedras <= max_stones and piedras <= pile):
            return True
        else:
            return False

    while pile > 0:

        #player 1
        #            while [pile is not empty]:
        #               while [player 1’s answer is not valid]:
        #                   [ask player 1]
        #               [execute player 1’s move]

        print("Hay", pile, "Piedras restantes")
        p1 = 0
        while not correcto(p1):
            p1 = input("P1, Cuantas piedras quitas?")

            if not correcto(p1):
                print("Numero no valido")

        pile -= int(p1) #quitar las piedras de la pila

        if pile == 0:
            print("Felicidad Jugador 1 has ganado")
            break

            #p2 Mismo procedimiento que con p1

        print("Hay", pile, "Piedras Restantes")
        p2 = 0
        while not correcto(p2):
            p2 = input("P2, Cuantas piedras quitas?")
            #legal answer?
            if not correcto(p2):
                print("Numero no valido")

        pile -= int(p2) #quitar las piedras de la pila

        if pile == 0:
            print("Felicidad Jugador 2 has ganado")
            break

play_nims(100,20)