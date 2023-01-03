import pyautogui
import random
import time

### simple version ###
# x, y = screen.size()
# while True:
#     x1 = random.randint(0, x)
#     y1 = random.randint(0, y)
#     screen.moveTo(x1, y1)
#     screen.click(int(x/2), y-30)
#     time.sleep(60)

for i in range(1,500):
    x = random.randint(0, 500)
    y = random.randint(0, 500)
    pyautogui.moveTo(x, y)

    local_time = time.localtime()
    timer = time.strftime("%I:%M:%S %p", local_time)

    print("Mouse moved: " + str(timer))
    time.sleep(5)

