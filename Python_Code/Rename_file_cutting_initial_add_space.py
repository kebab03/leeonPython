globals().clear()
import os

 # os.chdir('E:\unipd course\GENERAZIONE E ACCUMULO DI ENERGIA ELETTRICA DA FONTI RINNOVABILI 2020-2021\try')
os.chdir('E:/unipd course/GENERAZIONE E ACCUMULO DI ENERGIA ELETTRICA DA FONTI RINNOVABILI 2020-2021/try')
for f in os.listdir():

    print(len(os.listdir()))
    # file_name, file_ext = os.path.splitext(f)
    f_title, file_ext = os.path.splitext(f)
    print(f_title)
    #f_title, f_course, f_number = file_name.split('-')
     #print(f_title.strip()[11:])
     #print('{}{}'.format(f_title.strip()[11:],file_ext.strip()))
    # new_name='{}{}'.format(f_title.strip()[11:],file_ext.strip())
    na=f_title.strip()[:7] + ' ' + f_title.strip()[7:]
    new_name = '{}{}'.format(na, file_ext.strip())
    print(new_name)
    os.rename(f, new_name)