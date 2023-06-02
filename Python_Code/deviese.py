import time
import pyautogui
pyautogui.hotkey("win")
time.sleep(2)
pyautogui.typewrite("free")
time.sleep(2)
pyautogui.press("enter")
time.sleep(10)#tempo per aprire il free cam
pyautogui.click(788,776)#inizia a cliccare su newrecording

time.sleep(1)

#pyautogui.click(636,1100,clicks=2, interval=0.25)
#pyautogui.typewrite("2100")#asse x
#pyautogui.press("enter")
pyautogui.click(726,1103)
time.sleep(1)# altezza
pyautogui.click(684,1248)
time.sleep(1)
#pyautogui.click(760,1103) Point(x=831, y=1338)
pyautogui.click(817,1227)
#pyautogui.click(416,1102,clicks=2, interval=0.25)
#pyautogui.typewrite("1100")
#pyautogui.press("enter")

# pyautogui.click(725,1102)
# time.sleep(1)
# pyautogui.click(670,1192)#seleziona il formato di screen
time.sleep(1)
#pyautogui.click(36,1402) #clicca il bottore record
# pyautogui.click(96,1405) #clicca il bottore record
pyautogui.click(287,1191)
pyautogui.click(180,214)
time.sleep(54000) #tempo di registrazione 6 uguale a 2 sec di registra .
#time.sleep(80)
# allora 8 deve essere 4 sec
#        10 equivale a 6 sec
#        quidni i primi 4 sec sono da scartare
pyautogui.hotkey("esc")

time.sleep(3*10)# aspettare per la preparazione di file da salvare

pyautogui.click(48,120) # apre file save option
time.sleep(2)#posso variare causano solo ritardo , serve x sicurezza che non c'è blocco in divedo
pyautogui.click(116,300) #clik save file
time.sleep(2)
pyautogui.click(1908,1396) # salva il file finale
