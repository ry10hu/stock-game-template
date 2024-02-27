import time
import random
import stocktable


def timeloop():
  while True:
    for x in range(0, len(stocktable.table)):
      number = random.randint(-20, 20)
      if stocktable.table[x][1] + number > 0:
        stocktable.table[x][1] += number
    time.sleep(60)
    
