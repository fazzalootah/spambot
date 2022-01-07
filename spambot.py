import pyautogui
msg = input("Enter the message: ")
n = input("How many times ?: ")
for i in range(0,int(n)):
  pyautogui.typewrite(msg + '\n')
