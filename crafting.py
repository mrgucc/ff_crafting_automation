import pyautogui
import time

intro_countdown = 10

number_crafts = 20
# number_crafts1 = 19
# number_crafts2 = 21

# need ~ 55 total to get to 60
time_to_craft = 35

synth_coords = [0, 0]

print('make sure to hover over the synthesize button to register your coordinates!')
while intro_countdown > 0:
    print('Starting crafting in...' + str(intro_countdown))
    intro_countdown -= 1
    time.sleep(1)

synth_coords[0] = pyautogui.position().x
synth_coords[1] = pyautogui.position().y

while number_crafts > 0:
    print('time remaining: ' + str(((time_to_craft + 3) * (number_crafts)) / 60 ))
    pyautogui.moveTo(x = synth_coords[0], y = synth_coords[1])
    pyautogui.mouseDown()
    pyautogui.mouseUp()
    time.sleep(3)
    pyautogui.press('1')
    time.sleep(time_to_craft)
    number_crafts -= 1

print('all done :)')