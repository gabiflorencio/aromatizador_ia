import time
import random
import time

#listas das pessoas que vao circular na coordencao

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

# listas a serem preenchidas com quem tiver em cada sala

recepcao = []
sala0    = []
sala1    = []
sala2    = []
recepcaoM = 0
recepcaoF = 0
sala0M = 0
sala0F = 0
sala1M = 0
sala1F = 0
sala2M = 0
sala2F = 0

# função pra percorrer a lista de pessoas e colocar aleatoriamente todas as pessoas em cada sala, de 0 a 4 faz com que 
# nem todos estejam nas 4 salas.

def movimento_na_coordenacao():
    for i in range(len(pessoas)):

        numeroSala = random.randint(0,4)
        
        if numeroSala == 0:
            recepcao.append(pessoas[i])
        
        elif numeroSala == 1:
            sala0.append(pessoas[i])
        
        elif numeroSala == 2:
            sala1.append(pessoas[i])
            
        elif numeroSala == 3:
            sala2.append(pessoas[i])
        else:  
            pass

# comparando se tem mais M ou F na sala, assim dando o comando de borrifar um aroma nas salas, repetindo-se o processo
# 10 vezes, cada vez com com a ordem diferente de pessoas em cada sala

def qual_aroma():

    def qual_aroma_recepcao():

        # Comparando se sem mais M ou F na recpcao

        for i in range(len(recepcao)):
            if recepcao[i][1] == 'M':
                recepcaoM += 1
                print(recepcao[i])
            else:
                recepcaoF += 1
                print(recepcao[i])

        if recepcaoM > recepcaoF:
            print('aroma comum borrifado na recepcao.')
            
        else:
            print('aroma doce borrifado na recepcao.')

    def qual_aroma_sala0():
        
        for i in range(len(sala0)):
            if sala0[i][1] == 'M':
                sala0M += 1
                print(sala0[i])
            else:
                sala0F += 1
                print(sala0[i])

        if sala0M > sala0F:
            print('aroma comum borrifado na sala 0.')
            
        else:
            print('aroma doce borrifado na sala 0.')

    def qual_aroma_sala1():
        
        for i in range(len(sala1)):
            if sala1[i][1] == 'M':
                sala1M += 1
                print(sala1[i])
            else:
                sala1F += 1
                print(sala1[i])

        if sala1M > sala1F:
            print('aroma comum borrifado na sala 1.')
                
        else:
            print('aroma doce borrifado na sala 1.')

    def qual_aroma_sala2():
        
        for i in range(len(sala2)):
            if sala2[i][1] == 'M':
                sala2M += 1
                print(sala2[i])
            else:
                sala2F += 1
                print(sala2[i])

        if sala2M > sala2F:
            print('aroma comum borrifado na sala 2.')
            
        else:
            print('aroma doce borrifado na sala 2.')
    

# time.sleep(1)

#aqui a gente vai checar se a sala precisa ser borrifada ou nao

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
        if recepcaoF >= recepcaoM:
            print ('Recepção borrifada com arome doce.')
            recepcao = False
        else:
            print ('Recepção borrifada com arome comum.')
            recepcao = False
    elif self.posicao == 1 and sala0 == True:
        if sala0F > sala0M:
            print ('Sala0 borrifada com arome doce.')
            recepcao = False
        else:
            print ('Sala0 borrifada com arome comum.')
            recepcao = False
    elif self.posicao == 2 and sala1 == True:
        if sala1F > sala1M:
            print ('Sala1 borrifada com arome doce.')
            recepcao = False
        else:
            print ('Sala1 borrifada com arome comum.')
            recepcao = False
    elif self.posicao == 3 and sala2 == True:
        if sala2F > sala2M:
            print ('Sala2 borrifada com arome doce.')
            recepcao = False
        else:
            print ('Sala2 borrifada com arome comum.')
            recepcao = False
    else:
        return recepcao, sala0, sala1, sala2
