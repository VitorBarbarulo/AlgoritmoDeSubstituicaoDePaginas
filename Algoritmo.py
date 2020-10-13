# Create by Vitor Fernandes Barbarulo - D6929J0 - SI6P68

import time
memoria = [0, 0, 0]
paginas = [7, 0, 1, 2, 0, 3, 0, 4, 2, 3, 0, 3, 2, 1, 2, 0, 1, 7, 0, 1]
trocaPaginas = 0
trocaMemoria = 0
while True:
  if trocaMemoria < 3:
    memoria[trocaMemoria] = paginas[0]
    for n in range(len(paginas)):
      if n < len(paginas)-1:
        paginas[n] = paginas[n+1]
    trocaMemoria += 1
    paginas.pop()
  else:
    trocaMemoria = 0
    memoria[trocaMemoria] = paginas[1]
    for n in range(len(paginas)):
      if n < len(paginas)-1:
        paginas[n] = paginas[n+1]
    trocaMemoria += 1
    paginas.pop()
  trocaPaginas += 1
  print(memoria)
  print(paginas)
  time.sleep(1)