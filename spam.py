import pyautogui, time
position = pyautogui.position()
pesan = "NGEBO TERUSS!!!!"
time.sleep(10)
for a in range(20):
    pyautogui.click(position.x,position.y)
    pyautogui.typewrite(pesan)
    print(pesan)
    time.sleep(0.5)
    pyautogui.press("enter")