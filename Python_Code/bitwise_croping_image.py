C:\Users\leeon\PycharmProjects\upl\venv\Scripts\python.exe
"C:\Program Files\JetBrains\PyCharm Community Edition 2020.1.3\plugins\python-ce\helpers\pydev\pydevconsole.py" - -mode = client - -port = 50432
import sys;

print('Python %s on %s' % (sys.version, sys.platform))
sys.path.extend(['C:\\Users\\leeon\\PycharmProjects\\tutorial\\venv',
                 'C:\\Users\\leeon\\PycharmProjects\\voiceAssistent\\venv\\Lib',
                 'C:\\Users\\leeon\\PycharmProjects\\youdon\\venv', 'C:\\Users\\leeon\\PycharmProjects\\youtube',
                 'C:/Users/leeon/PycharmProjects/tutorial/venv'])
Python
3.8
.3(tags / v3
.8
.3: 6
f8c832, May
13
2020, 22: 37:02) [MSC v.1924 64 bit(AMD64)]
Type
'copyright', 'credits' or 'license'
for more information
    IPython
    7.18
    .1 - - An
    enhanced
    Interactive
    Python.Type
    '?'
    for help.
        PyDev
    console: using
    IPython
    7.18
    .1
Python
3.8
.3(tags / v3
.8
.3: 6
f8c832, May
13
2020, 22: 37:02) [MSC v.1924 64 bit(AMD64)]
on
win32
import cv2

...:
import numpy as np

...:
from matplotlib import pyplot as plt

...:
...: img = cv2.imread("C:/Users/leeon/Pictures/Atest-tesseract/image.jpg", cv2.IMREAD_GRAYSCALE)
...: lap = cv2.Laplacian(img, cv2.CV_64F, ksize=3)
...: lap = np.uint8(np.absolute(lap))
...: sobelX = cv2.Sobel(img, cv2.CV_64F, 1, 0)
...: sobelY = cv2.Sobel(img, cv2.CV_64F, 0, 1)
...: edges = cv2.Canny(img, 100, 200)
...:
...: sobelX = np.uint8(np.absolute(sobelX))
...: sobelY = np.uint8(np.absolute(sobelY))
...:
...: sobelCombined = cv2.bitwise_or(sobelX, sobelY)
...:
...: titles = ['image', 'Laplacian', 'sobelX', 'sobelY', 'sobelCombined', 'Canny']
...: images = [img, lap, sobelX, sobelY, sobelCombined, edges]
...:
for i in range(6):
    ...: plt.subplot(2, 3, i + 1), plt.imshow(images[i], 'gray')
...: plt.title(titles[i])
...: plt.xticks([]), plt.yticks([])
...:
...: plt.show()
Backend
TkAgg is interactive
backend.Turning
interactive
mode
on.
import cv2

...:
import numpy as np

...:
from matplotlib import pyplot as plt

...: direc = 'C:/Users/leeon/Pictures/Atest-tesseract/'
...: name = 'image'
...: name_templet = name + '_templet'
...: path_src = direc + name + '.jpg'
...: path_templet = direc + name_templet + '.jpg'
...:
...:  # print(path_src)
...:  # print(path_templet)
...:
...: img_rgb = cv2.imread(path_src)
...: print('img_rgb', img_rgb.shape)
...: img_Re = cv2.resize(img_rgb, (800, 880))
...:
...:  # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
...:
...: img_gray = cv2.cvtColor(img_Re, cv2.COLOR_BGR2GRAY)
...: template_Old = cv2.imread(path_templet, 0)
...:  # template=cv2.resize(template_Old,(100,50))
...:  # template=cv2.resize(template_Old,(320,80))
...:
...:
...: (thresh, blackAndWhiteImage) = cv2.threshold(template_Old, 120, 255, cv2.THRESH_BINARY)
...:  # cv2.imshow('Black white image', blackAndWhiteImage)
...:
...: template = blackAndWhiteImage
...:  # template=cv2.resize(template,(200,60))
...: cv2.imshow('templet_old', template_Old)
img_rgb(4608, 3456, 3)
import cv2

