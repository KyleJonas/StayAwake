import time, pyautogui
import PySimpleGUI as sg
import multiprocessing

# GUI that 
def GUI():
    sg.theme('Dark')
    layout = [
        [sg.Text('StayAwake is now running.\nYou can keep it minised, and it will continue running.\nClose it to disable it.')]
    ]
    window = sg.Window('StayAwake', layout)
    
    p2 = multiprocessing.Process(target = awake)
    p2.start()
    
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED: # Closes window or clicks cancel
            if p2.is_alive(): 
                p2.terminate()
            break

# Presses f15 every 2 min until gui closed
def awake():
    while True:
        pyautogui.press('f15')
        time.sleep(120)

if __name__ == '__main__':
    p1 = multiprocessing.Process(target = GUI)
    p1.start()
