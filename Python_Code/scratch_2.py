globals().clear()
import os
def listToString(s):
    # initialize an empty string
    str1 = " "
# return string
    return (str1.join(s))

os.chdir("E:/unipd course/ok course/POWER ELECTRONICS DESIGN 2021 di dei ok/Lezione")
#os.chdir("E:/unipd course/ok course/ADVANCED CONTROL SYSTEMS 2020-2021 - PROF. ALESSANDRO BEGHI/Lezione")
for f in os.listdir():
    print(len(os.listdir()))
    f_title, file_ext = os.path.splitext(f)
    print(f_title)
    re = f_title.replace(",", " ")
    f_title = re.split()
    f_title1 = re.split()[1:]
    new_name = '{}{}'.format((listToString(f_title1)), file_ext.strip())
    print(new_name)
    os.rename(f, new_name)