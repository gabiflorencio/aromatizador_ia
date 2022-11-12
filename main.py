import time
import random
from ambiente import *
from agente import *
# função pra percorrer a lista de pessoas e colocar aleatoriamente todas as pessoas em cada sala, de 0 a 4 faz com que 
# nem todos estejam nas 4 salas.
for i in range(0,5):
  movimento_na_coordenacao()
  qual_aroma_recepcao()
  qual_aroma_sala0()
  qual_aroma_sala1()
  qual_aroma_sala2()
  print('=====================================')
  time.sleep(1)
  