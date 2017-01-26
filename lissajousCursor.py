import time
import math
import win32api

#カーソルを動かす(リサージュ曲線)
mouseX = win32api.GetCursorPos()[0]
mouseY = win32api.GetCursorPos()[1]
radius = 100
degree =1080
for i in range(degree):
    time.sleep(0.001) #必要あらば
    x = mouseX + int(radius * math.sin(math.radians(2/2*i)))
    y = mouseY + int(radius * math.cos(math.radians(3/2*i)))
    win32api.SetCursorPos((x,y))
win32api.SetCursorPos((mouseX,mouseY))