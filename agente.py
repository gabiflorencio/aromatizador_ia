#if nF > nM: borrifar aroma doce
#else: borrifar aroma comum
#funcao time.sleep(360): depois de 1h tudo volta pra True

import os, time
nF = 0
nM = 0

class Pessoas:
    #Pessoas que podem circular nas salas
    def __init__(self, F, M, ND, docente, discente):
        Clara    = (F, discente)
        Claudio  = (M, discente)
        Luis     = (M, discente)
        Paloma   = (F, discente)
        Valvan   = (ND, discente)
        Gabriela = (F, discente)
        Manuel   = (M, discente)
        Clarice  = (F, discente)
        Carlos   = (M, discente)
        Aluisio  = (M, discente)
        Pamela   = (F, discente)
        Leona    = (F, discente)
        Gloria   = (F, discente)
        Albert   = (M, discente)
        Manuele  = (F, discente)
        Patricia = (F, docente)
        Valeria  = (F, docente)
        Igor     = (M, docente)
        Renato   = (M, docente)
        Rayanne  = (F, docente)

class Sala:
    #Ambiente
    def __init__(self):
        self.recepcao = False
        self.sala0 = False
        self.sala1 = False
        self.sala2 = False

    def averiguar (self, posicao):
        print('========================')
        print('      AROMATIZADOR      ')
        print('========================')

        if self.recepcao == False and self.sala0 == False and self.sala1 == False and self.sala2 == False:

            print('Tudo cheiroso')

        elif self.sala0 == True:
  
            print('Borrifar sala 0')

        elif self.sala1 == True:

            print('Borrifar sala 1')

        elif self.sala2 == True:

            print('Borrifar sala 2')  

        else:
            pass

class Aromatizador:
    #Agente
    def __init__(self):
        self.posicao = 0
    
    #Receptores e Atuadores
    def movimentar (self, recepcao, sala0, sala1, sala2, sala3):
        if self.posicao == 0 and recepcao == False:
            self.posição = 1
        elif self.posicao == 1 and sala0 == False:
            self.posição = 2
        elif self.posicao == 2 and sala1 == False:
            self.posicao = 3
        elif self.posicao == 3 and sala2 == False:
            self.posicao = 0     
        else:
            pass
    
    #aqui é preciso contar a incidencia de F e M na lista de pessoas e comparar qual dos duas é maior
    def borrifar (self, recepcao, sala0, sala1, sala2) :
        if self.posicao == 0 and recepcao == True:
            if nF >= nM:
                print ('Recepção borrifada com arome doce.')
                recepcao = False
            else:
                print ('Recepção borrifada com arome comum.')
                recepcao = False
        elif self.posicao == 1 and sala0 == True:
            if nF > nM:
                print ('Sala0 borrifada com arome doce.')
                recepcao = False
            else:
                print ('Sala0 borrifada com arome comum.')
                recepcao = False
        elif self.posicao == 2 and sala1 == True:
            if nF > nM:
                print ('Sala1 borrifada com arome doce.')
                recepcao = False
            else:
                print ('Sala1 borrifada com arome comum.')
                recepcao = False
        elif self.posicao == 3 and sala2 == True:
            if nF > nM:
                print ('Sala2 borrifada com arome doce.')
                recepcao = False
            else:
                print ('Sala2 borrifada com arome comum.')
                recepcao = False
        else:
            Aromatizador.movimentar(recepcao, sala0, sala1, sala2)
            return recepcao, sala0, sala1, sala2

sala = Sala()
aromatizador = Aromatizador()
