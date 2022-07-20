import pyautogui,  webbrowser
from time import sleep

webbrowser.open('https://web.whatsapp.com/send?phone=') #here you put the phone number and the prefix of the country where you live
sleep(10)

with open ("mensajes.txt", "r") as file:
    for line in file:
        pyautogui.typewrite(line)
        pyautogui.press("enter")