...:
import numpy as np

...:
from matplotlib import pyplot as plt

...: direc = 'C:/Users/leeon/Pictures/Atest-tesseract/'
...: name = 'image'
...: name_templet = name + '_templet'
...: path_src = direc + name + '.jpg'
...: path_templet = direc + name_templet + '.jpg'
...:
...:  # print(path_src)
...:  # print(path_templet)
...:
...: img_rgb = cv2.imread(path_src)
...: print('img_rgb', img_rgb.shape)
...: img_Re = cv2.resize(img_rgb, (800, 880))
...:
...:  # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
...:
...: img_gray = cv2.cvtColor(img_Re, cv2.COLOR_BGR2GRAY)
...: template_Old = cv2.imread(path_templet, 0)
...:  # template=cv2.resize(template_Old,(100,50))
...:  # template=cv2.resize(template_Old,(320,80))
...:
...:
...: (thresh, blackAndWhiteImage) = cv2.threshold(template_Old, 120, 255, cv2.THRESH_BINARY)
...: cv2.imshow('Black white image', blackAndWhiteImage)
...:
...: template = blackAndWhiteImage
...:  # template=cv2.resize(template,(200,60))
...: cv2.imshow('templet_old', template_Old)
img_rgb(4608, 3456, 3)
img_Re = cv2.resize(img_rgb, (800, 880))
cv2.imshow('Black white image', blackAndWhiteImage)
img_Re1 = cv2.resize(template_Old, (800, 880))
cv2.imshow('Black white image_re', template_Old)
gloab().clear()
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-9-a108d20d4e86>", line
1, in < module >
gloab().clear()
NameError: name
'gloab' is not defined
global
().clear()
File
"<ipython-input-10-5f7acbb38a26>", line
1
global
().clear()
^
SyntaxError: invalid
syntax
Global().clear()
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-11-f1cce6a9f0f7>", line
1, in < module >
Global().clear()
NameError: name
'Global' is not defined
Global().Clear()
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-12-5f162d51bb6f>", line
1, in < module >
Global().Clear()
NameError: name
'Global' is not defined
globals().clear()
globals().clear()
...:
import cv2

...:
import numpy as np

...:
from matplotlib import pyplot as plt

...: direc = 'C:/Users/leeon/Pictures/Atest-tesseract/'
...: name = 'image'
...: name_templet = name + '_templet'
...: path_src = direc + name + '.jpg'
...: path_templet = direc + name_templet + '.jpg'
...:
...:  # print(path_src)
...:  # print(path_templet)
...:
...: img_rgb = cv2.imread(path_src)
...: print('img_rgb', img_rgb.shape)
...: img_Re = cv2.resize(img_rgb, (800, 880))
...:
...:  # img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
...:
...: img_gray = cv2.cvtColor(img_Re, cv2.COLOR_BGR2GRAY)
...: template_Old = cv2.imread(path_templet, 0)
...:  # template=cv2.resize(template_Old,(100,50))
...:  # template=cv2.resize(template_Old,(320,80))
...:
...:
...: (thresh, blackAndWhiteImage) = cv2.threshold(template_Old, 120, 255, cv2.THRESH_BINARY)
...:  # cv2.imshow('Black white image', blackAndWhiteImage)
...:
...: template = blackAndWhiteImage
...:  # template=cv2.resize(template,(200,60))
...: cv2.imshow('Black white image_templet', template)
...:
...: print('template_shape:::', template.shape)
...: print('img_Re_shape::', img_Re.shape)
...: print('img_Re_shape[::]::', img_Re.shape[::])
...: cv2.imshow('template', template)
...: cv2.imshow('img_Re', img_Re)
...:
...: cv2.imshow('img_gray', img_gray)
...:


def nothing(x):
    ...: print(x)


