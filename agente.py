import os, time
import array as arr 
import random
import time

#lista das pessoas que vao circular na coordencao

pessoas = [
    ['Clara',    'F',  'discente'],
    ['Claudio',  'M',  'discente'],
    ['Luis',     'M',  'discente'],
    ['Paloma',   'F',  'discente'],
    ['Valvan',   'ND', 'discente'],
    ['Gabriela', 'M',  'discente'],
    ['Manuel',   'M',  'discente'],
    ['Clarice',  'F',  'discente'],
    ['Carlos',   'M',  'discente'],
    ['Aluisio',  'M',  'discente'],
    ['Pamela',   'F',  'discente'],
    ['Leona',    'F',  'discente'],
    ['Gloria',   'F',  'discente'],
    ['Albert',   'M',  'discente'],
    ['Carlos',   'M',  'discente'],
    ['Manuele',  'F',  'discente'],
    ['Patricia', 'F',  'docente'],
    ['Valeria',  'F',  'docente'],
    ['Igor',     'M',  'docente'],
    ['Renato',   'M',  'docente'],
    ['Rayanne',  'F',  'docente']
]

#listas a serem preenchidas com quem tiver em cada sala

recepcao = []
sala1    = []
sala2    = []
sala3    = []

# função pra percorrer a lista de pessoas e colocar aleatoriamente todas as pessoas em cada sala
# no final ja é comparado se tem mais M ou F na sala, assim dando o comando de borrifar tal aroma nas salas, talves seja melhor separar
# isso pra nao ficar em um unico bloco o codigo inteiro

def movimento_na_coordenacao():
    for i in range(0,9):

    for i in range(len(pessoas)):

        numeroSala = random.randint(0,3)
        
        if numeroSala == 0:
            recepcao.append(pessoas[i])
        
        elif numeroSala == 1:
            sala1.append(pessoas[i])
        
        elif numeroSala == 2:
            sala2.append(pessoas[i])
            
        elif numeroSala == 3:
            sala3.append(pessoas[i])

    recepcaoM = 0;
    recepcaoF = 0;

    for i in range(len(recepcao)):
        if recepcao[i][1] == 'M':
            recepcaoM += 1;
            print(recepcao[i])
        else:
            recepcaoF += 1;
            print(recepcao[i])

    if recepcaoM > recepcaoF:
        #faltou alterar valor boleane da recepcao
        print('aroma comum borrifado na recepcao.')
        
    else:
        print('aroma doce borrifado na recepcao.')
    
    #repetir esse for pras outras salas
    
    #aqui os valores são resetados pra que o processo seja refeito sem colocar a mesma pessoas 2x na mesma sala ou ao mesmo tempo em salas diferentes
    
    recepcao = []
    sala1 = []
    sala2 = []
    sala3 = []

    time.sleep(1)

#aqui a gente vai checar se a sala precisa ser borrifada ou nao

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

#aqui vai ser controlado o deslocamento do borrifador nas salas

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
    

    ######### nao é mais preciso que seja feito dessa forma, pois acima o codigo foi alterado,  ##################
    ######### mas como peciso ir pra ufma nao consegui alterar o fim do codigo <3               ##################


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
