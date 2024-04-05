import pyautogui
import time

pos1 = (0,0)
pos2 = (0,0)
pos3 = (0,0)
pos4 = (0,0)

config = [[0,0],[0,0],[0,0],[0,0]]

print('Lets get configured!')
print('click on the appraiser and hover over your turn in')
time.sleep(5)
config[0][0] = pyautogui.position().x
config[0][1] = pyautogui.position().y
pyautogui.mouseDown(button='left')
pyautogui.mouseUp(button='left')

print('Now hover over the item request box')
time.sleep(5)
config[1][0] = pyautogui.position().x
config[1][1] = pyautogui.position().y
pyautogui.mouseDown(button='right')
pyautogui.mouseUp(button='right')

print('Now hover over the item youre going to turn in (top left corner)')
time.sleep(5)
config[2][0] = pyautogui.position().x
config[2][1] = pyautogui.position().y
pyautogui.mouseDown(button='left')
pyautogui.mouseUp(button='left')

print('now hover over the "hand over" button')
time.sleep(5)
config[3][0] = pyautogui.position().x
config[3][1] = pyautogui.position().y
pyautogui.mouseDown(button='left')
pyautogui.mouseUp(button='left')

print(config)