...:  # grayImage = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
...: cv2.namedWindow("In_Trackbars_Window")
...: cv2.resizeWindow("In_Trackbars_Window", 360, 240)
...: cv2.createTrackbar("Name_of_Threshold1", "In_Trackbars_Window", 0, 255, nothing)
...: cv2.createTrackbar("Threshold2", "In_Trackbars_Window", 0, 255, nothing)
...:
...:
...:
...:  # (thresh, blackAndWhiteImage) = cv2.threshold(template_Old, Threshold1, Threshold2, cv2.THRESH_BINARY)
...:  # while   True:
...:  # (thresh, blackAndWhiteImage) = cv2.threshold(template_Old, 127, 255, cv2.THRESH_BINARY)
...:  # cv2.imshow('Black white image', blackAndWhiteImage)
...:  # cv2.imshow('Original image', originalImage)
...:
...:  # cv2.waitKey(0)
...:  # cv2.destroyAllWindows()
...:
...:
...:
...:
...:
...:
...:
...: h, w = template.shape[::]
...: print('h::', h)
...: print('w:::', w)
...:  # h=h_s/2
...:  # w=w_s/2
...:
...:  # methods available: ['cv2.TM_CCOEFF', 'cv2.TM_CCOEFF_NORMED', 'cv2.TM_CCORR',
...:  # 'cv2.TM_CCORR_NORMED', 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']
...:
...: res = cv2.matchTemplate(img_gray, template, cv2.TM_SQDIFF)
...:  # For TM_SQDIFF, Good match yields minimum value; bad match yields large values
...:  # For all others it is exactly opposite, max value = good fit.
...:  # plt.imshow(res, cmap='gray')
...:  # print('res:',res)
...:  # print('res_shape:',res.shape)
...:  # print('res_dtype:',res.dtype)
...: min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
...: print('min_loc:', min_loc)
...: top_left = min_loc  # Change to max_loc for all except for TM_SQDIFF
...: bottom_right = (top_left[0] + w, top_left[1] + h)
...: cv2.rectangle(img_gray, top_left, bottom_right, 255, 1)  # White rectangle with thickness 2.
...:
...: cv2.imshow("Matched image", img_gray)
...:  # so=0
...:  # while   True:
...:  # Threshold1 = cv2.getTrackbarPos("Name_of_Threshold1", "In_Trackbars_Window")
...:  # Threshold2 = cv2.getTrackbarPos("Threshold2", "In_Trackbars_Window")
...:  # print('Threshold1:', Threshold1)
...:  # print('Threshold2:', Threshold2)
...:  # (thresh, blackAndWhiteImage) = cv2.threshold(template_Old, 120, 255, cv2.THRESH_BINARY)
...:  # cv2.imshow('Black white image', blackAndWhiteImage)
...:  #
...:  # print(so)
...:  # so=so+1
...: cv2.waitKey(0)
...:
...: cv2.destroyAllWindows()
...:  # key=cv2.waitKey(1)
...:  # if key==27:
...:  # break
...:  # cv2.destroyAllWindows()
img_rgb(4608, 3456, 3)
template_shape::: (684, 692)
img_Re_shape:: (880, 800, 3)
img_Re_shape[::]:: (880, 800, 3)
h:: 684
w::: 692
min_loc: (67, 73)
globals().clear()
...:
import cv2

...:
import numpy as np

...:
import pytesseract

...:
from PIL import Image

...:
from pytesseract import image_to_string

