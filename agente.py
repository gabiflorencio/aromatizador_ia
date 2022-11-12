      else:
        print('aroma doce borrifado na recepcao.')
        recepcaoF = 1
def qual_aroma_sala0():
    sala0M = 0
    sala0F = 0
    for i in range(len(sala0)):
        if sala0[i][1] == 'M':
            sala0M += 1
        else:
            sala0F += 1
    if sala0M > sala0F:
        print('aroma comum borrifado na sala 0.')
        sala0M = 1
    else:
        print('aroma doce borrifado na sala 0.')
        sala0F = 1
def qual_aroma_sala1():
     sala1M = 0
     sala1F = 0
     for i in range(len(sala1)):
         if sala1[i][1] == 'M':
             sala1M += 1
         else:
             sala1F += 1
     if sala1M > sala1F:
         print('aroma comum borrifado na sala 1.')
         sala1M = 1
     else:
         print('aroma doce borrifado na sala 1.')
         sala1F = 1
def qual_aroma_sala2():
     sala2M = 0
     sala2F = 0
     for i in range(len(sala2)):
         if sala2[i][1] == 'M':
             sala2M += 1
         else:
             sala2F += 1
     if sala2M > sala2F:
         print('aroma comum borrifado na sala 2.')
         sala2M = 1
     else:
         print('aroma doce borrifado na sala 2.')
         sala2F = 1