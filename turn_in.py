import pyautogui
import time

number_of_turnins = 25

config = [
    [1786, 555], 
    [2033, 582], 
    [2059, 608], 
    [2045, 626]
    ]

print('starting up turn in process starting in 10 sec.  Make sure to hover over the turnin you are ready to start')
time.sleep(10)
config[0][0] = pyautogui.position().x
config[0][1] = pyautogui.position().y

while number_of_turnins > 0:
    pyautogui.moveTo(x = config[0][0], y = config[0][1])
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    time.sleep(0.15)

    pyautogui.moveTo(x = config[1][0], y = config[1][1])
    pyautogui.mouseDown(button='right')
    pyautogui.mouseUp(button='right')

    time.sleep(0.15)

    pyautogui.moveTo(x = config[2][0], y = config[2][1])
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    time.sleep(0.15)

    pyautogui.moveTo(x = config[3][0], y = config[3][1])
    pyautogui.mouseDown(button='left')
    pyautogui.mouseUp(button='left')

    number_of_turnins -= 1

    time.sleep(0.5)