src_path = 'C:/Users/leeon/Pictures/Atest-tesseract/image.jpg'
img = cv2.imread(src_path)
cv2.imshow((img))
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-18-5f757e961c79>", line
1, in < module >
cv2.imshow((img))
TypeError: imshow()
missing
required
argument
'mat'(pos
2)
cv2.imshow(img)
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-19-3594ed6a38c9>", line
1, in < module >
cv2.imshow(img)
TypeError: imshow()
missing
required
argument
'mat'(pos
2)
cv2.imshow('img', img)
img_Re = cv2.resize(img, (880, 800))
cv2.imshow('img_Re', img_Re)
img_Re = cv2.resize(img, (800, 880))
cv2.imshow('img_Re', img_Re)
heightImg = 800
widthImg = 880
imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)
cv2.imshow('imgBlank', imgBlank)
widthImg = 800
heightImg = 880
imgBlank = np.zeros((heightImg, widthImg, 3), np.uint8)
cv2.imshow('imgBlank', imgBlank)
imgBlank_mask = img[600:heightImg, :]
...:
cv2.imshow('imgBlank_mask', imgBlank_mask)
imgBlank_mask = imgBlank[600:heightImg, :]
...:
cv2.imshow('imgBlank_mask', imgBlank_mask)
cv2.imshow('img_Re', img_Re)
imgBlank_frame = np.zeros((heightImg, widthImg, 3), np.uint8)
tr = cv2.bitwise_or(imgBlank_frame, imgBlank_mask)
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-39-eca3da928b8f>", line
1, in < module >
tr = cv2.bitwise_or(imgBlank_frame, imgBlank_mask)
cv2.error: OpenCV(4.4
.0) C:\Users\appveyor\AppData\Local\Temp\1\pip - req - build - k8sx3e60\opencv\modules\core\src\arithm.cpp: 234: error: (
    -209:Sizes of input arguments do not match)
The
operation is neither
'array op array'(where
arrays
have
the
same
size and type), nor
'array op scalar', nor
'scalar op array' in function
'cv::binary_op'
imgBlank_mask1 = cv2.rectangle(imgBlank_frame, (0, 600)(widthImg, heightImg), (255, 255, 255), -1)
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
<>:1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< ipython - input - 40 - 913
dbc92bea9 >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
imgBlank_mask1 = cv2.rectangle(imgBlank_frame, (0, 600)(widthImg, heightImg), (255, 255, 255), -1)
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-40-913dbc92bea9>", line
1, in < module >
imgBlank_mask1 = cv2.rectangle(imgBlank_frame, (0, 600)(widthImg, heightImg), (255, 255, 255), -1)
TypeError: 'tuple'
object is not callable
cv2.imshow('imgBlank_mask', imgBlank_mask)
cv2.imshow('imgBlank_frame', imgBlank_frame)
...:
imgBlank_mask1 = cv2.rectangle(imgBlank_frame, (0, 600)(widthImg, heightImg), (255, 255, 255), -1)
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
<>:1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< ipython - input - 43 - 913
dbc92bea9 >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
imgBlank_mask1 = cv2.rectangle(imgBlank_frame, (0, 600)(widthImg, heightImg), (255, 255, 255), -1)
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-43-913dbc92bea9>", line
1, in < module >
imgBlank_mask1 = cv2.rectangle(imgBlank_frame, (0, 600)(widthImg, heightImg), (255, 255, 255), -1)
TypeError: 'tuple'
object is not callable
imgBlank_mask1 = cv2.rectangle(imgBlank_frame, (2, 600)(widthImg, heightImg), (255, 255, 255), -1)
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
<>:1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< ipython - input - 44 - 5051
eb2d1446 >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
imgBlank_mask1 = cv2.rectangle(imgBlank_frame, (2, 600)(widthImg, heightImg), (255, 255, 255), -1)
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-44-5051eb2d1446>", line
1, in < module >
imgBlank_mask1 = cv2.rectangle(imgBlank_frame, (2, 600)(widthImg, heightImg), (255, 255, 255), -1)
TypeError: 'tuple'
object is not callable
imgBlank_mask1 = cv2.rectangle(imgBlank_frame, (2, 600), (widthImg, heightImg), (255, 255, 255), -1)
cv2.imshow('imgBlank_mask1', imgBlank_mask1)
tr = cv2.bitwise_or(img_Re, imgBlank_mask1)
cv2.imshow('tr', tr)
tr_xor = cv2.bitwise_xor(img_Re, imgBlank_mask1)
cv2.imshow('tr_xor', tr_xor)
tr_and = cv2.bitwise_and(img_Re, imgBlank_mask1)
cv2.imshow('tr_and', tr_and)
cv2.imwrite(src_path + "Parte_sotto.png", tr_and)
Out[53]: Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-53-03a0deedc207>", line
1, in < module >
cv2.imwrite(src_path + "Parte_sotto.png", tr_and)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
263, in __call__
self.update_user_ns(result)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
201, in update_user_ns
if self.cache_size and result is not self.shell.user_ns['_oh']:
    KeyError: '_oh'
