import time
import os

# while 16 == 16:
ti=time.localtime()
anno = ti[0]
ora = ti[-6]
hour=ti.tm_hour
# print(hour)
if ora == 9 :
    #   print("b is greater than a")
    #   ti

        print(hour)
        minuti =ti[-5]
        #   min = ti.tm_min

        if minuti == 36:
         print(" sono giusti ")
         #execfile("deviese.py ")
         #os.system("python deviese.py 1")
         os.system("python openzoomre.py 1")
         #          break
