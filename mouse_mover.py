import pyautogui
import random
import time

for i in range(1,500):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pyautogui.moveTo(x, y)

    local_time = time.localtime()
    timer = time.strftime("%I:%M:%S %p", local_time)

    print("Mouse moved: " + str(timer))
    time.sleep(5)

