globals().clear()
import os
os.chdir("E:/unipd course/PROGETTO E SIMULAZIONE DI CIRCUITI ELETTRONICI 2021/Lezione")
#os.chdir("E:/unipd course/ANTENNAS AND WIRELESS PROPAGATION - ANTENNE E PROPAGAZIONE WIRELESS/try")
for f in os.listdir():
    print(len(os.listdir()))
    f_title, file_ext = os.path.splitext(f)
    print(f_title)
    #f_title.replace(",", " ")

     #print('{}{}'.format(f_title.strip()[11:],file_ext.strip()))
    new_name='{}{}'.format(f_title.replace(","," ").strip()[11:],file_ext.strip())
    print(new_name)
    os.rename(f, new_name)