cv2.imwrite('C:/Users/leeon/Pictures/Atest-tesseract/' + "Parte_sotto.png", tr_and)
Out[54]: Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-54-a90caf918ca8>", line
1, in < module >
cv2.imwrite('C:/Users/leeon/Pictures/Atest-tesseract/' + "Parte_sotto.png", tr_and)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
263, in __call__
self.update_user_ns(result)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
201, in update_user_ns
if self.cache_size and result is not self.shell.user_ns['_oh']:
    KeyError: '_oh'
cv2.imwrite('C:/Users/leeon/Pictures/Atest-tesseract/' + 'Parte_sotto.png', tr_and)
Out[55]: Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-55-29bf1591f9ed>", line
1, in < module >
cv2.imwrite('C:/Users/leeon/Pictures/Atest-tesseract/' + 'Parte_sotto.png', tr_and)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
263, in __call__
self.update_user_ns(result)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
201, in update_user_ns
if self.cache_size and result is not self.shell.user_ns['_oh']:
    KeyError: '_oh'
cv2.imwrite('D:\azio' + 'Parte_sotto.png', tr_and)
Out[56]: Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-56-6edc826da1ee>", line
1, in < module >
cv2.imwrite('D:\azio' + 'Parte_sotto.png', tr_and)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
263, in __call__
self.update_user_ns(result)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
201, in update_user_ns
if self.cache_size and result is not self.shell.user_ns['_oh']:
    KeyError: '_oh'
cv2.imwrite('D://azio' + 'Parte_sotto.png', tr_and)
Out[57]: Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-57-fe14ae1e96d0>", line
1, in < module >
cv2.imwrite('D://azio' + 'Parte_sotto.png', tr_and)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
263, in __call__
self.update_user_ns(result)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
201, in update_user_ns
if self.cache_size and result is not self.shell.user_ns['_oh']:
    KeyError: '_oh'
cv2.imwrite('D:/azio/' + 'Parte_sotto.png', tr_and)
Out[58]: Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-58-166cf6855385>", line
1, in < module >
cv2.imwrite('D:/azio/' + 'Parte_sotto.png', tr_and)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
263, in __call__
self.update_user_ns(result)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
201, in update_user_ns
if self.cache_size and result is not self.shell.user_ns['_oh']:
    KeyError: '_oh'
cv2.imwrite('D:\\azio\\' + 'Parte_sotto.png', tr_and)
Out[59]: Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-59-dfc7cee725ee>", line
1, in < module >
cv2.imwrite('D:\\azio\\' + 'Parte_sotto.png', tr_and)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
263, in __call__
self.update_user_ns(result)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
201, in update_user_ns
if self.cache_size and result is not self.shell.user_ns['_oh']:
    KeyError: '_oh'
cv2.imwrite("D:\\azio\\" + "arte_sotto.png", tr_and)
Out[60]: Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-60-cf7b81fa5497>", line
1, in < module >
cv2.imwrite("D:\\azio\\" + "arte_sotto.png", tr_and)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
263, in __call__
self.update_user_ns(result)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
201, in update_user_ns
if self.cache_size and result is not self.shell.user_ns['_oh']:
    KeyError: '_oh'
print("D:\\azio\\" + "arte_sotto.png")
D:\azio\arte_sotto.png
result = pytesseract.image_to_string(tr_and)
print(result)
cul
corrispondono
le
induttanze
di
dispersione(6.29)
1.9533
mH
9.040076
mH(oyvero
3.1396
mH
riportata
al
primario)
APprossimando
la
totale
induttanza
di
dispersione
ista
al
primario
come

result1 = pytesseract.image_to_string(img_Re)
print(result1)

fona
'g U5,
Fetengicoello
gj
ertpondente
af
Valor
Caloleto
dale
sozione
gS
nent
edi
campo,
‘mapnetica(r]


ister(1
m)

@


