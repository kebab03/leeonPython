globals().clear()
import os
os.chdir("E:/unipd course/ok course/ADVANCED CONTROL SYSTEMS 2020-2021 - PROF. ALESSANDRO BEGHI/Lezione")
for f in os.listdir():
    print(len(os.listdir()))
    f_title, file_ext = os.path.splitext(f)
    print(f_title)
    ind = f_title.find('L')
    print(ind)
    #f_title.replace(",", " ")

    print('{}{}'.format(f_title.strip()[ind:],file_ext.strip()))
    new_name = '{}{}'.format(f_title.strip()[ind:],file_ext.strip())
    #new_name='{}{}'.format(f_title.replace(","," ").strip()[11:],file_ext.strip())
    print(new_name)
    os.rename(f,new_name)