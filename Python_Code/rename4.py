globals().clear()
import os
def listToString(s):
    # initialize an empty string
    str1 = " "
# return string
    return (str1.join(s))

os.chdir("E:/unipd course/ok course/PROGETTAZIONE DI SISTEMI DI CONTROLLO 2019-2020 - PROF. ROBERTO OBOE di DTG/New folder1")
for f in os.listdir():
    print(len(os.listdir()))
    f_title, file_ext = os.path.splitext(f)
    print(f_title)
    #re = f_title.replace(",", " ")
    #f_title = re.split()
    f_title1 = f_title.split()[1:]
    new_name = '{}{}'.format((listToString(f_title1)), file_ext.strip())
    print(new_name)
    os.rename(f, new_name)