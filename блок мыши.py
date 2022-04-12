import pyautogui
import keyboard
import time

stopKey = "s" #Клавиша остановки - это кнопка, которую нужно нажать для остановки. вы также можете использовать сочетание клавиш, например ctrl + s
maxX, maxY = pyautogui.size() #получить максимальный размер экрана

while True:
    if keyboard.is_pressed(stopKey):
        break
    else:
        pyautogui.click(button='left')
        time.sleep(0.1)
        pyautogui.moveTo(maxX/2, maxY/2) #переместите мышь в центр экрана