PS
ai
Atte
Betta
ae
7
apessainente
Alle, Figs) 6: 10: spa
immagazzinata, calcolata
con(6.25)
6
PUPS
em.Ueno
pe
Wm
~ 2.547
mJ
Peso
Clsimento
principale(45.5906), secondario
¢ risus
praticameme
concentrata
1.599 %).Nel
ferro
una
quant
noone
ss
(42, 8796)
e
nello
spazio
circostante( |
Dalla(6.26)
si
calcola
sempre
Wn = 2.547
mJ
iio © 1.5704
tJ
nclr
'avvolgimento secondario,
4
cui
0.9766
mJ
nell
'avvolgimento primar
IMlussi
concatenari, dalla(6.27), sono
1.9533
mVs
0.35488
mVs

cui
corrispondono
Je
induttanze
di
dispersione(6.29)
5.1710)
evisto,

9533
mH
Lie
9.040076
mH(ovvero
3.1396
mH
riportata
al
primario)
Lae
Approssimando
la
totale
induttanza
di
dispersione
vista
al
primario
come
pug

imgBlank_frame1 = np.zeros((4608, 3456, 3), np.uint8)
imgBlank_mask2 = cv2.rectangle(imgBlank_frame, (0, 3800)(4608, 3456), (255, 255, 255), -1)
                 < string >:1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
<>:1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< ipython - input - 67 - 9
ea7303f5d55 >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
imgBlank_mask2 = cv2.rectangle(imgBlank_frame, (0, 3800)(4608, 3456), (255, 255, 255), -1)
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-67-9ea7303f5d55>", line
1, in < module >
        imgBlank_mask2 = cv2.rectangle(imgBlank_frame, (0, 3800)(4608, 3456), (255, 255, 255), -1)
TypeError: 'tuple'
object is not callable
imgBlank_mask2 = cv2.rectangle(imgBlank_frame1, (0, 3800)(4608, 3456), (255, 255, 255), -1)
                 < string >:1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< string >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
<>:1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
< ipython - input - 68 - d5bd8f67407d >: 1: SyntaxWarning: 'tuple'
object is not callable;
perhaps
you
missed
a
comma?
imgBlank_mask2 = cv2.rectangle(imgBlank_frame1, (0, 3800)(4608, 3456), (255, 255, 255), -1)
Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-68-d5bd8f67407d>", line
1, in < module >
        imgBlank_mask2 = cv2.rectangle(imgBlank_frame1, (0, 3800)(4608, 3456), (255, 255, 255), -1)
TypeError: 'tuple'
object is not callable
imgBlank_mask2 = cv2.rectangle(imgBlank_frame1, (0, 3800), (4608, 3456), (255, 255, 255), -1)
tr_and1 = cv2.bitwise_and(img, imgBlank_mask2)
result2 = pytesseract.image_to_string(tr_and1)
print(result2)
L
26 = 0.040076
mH(ovvero
3.1396
mH
riportata
al
primario)

Approssimando
la
totale
induttanza
di
dispersione
vista
al
primario
come

tr_xor1 = cv2.bitwise_xor(img, imgBlank_mask2)
cv2.imshow('tr_xor1', tr_xor1)
tr_or1 = cv2.bitwise_or(img, imgBlank_mask2)
cv2.imshow('tr_or1', tr_or1)
cv2.imwrite('C:/Users/leeon/Pictures/Atest-tesseract/' + 'Parte_sotto2.png', tr_and)
Out[77]: Traceback(most
recent
call
last):
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\interactiveshell.py", line
3417, in run_code
exec(code_obj, self.user_global_ns, self.user_ns)
File
"<ipython-input-77-44d0317dea19>", line
1, in < module >
        cv2.imwrite('C:/Users/leeon/Pictures/Atest-tesseract/' + 'Parte_sotto2.png', tr_and)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
263, in __call__
self.update_user_ns(result)
File
"C:\Users\leeon\PycharmProjects\upl\venv\lib\site-packages\IPython\core\displayhook.py", line
201, in update_user_ns
if self.cache_size and result is not self.shell.user_ns['_oh']:
    KeyError: '_oh'
