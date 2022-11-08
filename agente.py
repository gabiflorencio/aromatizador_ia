import os, time

class Sala:
    #Ambiente
    def __init__(self):
        self.ladoA = False
        self.ladoB = False

    def mostrar (self, posicao):
        print('========================')
        print('      ASPIRADOR         ')
        print('========================')
        print('------------------------')
        if posicao == 0:
            print('aspirador        \n')
        elif posicao == 1:
            print('       aspirador \n')
        else:
            pass

        if self.ladoA == False and self.ladoB == False:
            print('////////////////////')
            print(' Limpo        Limpo ')
            print('////////////////////')
        elif self.ladoA == True and self.ladoB == False:
            print('////////////////////')
            print(' Sujo         Limpo ')
            print('////////////////////')
        elif self.ladoA == False and self.ladoB == True:
            print('////////////////////')
            print(' Limpo         Sujo ')
            print('////////////////////')
        elif self.ladoA == True and self.ladoB == True:
            print('////////////////////')
            print(' Sujo          Sujo ')
            print('////////////////////')
        else:
            pass

class Aspirador:
    #Agente
    def __init__(self):
        self.posicao = 0
    
    #Receptores e Atuadores
    def movimentar (self, ladoA, ladoB):
        if self.posicao == 0 and ladoA == False:
            self.posição = 1
        elif self.posicao == 1 and ladoB == False:
            self.posicao = 0
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
