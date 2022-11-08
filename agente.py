# listas
# class Alunos: clara = (F, discente), claudio = (M, discente), luis = (M, discente), paloma = (F,discente), valvan = (, discente), gabriela = (F, discente), manuel = (F, discente)
#if nF > nM: borrifar aroma doce
#else: borrifar aroma comum
#

import os, time

class Sala:
    #Ambiente
    def __init__(self):
        self.recepcao = False
        self.sala0 = False
        self.sala1 = False
        self.sala2 = False
        self.sala3 = False

    def mostrar (self, posicao):
        print('========================')
        print('      AROMATIZADOR      ')
        print('========================')

        if self.recepcao = False and self.sala0 == False and self.sala1 == False and self.sala2 == False and self.sala3 == False:

            print('Tudo cheiroso')

        elif self.sala0 == True:
  
            print('Borrifar sala 0')

        elif self.sala1 == True:

            print('Borrifar sala 1')

        elif self.sala2 == True:

            print('Borrifar sala 2')

        elif self.sala3 == True:

            print('Borrifar sala 3')    

        else:
            pass

class Aromatizador:
    #Agente
    def __init__(self):
        self.posicao = 0
    
    #Receptores e Atuadores
    def movimentar (self, sala0, sala1, sala2, sala3):
        if self.posicao == 0 and sala0 == False:
            self.posição = 2
        elif self.posicao == 2 and sala1 == False:
            self.posicao = 4
        elif self.posicao == 4 and sala2 == False:
            self.posicao = 5
        elif self.posicao == 5 and sala3 == False:
            self.posicao = 4        
        else:
            pass
    
    def limpar (self, ladoA, ladoB) :
        if self.posicao == 0 and ladoA == True:
            if ladoB == True:
                return False, True
            else:
                return False, False
        elif self.posicao == 1 and ladoB == True:
            if ladoA == True:
                return True, False
            else:
                return False, False
        else:
            aspirador.movimentar(ladoA, ladoB)
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
