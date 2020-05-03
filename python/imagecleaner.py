#!/usr/bin/env python3

import time
import pyautogui

def cleanup_frame():
    # activate photos window
    pyautogui.moveTo(976, 256, 1)
    pyautogui.click()

    # click edit
    pyautogui.moveTo(1212, 53, 1)
    pyautogui.click()

    # click ...
    pyautogui.moveTo(1009, 49, 1)
    pyautogui.click()

    # click markup
    pyautogui.moveTo(1036, 81, 0.5)
    pyautogui.click()

    # get shape
    pyautogui.moveTo(159, 89, 1)
    pyautogui.click()
    pyautogui.moveTo(139, 133, 0.5)
    pyautogui.click()
    
    # drag shape to the good position
    pyautogui.moveTo(749, 421, 1)
    pyautogui.dragTo(1183, 434, 0.5, button="left")
    pyautogui.moveTo(550, 421, 1)
    pyautogui.dragTo(767, 720, 0.5, button="left")
    
    # copy shape
    pyautogui.hotkey("command", "c")

    # paste shape to clean up the area
    for i in range(20):
        time.sleep(0.1)
        pyautogui.hotkey("command", "v")

    # click save
    pyautogui.moveTo(1182, 51, 1)
    pyautogui.click()

    # click done
    pyautogui.moveTo(1207, 54, 1)
    pyautogui.click()

    # activate photos window
    pyautogui.moveTo(976, 256, 1)
    pyautogui.click()

    # press right arrow key
    time.sleep(0.5)
    pyautogui.press("right")


if __name__ == "__main__":
    for i in range(1):
        cleanup_frame()

        print("END")

