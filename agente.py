# listas
# class Alunos: clara = (F, discente), claudio = (M, discente), luis = (M, discente), paloma = (F,discente), valvan = (, discente), gabriela = (F, discente), manuel = (F, discente)
#if nF > nM: borrifar aroma doce
#else: borrifar aroma comum
#funcao time.sleep(360): depois de 1h tudo volta pra True

import os, time

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

        if self.recepcao = False and self.sala0 == False and self.sala1 == False and self.sala2 == False:

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
            aromatizador.movimentar(ladoA, ladoB)
            return ladoA, ladoB

#menu de opções
def menu_opcoes():
    print('--------------------')
    print('(1) Sujar Esquerda')
    print('(2) Sujar Direita')
    print('(3) Agir')
    print('(4) Encerrar')
    print('--------------------')

    try:
        opcao = int(input('Opção: '))
    except:
        print('Opção inválida')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        sala.mostrar(aspirador.posicao)
        menu_opcoes()

    if opcao == 1:
        sala.ladoA = True
        return True
    elif opcao == 2:
        sala.ladoB = True
    elif opcao == 3:
        sala.ladoA, sala.ladoB = aspirador.limpar(sala.ladoA, sala.ladoB)
    elif opcao == 4:
        return False
    else:
        print('Opção inválida.')
        time.sleep(2)
        os.system('cls' if os.name == 'nt' else 'clear')
        sala.mostra(aspirador.posicao)
        menu_opcoes()

sala = Sala()
aspirador = Aspirador()

prog = True
while prog == True:
    os.system('cls' if os.name == 'nt' else 'clear')
    sala.mostrar(aspirador.posicao)
    prog = menu_opcoes()